import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_all_items_seen_returns_empty():
    engine = RecommendationEngine()
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

if __name__ == "__main__":
    test_all_items_seen_returns_empty()
    print("PASS")
