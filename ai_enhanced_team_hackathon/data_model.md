# Data Model
## AI Study Plan Generator

## Overview
The data model consists of 4 entities: **User**, **StudyPlan**, **Subject**, and **Topic**. All entities are stored in a PostgreSQL relational database with foreign key constraints to ensure data integrity.

---

## Entity 1 – User

Represents a registered student using the platform.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each user |
| `name` | VARCHAR(100) | NOT NULL | Full name of the student |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE | Email address used for login |
| `password_hash` | VARCHAR(255) | NOT NULL | Bcrypt-hashed password |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp of account creation |
| `is_active` | BOOLEAN | DEFAULT TRUE | Whether the account is active |

**Relationships:**
- A User can have many StudyPlans.

---

## Entity 2 – StudyPlan

Represents an AI-generated study schedule created for a student.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each study plan |
| `user_id` | UUID | FOREIGN KEY → User.id | The student who owns this plan |
| `title` | VARCHAR(200) | NOT NULL | Name of the study plan (e.g., "Final Exams 2025") |
| `daily_hours` | DECIMAL(4,1) | NOT NULL | Number of study hours available per day |
| `start_date` | DATE | NOT NULL | Start date of the study plan |
| `end_date` | DATE | NOT NULL | End date of the study plan |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp when the plan was generated |

**Relationships:**
- A StudyPlan belongs to one User.
- A StudyPlan has many Subjects.

---

## Entity 3 – Subject

Represents a course or subject included in a study plan.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each subject |
| `study_plan_id` | UUID | FOREIGN KEY → StudyPlan.id | The study plan this subject belongs to |
| `name` | VARCHAR(150) | NOT NULL | Name of the subject (e.g., "Mathematics") |
| `exam_date` | DATE | NOT NULL | Date of the exam for this subject |
| `priority` | ENUM | NOT NULL | One of: `low`, `medium`, `high` |
| `ai_tips` | TEXT | NULLABLE | AI-generated study tips for this subject |

**Relationships:**
- A Subject belongs to one StudyPlan.
- A Subject has many Topics.

---

## Entity 4 – Topic

Represents an individual study topic within a subject, assigned to a specific day.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each topic |
| `subject_id` | UUID | FOREIGN KEY → Subject.id | The subject this topic belongs to |
| `title` | VARCHAR(200) | NOT NULL | Title of the study topic |
| `scheduled_date` | DATE | NOT NULL | The day this topic is scheduled to be studied |
| `duration_minutes` | INTEGER | NOT NULL | Estimated time to complete this topic in minutes |
| `is_completed` | BOOLEAN | DEFAULT FALSE | Whether the student has marked this topic as done |
| `completed_at` | TIMESTAMP | NULLABLE | Timestamp when the topic was marked as completed |

**Relationships:**
- A Topic belongs to one Subject.

---

## Entity Relationship Summary

```
User ──< StudyPlan ──< Subject ──< Topic
```
