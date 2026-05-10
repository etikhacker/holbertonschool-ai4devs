# Data Model

## Overview
The data model consists of 5 entities: **User**, **Class**, **Assignment**, **Grade**, and **Attendance**. All entities are stored in a relational PostgreSQL database. Relationships are enforced through foreign keys to maintain data integrity.

---

## Entity 1 – User

Represents all registered users of the platform, including students, teachers, and admins.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each user |
| `name` | VARCHAR(100) | NOT NULL | Full name of the user |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE | Email address used for login |
| `password_hash` | VARCHAR(255) | NOT NULL | Bcrypt-hashed password |
| `role` | ENUM | NOT NULL | One of: `student`, `teacher`, `admin` |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp of account creation |
| `is_active` | BOOLEAN | DEFAULT TRUE | Whether the account is active |

**Relationships:**
- A User with role `teacher` can create many Classes.
- A User with role `student` can enroll in many Classes.
- A User with role `student` receives many Grades.
- A User with role `student` has many Attendance records.

---

## Entity 2 – Class

Represents a course or group created by a teacher and attended by students.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each class |
| `name` | VARCHAR(150) | NOT NULL | Name of the class (e.g., "Math 101") |
| `description` | TEXT | NULLABLE | Optional description of the class content |
| `teacher_id` | UUID | FOREIGN KEY → User.id | The teacher who owns this class |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp of class creation |

**Relationships:**
- A Class belongs to one User (teacher).
- A Class has many Assignments.
- A Class has many Attendance records.
- A Class has many enrolled Users (students) via a join table `class_enrollments`.

---

## Entity 3 – Assignment

Represents a task or piece of work assigned to students within a class.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each assignment |
| `class_id` | UUID | FOREIGN KEY → Class.id | The class this assignment belongs to |
| `title` | VARCHAR(200) | NOT NULL | Title of the assignment |
| `description` | TEXT | NULLABLE | Detailed instructions for the assignment |
| `due_date` | DATE | NOT NULL | The deadline for submission |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp when the assignment was created |

**Relationships:**
- An Assignment belongs to one Class.
- An Assignment has many Grades (one per enrolled student).

---

## Entity 4 – Grade

Represents the score given to a student for a specific assignment.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each grade record |
| `assignment_id` | UUID | FOREIGN KEY → Assignment.id | The assignment being graded |
| `student_id` | UUID | FOREIGN KEY → User.id | The student receiving the grade |
| `score` | DECIMAL(5,2) | NOT NULL | Numeric score (e.g., 85.50) |
| `feedback` | TEXT | NULLABLE | Optional written feedback from the teacher |
| `graded_at` | TIMESTAMP | NOT NULL | Timestamp when the grade was recorded |

**Constraints:**
- The combination of `assignment_id` and `student_id` must be unique (one grade per student per assignment).

**Relationships:**
- A Grade belongs to one Assignment.
- A Grade belongs to one User (student).

---

## Entity 5 – Attendance

Represents the attendance status of a student for a specific class session.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each attendance record |
| `class_id` | UUID | FOREIGN KEY → Class.id | The class session being recorded |
| `student_id` | UUID | FOREIGN KEY → User.id | The student whose attendance is recorded |
| `session_date` | DATE | NOT NULL | The date of the class session |
| `status` | ENUM | NOT NULL | One of: `present`, `absent`, `late` |
| `recorded_at` | TIMESTAMP | NOT NULL | Timestamp when the record was created |

**Constraints:**
- The combination of `class_id`, `student_id`, and `session_date` must be unique (one attendance record per student per session).

**Relationships:**
- An Attendance record belongs to one Class.
- An Attendance record belongs to one User (student).

---

## Entity Relationship Summary

```
User (teacher) ──< Class ──< Assignment ──< Grade >── User (student)
                      │
                      └──< Attendance >── User (student)

User (student) ──< class_enrollments >── Class
```