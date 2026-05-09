"""
Recommendation Engine — Reference Implementation (Python)
==========================================================
Content-based recommendation engine that scores items for a user based on:
  score = (matching_tags / total_user_tags) * 0.7
        + (item.popularity / max_popularity) * 0.3

Tie-breaking: alphabetical (A→Z) by item name.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class User:
    id: str
    interests: list[str]

    def unique_interests(self) -> list[str]:
        """Return deduplicated interest tags preserving order."""
        seen: set[str] = set()
        result: list[str] = []
        for tag in self.interests:
            if tag not in seen:
                seen.add(tag)
                result.append(tag)
        return result


@dataclass
class Item:
    id: str
    name: str
    tags: list[str]
    popularity: int


@dataclass
class Recommendation:
    rank: int
    item_id: str
    item_name: str
    score: float
    matched_tags: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "rank": self.rank,
            "item_id": self.item_id,
            "item_name": self.item_name,
            "score": self.score,
            "matched_tags": self.matched_tags,
        }


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

class RecommendationEngine:
    """Content-based recommendation engine."""

    TAG_WEIGHT: float = 0.7
    POP_WEIGHT: float = 0.3

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def recommend(self, payload: dict[str, Any]) -> dict[str, Any]:
        """
        Entry point.  Accepts the JSON payload described in the spec and
        returns a dict matching the specified output format.

        Args:
            payload: dict with keys 'user', 'items', 'seen_item_ids', 'top_n'.

        Returns:
            dict with keys 'user_id' and 'recommendations'.

        Raises:
            ValueError: if required keys are missing or types are wrong.
        """
        user, items, seen_ids, top_n = self._parse_payload(payload)

        eligible = [item for item in items if item.id not in seen_ids]

        if not eligible or top_n == 0:
            return {"user_id": user.id, "recommendations": []}

        interests = user.unique_interests()
        max_pop = max(item.popularity for item in items)  # use full catalogue

        scored = self._score_items(interests, eligible, max_pop)
        ranked = self._rank(scored, top_n)

        return {
            "user_id": user.id,
            "recommendations": [r.to_dict() for r in ranked],
        }

    # ------------------------------------------------------------------
    # Scoring
    # ------------------------------------------------------------------

    def _score_items(
        self,
        interests: list[str],
        items: list[Item],
        max_popularity: int,
    ) -> list[tuple[float, str, Item, list[str]]]:
        """
        Compute (score, name, item, matched_tags) for every eligible item.
        """
        results: list[tuple[float, str, Item, list[str]]] = []
        interest_set = set(interests)
        n_interests = len(interest_set)

        for item in items:
            matched = [t for t in item.tags if t in interest_set]

            if n_interests > 0:
                tag_component = (len(matched) / n_interests) * self.TAG_WEIGHT
            else:
                tag_component = 0.0

            if max_popularity > 0:
                pop_component = (item.popularity / max_popularity) * self.POP_WEIGHT
            else:
                pop_component = 0.0

            score = round(tag_component + pop_component, 4)
            results.append((score, item.name, item, matched))

        return results

    def _rank(
        self,
        scored: list[tuple[float, str, Item, list[str]]],
        top_n: int,
    ) -> list[Recommendation]:
        """Sort by score desc, then name asc; return top_n Recommendation objects."""
        sorted_items = sorted(scored, key=lambda x: (-x[0], x[1]))
        recommendations: list[Recommendation] = []
        for rank, (score, _, item, matched) in enumerate(sorted_items[:top_n], start=1):
            recommendations.append(
                Recommendation(
                    rank=rank,
                    item_id=item.id,
                    item_name=item.name,
                    score=score,
                    matched_tags=matched,
                )
            )
        return recommendations

    # ------------------------------------------------------------------
    # Parsing / validation
    # ------------------------------------------------------------------

    def _parse_payload(
        self, payload: dict[str, Any]
    ) -> tuple[User, list[Item], set[str], int]:
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a JSON object (dict).")

        # user
        raw_user = payload.get("user")
        if not isinstance(raw_user, dict):
            raise ValueError("'user' must be an object.")
        user = User(
            id=str(raw_user.get("id", "")),
            interests=list(raw_user.get("interests", [])),
        )

        # items
        raw_items = payload.get("items", [])
        if not isinstance(raw_items, list):
            raise ValueError("'items' must be an array.")
        items: list[Item] = []
        for raw in raw_items:
            items.append(
                Item(
                    id=str(raw.get("id", "")),
                    name=str(raw.get("name", "")),
                    tags=list(raw.get("tags", [])),
                    popularity=int(raw.get("popularity", 0)),
                )
            )

        # seen_item_ids
        seen_ids: set[str] = set(str(s) for s in payload.get("seen_item_ids", []))

        # top_n
        top_n = int(payload.get("top_n", 3))
        if top_n < 0:
            raise ValueError("'top_n' must be a non-negative integer.")

        return user, items, seen_ids, top_n
