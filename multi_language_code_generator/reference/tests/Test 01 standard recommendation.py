import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_standard_recommendation():
    engine = RecommendationEngine()
    payload = {
        "user": {"id": "u1", "interests": ["python", "backend", "databases"]},
        "items": [
            {"id": "i1", "name": "Intro to Django",     "tags": ["python", "backend"],    "popularity": 900},
            {"id": "i2", "name": "React for Beginners", "tags": ["javascript", "frontend"],"popularity": 1000},
            {"id": "i3", "name": "PostgreSQL Deep Dive","tags": ["databases", "backend"],  "popularity": 700},
            {"id": "i4", "name": "Python Data Science", "tags": ["python", "databases"],   "popularity": 800},
        ],
        "seen_item_ids": [],
        "top_n": 3,
    }
    result = engine.recommend(payload)
    ids = [r["item_id"] for r in result["recommendations"]]
    assert result["user_id"] == "u1"
    assert ids == ["i1", "i4", "i3"]
    assert len(result["recommendations"]) == 3
    assert result["recommendations"][0]["rank"] == 1

if __name__ == "__main__":
    test_standard_recommendation()
    print("PASS")
