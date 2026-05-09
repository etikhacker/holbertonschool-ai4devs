# Cross-Language Specification — Recommendation Engine

## Project: `multi_language_code_generator` — `holbertonschool-ai4devs`

---

## Algorithm

A **content-based recommendation engine** that scores and ranks items for a given user based on the overlap between the user's interest tags and each item's tags, weighted by item popularity.

The scoring formula for each item is:

```
score(user, item) = (matching_tags / total_user_tags) * 0.7
                  + (item.popularity / max_popularity) * 0.3
```

Steps:
1. Load the user profile (list of interest tags).
2. Load the item catalogue (each item has a name, tags, and a popularity score).
3. Exclude items the user has already seen.
4. For every remaining item, compute the weighted score above.
5. Return the top-N items sorted by score descending; break ties alphabetically by item name.

---

## Input Format

A single JSON object with three keys:

```json
{
  "user": {
    "id": "string",
    "interests": ["tag1", "tag2", "..."]
  },
  "items": [
    {
      "id": "string",
      "name": "string",
      "tags": ["tag1", "tag2", "..."],
      "popularity": 0
    }
  ],
  "seen_item_ids": ["string"],
  "top_n": 3
}
```

| Field | Type | Description |
|---|---|---|
| `user.id` | string | Unique user identifier |
| `user.interests` | string[] | Tags describing the user's preferences |
| `items` | object[] | Full item catalogue |
| `items[].popularity` | integer ≥ 0 | Absolute popularity count (e.g. views, purchases) |
| `seen_item_ids` | string[] | Item IDs to exclude from results |
| `top_n` | integer ≥ 1 | Maximum number of results to return |

---

## Output Format

A JSON object with a ranked list of recommendations:

```json
{
  "user_id": "string",
  "recommendations": [
    {
      "rank": 1,
      "item_id": "string",
      "item_name": "string",
      "score": 0.00,
      "matched_tags": ["tag1"]
    }
  ]
}
```

Scores are rounded to 4 decimal places. If fewer than `top_n` eligible items exist, return only the available ones.

---

## Edge Cases

| # | Edge Case | Expected Behaviour |
|---|---|---|
| 1 | `user.interests` is empty (`[]`) | Tag-overlap component is 0 for all items; ranking is driven entirely by popularity. No error raised. |
| 2 | All items are in `seen_item_ids` | Return `{"recommendations": []}` — empty list, no error. |
| 3 | `items` catalogue is empty | Return `{"recommendations": []}` — empty list, no error. |
| 4 | An item has `tags: []` | Matching tags = 0; item may still rank via popularity component. |
| 5 | Two items share the same computed score | Tie broken alphabetically (A–Z) by `item_name`. |
| 6 | `popularity` is 0 for all items | Popularity component = 0 for all; ranking driven entirely by tag overlap. |
| 7 | `top_n` exceeds the number of eligible items | Return all eligible items ranked; do not pad with nulls or raise an error. |
| 8 | `user.interests` contains duplicate tags | Deduplicate before computing `total_user_tags` to avoid inflating the denominator. |
| 9 | Item tags contain values not present in any user profile | Those tags contribute 0 to the score; no error raised. |
| 10 | `top_n` is 0 | Return `{"recommendations": []}` — empty list, no error. |

---

## Test Cases

### Test Case 1 — Standard Recommendation

**Input:**
```json
{
  "user": { "id": "u1", "interests": ["python", "backend", "databases"] },
  "items": [
    { "id": "i1", "name": "Intro to Django", "tags": ["python", "backend"], "popularity": 900 },
    { "id": "i2", "name": "React for Beginners", "tags": ["javascript", "frontend"], "popularity": 1000 },
    { "id": "i3", "name": "PostgreSQL Deep Dive", "tags": ["databases", "backend"], "popularity": 700 },
    { "id": "i4", "name": "Python Data Science", "tags": ["python", "databases"], "popularity": 800 }
  ],
  "seen_item_ids": [],
  "top_n": 3
}
```

**Expected Output:**
```json
{
  "user_id": "u1",
  "recommendations": [
    { "rank": 1, "item_id": "i1", "item_name": "Intro to Django",     "score": 0.7467, "matched_tags": ["python", "backend"] },
    { "rank": 2, "item_id": "i4", "item_name": "Python Data Science", "score": 0.7067, "matched_tags": ["python", "databases"] },
    { "rank": 3, "item_id": "i3", "item_name": "PostgreSQL Deep Dive","score": 0.6767, "matched_tags": ["databases", "backend"] }
  ]
}
```

---

### Test Case 2 — Seen Items Excluded

**Input:**
```json
{
  "user": { "id": "u2", "interests": ["python", "backend"] },
  "items": [
    { "id": "i1", "name": "Intro to Django",   "tags": ["python", "backend"], "popularity": 900 },
    { "id": "i2", "name": "Flask Microservices","tags": ["python", "backend"], "popularity": 800 }
  ],
  "seen_item_ids": ["i1"],
  "top_n": 2
}
```

**Expected Output:**
```json
{
  "user_id": "u2",
  "recommendations": [
    { "rank": 1, "item_id": "i2", "item_name": "Flask Microservices", "score": 0.9400, "matched_tags": ["python", "backend"] }
  ]
}
```

*`i1` is excluded because it appears in `seen_item_ids`. Only one eligible item remains, so `top_n: 2` returns one result.*

---

### Test Case 3 — Empty User Interests (Popularity-Only Ranking)

**Input:**
```json
{
  "user": { "id": "u3", "interests": [] },
  "items": [
    { "id": "i1", "name": "Machine Learning A–Z", "tags": ["python", "ml"], "popularity": 500 },
    { "id": "i2", "name": "Docker Essentials",    "tags": ["devops"],       "popularity": 800 },
    { "id": "i3", "name": "SQL Masterclass",      "tags": ["databases"],    "popularity": 300 }
  ],
  "seen_item_ids": [],
  "top_n": 2
}
```

**Expected Output:**
```json
{
  "user_id": "u3",
  "recommendations": [
    { "rank": 1, "item_id": "i2", "item_name": "Docker Essentials",    "score": 0.3000, "matched_tags": [] },
    { "rank": 2, "item_id": "i1", "item_name": "Machine Learning A–Z", "score": 0.1875, "matched_tags": [] }
  ]
}
```

*With no interests, tag overlap = 0 for all; ranking is purely by `popularity / max_popularity * 0.3`.*

---

### Test Case 4 — Tie-Breaking by Name

**Input:**
```json
{
  "user": { "id": "u4", "interests": ["devops"] },
  "items": [
    { "id": "i1", "name": "Kubernetes Guide", "tags": ["devops"], "popularity": 600 },
    { "id": "i2", "name": "Ansible Basics",   "tags": ["devops"], "popularity": 600 }
  ],
  "seen_item_ids": [],
  "top_n": 2
}
```

**Expected Output:**
```json
{
  "user_id": "u4",
  "recommendations": [
    { "rank": 1, "item_id": "i2", "item_name": "Ansible Basics",   "score": 1.0000, "matched_tags": ["devops"] },
    { "rank": 2, "item_id": "i1", "item_name": "Kubernetes Guide", "score": 1.0000, "matched_tags": ["devops"] }
  ]
}
```

*Both items score 1.0000; "Ansible Basics" ranks first because "A" precedes "K" alphabetically.*

---

### Test Case 5 — All Items Already Seen

**Input:**
```json
{
  "user": { "id": "u5", "interests": ["python"] },
  "items": [
    { "id": "i1", "name": "Python Basics",    "tags": ["python"], "popularity": 700 },
    { "id": "i2", "name": "Advanced Python",  "tags": ["python"], "popularity": 850 }
  ],
  "seen_item_ids": ["i1", "i2"],
  "top_n": 3
}
```

**Expected Output:**
```json
{
  "user_id": "u5",
  "recommendations": []
}
```

*Every item is in `seen_item_ids`; no eligible items remain.*

---

### Test Case 6 — Item with No Tags Still Ranked by Popularity

**Input:**
```json
{
  "user": { "id": "u6", "interests": ["python", "ml"] },
  "items": [
    { "id": "i1", "name": "Python ML Guide", "tags": ["python", "ml"], "popularity": 400 },
    { "id": "i2", "name": "Mystery Course",  "tags": [],               "popularity": 1000 }
  ],
  "seen_item_ids": [],
  "top_n": 2
}
```

**Expected Output:**
```json
{
  "user_id": "u6",
  "recommendations": [
    { "rank": 1, "item_id": "i1", "item_name": "Python ML Guide", "score": 0.8200, "matched_tags": ["python", "ml"] },
    { "rank": 2, "item_id": "i2", "item_name": "Mystery Course",  "score": 0.3000, "matched_tags": [] }
  ]
}
```

*`i2` has no matching tags but its high popularity (1000 = max) still earns it a `0.3` score, keeping it in results.*

---

### Test Case 7 — `top_n` Larger Than Eligible Items

**Input:**
```json
{
  "user": { "id": "u7", "interests": ["security"] },
  "items": [
    { "id": "i1", "name": "Ethical Hacking", "tags": ["security"], "popularity": 500 }
  ],
  "seen_item_ids": [],
  "top_n": 10
}
```

**Expected Output:**
```json
{
  "user_id": "u7",
  "recommendations": [
    { "rank": 1, "item_id": "i1", "item_name": "Ethical Hacking", "score": 1.0000, "matched_tags": ["security"] }
  ]
}
```

*Only 1 eligible item exists; returning 1 result is correct — no padding, no error.*
