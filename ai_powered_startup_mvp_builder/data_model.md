# Data Model
## AI-Powered Job Application Assistant MVP

## Overview
The data model consists of 4 entities: **User**, **Resume**, **Application**, and **CoverLetter**. All entities are stored in a PostgreSQL relational database with foreign key constraints to ensure data integrity.

---

## Entity 1 – User

Represents a registered job seeker using the platform.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each user |
| `name` | VARCHAR(100) | NOT NULL | Full name of the user |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE | Email address used for login |
| `password_hash` | VARCHAR(255) | NOT NULL | Bcrypt-hashed password |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp of account creation |
| `is_active` | BOOLEAN | DEFAULT TRUE | Whether the account is active |

**Relationships:**
- A User can have many Resumes.
- A User can have many Applications.
- A User can have many CoverLetters.

---

## Entity 2 – Resume

Represents an uploaded and parsed resume belonging to a user.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each resume |
| `user_id` | UUID | FOREIGN KEY → User.id | The user who owns this resume |
| `file_name` | VARCHAR(255) | NOT NULL | Original file name of the uploaded resume |
| `content_text` | TEXT | NOT NULL | Extracted plain text content of the resume |
| `ai_feedback` | TEXT | NULLABLE | AI-generated suggestions to improve the resume |
| `uploaded_at` | TIMESTAMP | NOT NULL | Timestamp when the resume was uploaded |

**Relationships:**
- A Resume belongs to one User.
- A Resume can be linked to many Applications.
- A Resume can be linked to many CoverLetters.

---

## Entity 3 – Application

Represents a job application submitted or tracked by a user.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each application |
| `user_id` | UUID | FOREIGN KEY → User.id | The user tracking this application |
| `resume_id` | UUID | FOREIGN KEY → Resume.id | The resume used for this application |
| `company_name` | VARCHAR(200) | NOT NULL | Name of the company being applied to |
| `job_title` | VARCHAR(200) | NOT NULL | Title of the position being applied for |
| `job_description` | TEXT | NULLABLE | Full job description text pasted by the user |
| `match_score` | DECIMAL(5,2) | NULLABLE | AI-generated match score between resume and job |
| `status` | ENUM | NOT NULL | One of: `saved`, `applied`, `interview`, `offer`, `rejected` |
| `applied_at` | DATE | NULLABLE | Date the application was submitted |
| `created_at` | TIMESTAMP | NOT NULL | Timestamp when the record was created |

**Relationships:**
- An Application belongs to one User.
- An Application belongs to one Resume.
- An Application can have one CoverLetter.

---

## Entity 4 – CoverLetter

Represents an AI-generated cover letter created for a specific job application.

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | UUID | PRIMARY KEY | Unique identifier for each cover letter |
| `user_id` | UUID | FOREIGN KEY → User.id | The user who owns this cover letter |
| `application_id` | UUID | FOREIGN KEY → Application.id, NULLABLE | The application this cover letter was generated for |
| `resume_id` | UUID | FOREIGN KEY → Resume.id | The resume used as input for generation |
| `content` | TEXT | NOT NULL | The full AI-generated cover letter text |
| `job_description_input` | TEXT | NOT NULL | The job description used as input for the AI |
| `generated_at` | TIMESTAMP | NOT NULL | Timestamp when the cover letter was generated |

**Relationships:**
- A CoverLetter belongs to one User.
- A CoverLetter belongs to one Resume.
- A CoverLetter optionally belongs to one Application.

---

## Entity Relationship Summary

```
User ──< Resume ──< CoverLetter
  │          │
  │          └──< Application ──< CoverLetter
  │
  └──< Application
```