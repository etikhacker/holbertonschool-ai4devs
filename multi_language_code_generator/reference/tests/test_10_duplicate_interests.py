import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_duplicate_interests_deduplicated():
    engine = RecommendationEngine()
    # "python" appears twice; total_user_tags must be 1, not 2
    payload = {
        "user": {"id": "u10", "interests": ["python", "python"]},
        "items": [
            {"id": "i1", "name": "Python Basics", "tags": ["python"], "popularity": 1000},
        ],
        "seen_item_ids": [],
        "top_n": 1,
    }
    result = engine.recommend(payload)
    # 1/1 tag match * 0.7 + 1.0 * 0.3 = 1.0
    assert result["recommendations"][0]["score"] == 1.0

if __name__ == "__main__":
    test_duplicate_interests_deduplicated()
    print("PASS")
