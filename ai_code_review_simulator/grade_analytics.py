"""
Grade Analytics Module – EduTrack
Provides functions to compute GPA, subject averages,
at-risk detection, and full student performance summaries.
"""


def calculate_gpa(grades):
    """
    Calculate GPA from a list of grade records.

    Args:
        grades (list): List of dicts with 'score' (0-100) and 'credits' keys.

    Returns:
        float: GPA on a 4.0 scale, or 0.0 if no grades provided.
    """
    if not grades:
        return 0.0

    total_points = 0.0
    total_credits = 0

    for grade in grades:
        score = grade.get("score", 0)
        credits = grade.get("credits", 1)

        if score >= 90:
            grade_point = 4.0
        elif score >= 80:
            grade_point = 3.0
        elif score >= 70:
            grade_point = 2.0
        elif score >= 60:
            grade_point = 1.0
        else:
            grade_point = 0.0

        total_points += grade_point * credits
        total_credits += credits

    if total_credits == 0:
        return 0.0

    return round(total_points / total_credits, 2)


def get_subject_averages(grades):
    """
    Compute average score per subject.

    Args:
        grades (list): List of dicts with 'subject' and 'score' keys.

    Returns:
        dict: Subject name mapped to average score (rounded to 2 decimals).
    """
    subject_totals = {}
    subject_counts = {}

    for grade in grades:
        subject = grade.get("subject", "Unknown")
        score = grade.get("score", 0)

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += score
        subject_counts[subject] += 1

    averages = {}
    for subject in subject_totals:
        averages[subject] = round(subject_totals[subject] / subject_counts[subject], 2)

    return averages


def identify_at_risk(grades, threshold=60):
    """
    Identify subjects where the student's average is below the threshold.

    Args:
        grades (list): List of grade dicts with 'subject' and 'score'.
        threshold (int): Minimum passing average. Default is 60.

    Returns:
        list: Subject names where average score is below threshold.
    """
    averages = get_subject_averages(grades)
    at_risk = [subject for subject, avg in averages.items() if avg < threshold]
    return at_risk


def generate_summary(student_id, grades):
    """
    Generate a full analytics report for a student.

    Args:
        student_id (str): The student's unique identifier.
        grades (list): List of grade records.

    Returns:
        dict: Full analytics report including GPA, averages, and at-risk subjects.
    """
    return {
        "student_id": student_id,
        "total_grades": len(grades),
        "gpa": calculate_gpa(grades),
        "subject_averages": get_subject_averages(grades),
        "at_risk_subjects": identify_at_risk(grades),
    }
