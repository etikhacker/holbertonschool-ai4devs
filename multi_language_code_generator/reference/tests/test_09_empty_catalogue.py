import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_empty_catalogue_returns_empty():
    engine = RecommendationEngine()
    payload = {
        "user": {"id": "u9", "interests": ["python"]},
        "items": [],
        "seen_item_ids": [],
        "top_n": 3,
    }
    result = engine.recommend(payload)
    assert result["recommendations"] == []

if __name__ == "__main__":
    test_empty_catalogue_returns_empty()
    print("PASS")
