import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_top_n_zero_returns_empty():
    engine = RecommendationEngine()
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

if __name__ == "__main__":
    test_top_n_zero_returns_empty()
    print("PASS")
