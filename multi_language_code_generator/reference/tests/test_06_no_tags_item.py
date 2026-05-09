import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_item_with_no_tags_ranked_by_popularity():
    engine = RecommendationEngine()
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
    assert abs(recs["i2"]["score"] - 0.3) < 0.001
    assert [r["item_id"] for r in result["recommendations"]][0] == "i1"

if __name__ == "__main__":
    test_item_with_no_tags_ranked_by_popularity()
    print("PASS")
