import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_top_n_exceeds_eligible_items():
    engine = RecommendationEngine()
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

if __name__ == "__main__":
    test_top_n_exceeds_eligible_items()
    print("PASS")
