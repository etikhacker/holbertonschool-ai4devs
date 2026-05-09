"""
Tests for RecommendationEngine — Reference Implementation
==========================================================
Run with:  python -m pytest tests/test_recommendation_engine.py -v
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ids(result: dict) -> list[str]:
    return [r["item_id"] for r in result["recommendations"]]

def scores(result: dict) -> list[float]:
    return [r["score"] for r in result["recommendations"]]

def names(result: dict) -> list[str]:
    return [r["item_name"] for r in result["recommendations"]]


# ---------------------------------------------------------------------------
# Test Case 1 — Standard recommendation (spec example)
# ---------------------------------------------------------------------------

def test_standard_recommendation():
    payload = {
        "user": {"id": "u1", "interests": ["python", "backend", "databases"]},
        "items": [
            {"id": "i1", "name": "Intro to Django",    "tags": ["python", "backend"],    "popularity": 900},
            {"id": "i2", "name": "React for Beginners","tags": ["javascript", "frontend"],"popularity": 1000},
            {"id": "i3", "name": "PostgreSQL Deep Dive","tags": ["databases", "backend"], "popularity": 700},
            {"id": "i4", "name": "Python Data Science", "tags": ["python", "databases"],  "popularity": 800},
        ],
        "seen_item_ids": [],
        "top_n": 3,
    }
    result = engine.recommend(payload)
    assert result["user_id"] == "u1"
    assert ids(result) == ["i1", "i4", "i3"]
    assert len(result["recommendations"]) == 3
    assert result["recommendations"][0]["rank"] == 1


# ---------------------------------------------------------------------------
# Test Case 2 — Seen items are excluded
# ---------------------------------------------------------------------------

def test_seen_items_excluded():
    payload = {
        "user": {"id": "u2", "interests": ["python", "backend"]},
        "items": [
            {"id": "i1", "name": "Intro to Django",    "tags": ["python", "backend"], "popularity": 900},
            {"id": "i2", "name": "Flask Microservices","tags": ["python", "backend"], "popularity": 800},
        ],
        "seen_item_ids": ["i1"],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    assert ids(result) == ["i2"]
    assert len(result["recommendations"]) == 1


# ---------------------------------------------------------------------------
# Test Case 3 — Empty user interests → popularity-only ranking
# ---------------------------------------------------------------------------

def test_empty_interests_uses_popularity():
    payload = {
        "user": {"id": "u3", "interests": []},
        "items": [
            {"id": "i1", "name": "Machine Learning A-Z", "tags": ["python", "ml"], "popularity": 500},
            {"id": "i2", "name": "Docker Essentials",    "tags": ["devops"],       "popularity": 800},
            {"id": "i3", "name": "SQL Masterclass",      "tags": ["databases"],    "popularity": 300},
        ],
        "seen_item_ids": [],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    # Highest popularity wins: i2 (800) then i1 (500)
    assert ids(result) == ["i2", "i1"]
    # Tag component is 0 for all; scores are purely popularity-based
    for r in result["recommendations"]:
        assert r["matched_tags"] == []


# ---------------------------------------------------------------------------
# Test Case 4 — Tie-breaking alphabetically by item name
# ---------------------------------------------------------------------------

def test_tie_breaking_alphabetical():
    payload = {
        "user": {"id": "u4", "interests": ["devops"]},
        "items": [
            {"id": "i1", "name": "Kubernetes Guide", "tags": ["devops"], "popularity": 600},
            {"id": "i2", "name": "Ansible Basics",   "tags": ["devops"], "popularity": 600},
        ],
        "seen_item_ids": [],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    assert scores(result)[0] == scores(result)[1], "Scores should be equal"
    assert names(result) == ["Ansible Basics", "Kubernetes Guide"]


# ---------------------------------------------------------------------------
# Test Case 5 — All items already seen → empty recommendations
# ---------------------------------------------------------------------------

def test_all_items_seen_returns_empty():
    payload = {
        "user": {"id": "u5", "interests": ["python"]},
        "items": [
            {"id": "i1", "name": "Python Basics",   "tags": ["python"], "popularity": 700},
            {"id": "i2", "name": "Advanced Python", "tags": ["python"], "popularity": 850},
        ],
        "seen_item_ids": ["i1", "i2"],
        "top_n": 3,
    }
    result = engine.recommend(payload)
    assert result["recommendations"] == []


# ---------------------------------------------------------------------------
# Test Case 6 — Item with no tags ranked by popularity only
# ---------------------------------------------------------------------------

def test_item_with_no_tags_ranked_by_popularity():
    payload = {
        "user": {"id": "u6", "interests": ["python", "ml"]},
        "items": [
            {"id": "i1", "name": "Python ML Guide", "tags": ["python", "ml"], "popularity": 400},
            {"id": "i2", "name": "Mystery Course",  "tags": [],               "popularity": 1000},
        ],
        "seen_item_ids": [],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    recs = {r["item_id"]: r for r in result["recommendations"]}
    assert recs["i2"]["matched_tags"] == []
    assert recs["i2"]["score"] == pytest.approx(0.3, abs=0.001)
    # i1 should still rank higher (higher combined score)
    assert ids(result)[0] == "i1"


# ---------------------------------------------------------------------------
# Test Case 7 — top_n larger than eligible items → return all eligible
# ---------------------------------------------------------------------------

def test_top_n_exceeds_eligible_items():
    payload = {
        "user": {"id": "u7", "interests": ["security"]},
        "items": [
            {"id": "i1", "name": "Ethical Hacking", "tags": ["security"], "popularity": 500},
        ],
        "seen_item_ids": [],
        "top_n": 10,
    }
    result = engine.recommend(payload)
    assert len(result["recommendations"]) == 1
    assert result["recommendations"][0]["score"] == 1.0


# ---------------------------------------------------------------------------
# Test Case 8 — top_n = 0 → empty recommendations
# ---------------------------------------------------------------------------

def test_top_n_zero_returns_empty():
    payload = {
        "user": {"id": "u8", "interests": ["python"]},
        "items": [
            {"id": "i1", "name": "Python Basics", "tags": ["python"], "popularity": 500},
        ],
        "seen_item_ids": [],
        "top_n": 0,
    }
    result = engine.recommend(payload)
    assert result["recommendations"] == []


# ---------------------------------------------------------------------------
# Test Case 9 — Empty items catalogue → empty recommendations
# ---------------------------------------------------------------------------

def test_empty_catalogue_returns_empty():
    payload = {
        "user": {"id": "u9", "interests": ["python"]},
        "items": [],
        "seen_item_ids": [],
        "top_n": 3,
    }
    result = engine.recommend(payload)
    assert result["recommendations"] == []


# ---------------------------------------------------------------------------
# Test Case 10 — Duplicate user interests are deduplicated
# ---------------------------------------------------------------------------

def test_duplicate_interests_deduplicated():
    # interests has "python" twice; total_user_tags should be 1, not 2
    payload = {
        "user": {"id": "u10", "interests": ["python", "python"]},
        "items": [
            {"id": "i1", "name": "Python Basics", "tags": ["python"], "popularity": 1000},
        ],
        "seen_item_ids": [],
        "top_n": 1,
    }
    result = engine.recommend(payload)
    # With 1 unique interest and 1 match: tag_component = 1.0 * 0.7 = 0.7
    # pop_component = 1.0 * 0.3 = 0.3 → total = 1.0
    assert result["recommendations"][0]["score"] == 1.0


# ---------------------------------------------------------------------------
# Test Case 11 — All items have 0 popularity → tag-only ranking
# ---------------------------------------------------------------------------

def test_zero_popularity_all_items():
    payload = {
        "user": {"id": "u11", "interests": ["cloud", "devops"]},
        "items": [
            {"id": "i1", "name": "AWS Basics",    "tags": ["cloud"],           "popularity": 0},
            {"id": "i2", "name": "Terraform 101", "tags": ["devops", "cloud"], "popularity": 0},
        ],
        "seen_item_ids": [],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    recs = {r["item_id"]: r for r in result["recommendations"]}
    # i2 matches 2/2 tags → tag_component = 0.7; pop_component = 0
    assert recs["i2"]["score"] == pytest.approx(0.7, abs=0.001)
    # i1 matches 1/2 tags → tag_component = 0.35
    assert recs["i1"]["score"] == pytest.approx(0.35, abs=0.001)
    assert ids(result)[0] == "i2"


# ---------------------------------------------------------------------------
# Test Case 12 — Ranks are sequential starting from 1
# ---------------------------------------------------------------------------

def test_ranks_are_sequential():
    payload = {
        "user": {"id": "u12", "interests": ["python", "ml", "data"]},
        "items": [
            {"id": f"i{i}", "name": f"Course {i}", "tags": ["python"], "popularity": i * 100}
            for i in range(1, 6)
        ],
        "seen_item_ids": [],
        "top_n": 5,
    }
    result = engine.recommend(payload)
    assert [r["rank"] for r in result["recommendations"]] == [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# Test Case 13 — Invalid payload raises ValueError
# ---------------------------------------------------------------------------

def test_invalid_payload_raises():
    with pytest.raises((ValueError, TypeError, AttributeError)):
        engine.recommend("not a dict")


# ---------------------------------------------------------------------------
# Test Case 14 — matched_tags only contains user interest tags
# ---------------------------------------------------------------------------

def test_matched_tags_subset_of_interests():
    payload = {
        "user": {"id": "u14", "interests": ["python"]},
        "items": [
            {"id": "i1", "name": "Full Stack Python", "tags": ["python", "javascript", "docker"], "popularity": 500},
        ],
        "seen_item_ids": [],
        "top_n": 1,
    }
    result = engine.recommend(payload)
    assert result["recommendations"][0]["matched_tags"] == ["python"]
