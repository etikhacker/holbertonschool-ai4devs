import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_zero_popularity_all_items():
    engine = RecommendationEngine()
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
    assert abs(recs["i2"]["score"] - 0.7)  < 0.001
    assert abs(recs["i1"]["score"] - 0.35) < 0.001
    assert [r["item_id"] for r in result["recommendations"]][0] == "i2"

if __name__ == "__main__":
    test_zero_popularity_all_items()
    print("PASS")
