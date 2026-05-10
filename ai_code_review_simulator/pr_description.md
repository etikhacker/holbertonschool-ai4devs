# Pull Request: Add Student Grade Analytics Feature

## Summary
Implements a grade analytics module for the EduTrack platform. Adds functions to calculate GPA, identify at-risk students, and generate subject-level performance summaries. Includes a new API endpoint `/students/{id}/analytics` and full unit test coverage.

## Changes
- Added `grade_analytics.py` with the following functions:
  - `calculate_gpa(grades)` — computes weighted GPA from a list of grade records
  - `get_subject_averages(grades)` — returns average score per subject
  - `identify_at_risk(grades, threshold=60)` — flags subjects where average is below threshold
  - `generate_summary(student_id, grades)` — returns a full analytics report dict
- Added `test_grade_analytics.py` with 8 unit tests covering all functions and edge cases
- Updated `api_routes.py` to expose the new `/students/{id}/analytics` GET endpoint
- Updated `README.md` with endpoint documentation

## Context
Approximately 160 LOC across implementation and tests. Related to issue #17 (Student performance tracking).

The motivation for this feature is to give teachers a single endpoint to retrieve structured analytics for any student, replacing the manual process of fetching grades and computing averages client-side. The `identify_at_risk` function enables the dashboard to automatically flag struggling students without additional frontend logic.

## Test Results
All 8 new unit tests pass. All 12 existing tests continue to pass. No regressions.
