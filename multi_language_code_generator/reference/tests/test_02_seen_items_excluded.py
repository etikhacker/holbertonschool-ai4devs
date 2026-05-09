import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_seen_items_excluded():
    engine = RecommendationEngine()
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
    ids = [r["item_id"] for r in result["recommendations"]]
    assert ids == ["i2"]
    assert len(result["recommendations"]) == 1

if __name__ == "__main__":
    test_seen_items_excluded()
    print("PASS")
