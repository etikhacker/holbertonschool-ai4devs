# Data Model – EduTrack MVP

## Entity: User
Represents both students and teachers. Role determines access level.

| Field | Type | Constraints |
|-------|------|-------------|
| id | UUID | Primary Key |
| name | VARCHAR(100) | NOT NULL |
| email | VARCHAR(255) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(255) | NOT NULL |
| role | ENUM('student', 'teacher') | NOT NULL |
| language | VARCHAR(10) | DEFAULT 'en' |
| created_at | TIMESTAMP | DEFAULT NOW() |

---

## Entity: Class
Represents a class group managed by a teacher and attended by students.

| Field | Type | Constraints |
|-------|------|-------------|
| id | UUID | Primary Key |
| name | VARCHAR(100) | NOT NULL |
| subject | VARCHAR(100) | NOT NULL |
| teacher_id | UUID | Foreign Key → User.id |
| created_at | TIMESTAMP | DEFAULT NOW() |

---

## Entity: Assignment
Represents an assignment created by a teacher for a class.

| Field | Type | Constraints |
|-------|------|-------------|
| id | UUID | Primary Key |
| title | VARCHAR(200) | NOT NULL |
| description | TEXT | NULLABLE |
| due_date | TIMESTAMP | NOT NULL |
| priority | ENUM('urgent', 'normal', 'low') | DEFAULT 'normal' |
| class_id | UUID | Foreign Key → Class.id |
| created_by | UUID | Foreign Key → User.id |
| created_at | TIMESTAMP | DEFAULT NOW() |

---

## Entity: Grade
Represents a grade given to a student for a specific assignment.

| Field | Type | Constraints |
|-------|------|-------------|
| id | UUID | Primary Key |
| student_id | UUID | Foreign Key → User.id |
| assignment_id | UUID | Foreign Key → Assignment.id |
| score | DECIMAL(5,2) | CHECK (score >= 0 AND score <= 100) |
| feedback | TEXT | NULLABLE |
| graded_at | TIMESTAMP | DEFAULT NOW() |

---

## Entity: Attendance
Represents the attendance record of a student for a class session.

| Field | Type | Constraints |
|-------|------|-------------|
| id | UUID | Primary Key |
| student_id | UUID | Foreign Key → User.id |
| class_id | UUID | Foreign Key → Class.id |
| date | DATE | NOT NULL |
| status | ENUM('present', 'absent', 'late') | NOT NULL |
| recorded_at | TIMESTAMP | DEFAULT NOW() |

---

## Relationships
- One **User (teacher)** has many **Classes**
- One **Class** has many **Assignments**
- One **Class** has many **Users (students)** via enrollment (join table)
- One **Assignment** has many **Grades**
- One **User (student)** has many **Grades**
- One **User (student)** has many **Attendance** records
