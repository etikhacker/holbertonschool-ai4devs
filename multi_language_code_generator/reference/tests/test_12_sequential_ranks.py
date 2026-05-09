import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_ranks_are_sequential():
    engine = RecommendationEngine()
    payload = {
        "user": {"id": "u12", "interests": ["python", "ml", "data"]},
        "items": [
            {"id": f"i{i}", "name": f"Course {i}", "tags": ["python"], "popularity": i * 100}
            for i in range(1, 6)
        ],
        "seen_item_ids": [],
        "top_n": 5,
    }
    result = engine.recommend(payload)
    assert [r["rank"] for r in result["recommendations"]] == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    test_ranks_are_sequential()
    print("PASS")
