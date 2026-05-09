import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommendation_engine import RecommendationEngine

def test_tie_breaking_alphabetical():
    engine = RecommendationEngine()
    payload = {
        "user": {"id": "u4", "interests": ["devops"]},
        "items": [
            {"id": "i1", "name": "Kubernetes Guide", "tags": ["devops"], "popularity": 600},
            {"id": "i2", "name": "Ansible Basics",   "tags": ["devops"], "popularity": 600},
        ],
        "seen_item_ids": [],
        "top_n": 2,
    }
    result = engine.recommend(payload)
    scores = [r["score"] for r in result["recommendations"]]
    names  = [r["item_name"] for r in result["recommendations"]]
    assert scores[0] == scores[1], "Scores should be equal (tie)"
    assert names == ["Ansible Basics", "Kubernetes Guide"]

if __name__ == "__main__":
    test_tie_breaking_alphabetical()
    print("PASS")
