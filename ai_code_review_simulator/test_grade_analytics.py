"""
Unit tests for grade_analytics.py
"""

import sys
sys.path.insert(0, '/home/claude')
from grade_analytics import calculate_gpa, get_subject_averages, identify_at_risk, generate_summary


def test_calculate_gpa_empty():
    assert calculate_gpa([]) == 0.0

def test_calculate_gpa_all_a():
    grades = [{"score": 95, "credits": 3}, {"score": 92, "credits": 3}]
    assert calculate_gpa(grades) == 4.0

def test_calculate_gpa_mixed():
    grades = [
        {"score": 95, "credits": 3},
        {"score": 75, "credits": 3},
        {"score": 55, "credits": 3},
    ]
    assert calculate_gpa(grades) == round((4.0*3 + 2.0*3 + 0.0*3) / 9, 2)

def test_get_subject_averages():
    grades = [
        {"subject": "Math", "score": 80},
        {"subject": "Math", "score": 90},
        {"subject": "English", "score": 70},
    ]
    averages = get_subject_averages(grades)
    assert averages["Math"] == 85.0
    assert averages["English"] == 70.0

def test_get_subject_averages_empty():
    assert get_subject_averages([]) == {}

def test_identify_at_risk():
    grades = [
        {"subject": "Math", "score": 80},
        {"subject": "Physics", "score": 50},
        {"subject": "English", "score": 40},
    ]
    at_risk = identify_at_risk(grades)
    assert "Physics" in at_risk
    assert "English" in at_risk
    assert "Math" not in at_risk

def test_identify_at_risk_custom_threshold():
    grades = [{"subject": "Math", "score": 75}]
    assert identify_at_risk(grades, threshold=80) == ["Math"]

def test_generate_summary():
    grades = [
        {"subject": "Math", "score": 95, "credits": 3},
        {"subject": "Physics", "score": 45, "credits": 3},
    ]
    summary = generate_summary("student_001", grades)
    assert summary["student_id"] == "student_001"
    assert summary["total_grades"] == 2
    assert "Physics" in summary["at_risk_subjects"]
    assert "Math" not in summary["at_risk_subjects"]


if __name__ == "__main__":
    test_calculate_gpa_empty()
    test_calculate_gpa_all_a()
    test_calculate_gpa_mixed()
    test_get_subject_averages()
    test_get_subject_averages_empty()
    test_identify_at_risk()
    test_identify_at_risk_custom_threshold()
    test_generate_summary()
    print("All 8 tests passed!")
