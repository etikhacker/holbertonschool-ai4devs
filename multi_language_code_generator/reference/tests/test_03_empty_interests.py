import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_empty_interests_uses_popularity():
    engine = RecommendationEngine()
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
    ids = [r["item_id"] for r in result["recommendations"]]
    assert ids == ["i2", "i1"]
    for r in result["recommendations"]:
        assert r["matched_tags"] == []

if __name__ == "__main__":
    test_empty_interests_uses_popularity()
    print("PASS")
