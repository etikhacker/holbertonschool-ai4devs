# Data Model

## Project: AI-Enhanced Team Collaboration Platform

---

## Overview

The data model is designed around five core entities: **User**, **Project**, **Task**, **Comment**, and **Notification**. Relationships are defined to support multi-user collaboration, task management, and AI-generated content tracking.

---

## Entities

### 1. User

Represents a registered member of the platform.

| Field         | Type         | Constraints               | Description                          |
|---------------|--------------|---------------------------|--------------------------------------|
| `id`          | UUID         | PRIMARY KEY                | Unique identifier                    |
| `name`        | VARCHAR(100) | NOT NULL                  | Full display name                    |
| `email`       | VARCHAR(255) | NOT NULL, UNIQUE          | Login email address                  |
| `password_hash` | VARCHAR(255) | NOT NULL               | Bcrypt-hashed password               |
| `avatar_url`  | TEXT         | NULLABLE                  | Profile picture URL                  |
| `role`        | ENUM         | `member`, `lead`, `admin` | Platform-level role                  |
| `created_at`  | TIMESTAMP    | DEFAULT NOW()             | Account creation timestamp           |
| `updated_at`  | TIMESTAMP    | DEFAULT NOW()             | Last profile update                  |

**Relationships:**
- A User can be a **member of many Projects** (via `ProjectMember` join table)
- A User can **own/create many Projects**
- A User can be **assigned many Tasks**
- A User can **author many Comments**

---

### 2. Project

Represents a collaborative workspace grouping related tasks.

| Field         | Type         | Constraints      | Description                            |
|---------------|--------------|------------------|----------------------------------------|
| `id`          | UUID         | PRIMARY KEY       | Unique identifier                      |
| `name`        | VARCHAR(150) | NOT NULL         | Project name                           |
| `description` | TEXT         | NULLABLE         | Project overview                       |
| `owner_id`    | UUID         | FK → User.id     | Creator/owner of the project           |
| `deadline`    | DATE         | NULLABLE         | Target completion date                 |
| `status`      | ENUM         | `active`, `archived`, `completed` | Current project state   |
| `ai_summary`  | TEXT         | NULLABLE         | Latest AI-generated project summary    |
| `ai_summary_at` | TIMESTAMP  | NULLABLE         | Timestamp of last AI summary generation|
| `created_at`  | TIMESTAMP    | DEFAULT NOW()    | Project creation timestamp             |
| `updated_at`  | TIMESTAMP    | DEFAULT NOW()    | Last update timestamp                  |

**Relationships:**
- A Project **belongs to one User** (owner)
- A Project **has many Members** (via `ProjectMember` join table)
- A Project **has many Tasks**

---

### 3. Task

Represents a unit of work within a project.

| Field             | Type         | Constraints                          | Description                            |
|-------------------|--------------|--------------------------------------|----------------------------------------|
| `id`              | UUID         | PRIMARY KEY                           | Unique identifier                      |
| `project_id`      | UUID         | FK → Project.id, NOT NULL            | Parent project                         |
| `assignee_id`     | UUID         | FK → User.id, NULLABLE               | Assigned team member                   |
| `created_by_id`   | UUID         | FK → User.id, NOT NULL               | Task creator                           |
| `title`           | VARCHAR(200) | NOT NULL                             | Short task name                        |
| `description`     | TEXT         | NULLABLE                             | Detailed task description              |
| `ai_description`  | TEXT         | NULLABLE                             | AI-improved version of description     |
| `status`          | ENUM         | `todo`, `in_progress`, `done`        | Current task status                    |
| `priority`        | ENUM         | `low`, `medium`, `high`              | Task priority level                    |
| `due_date`        | DATE         | NULLABLE                             | Task deadline                          |
| `tags`            | TEXT[]       | NULLABLE                             | Skill/category tags for AI planning    |
| `created_at`      | TIMESTAMP    | DEFAULT NOW()                        | Task creation timestamp                |
| `updated_at`      | TIMESTAMP    | DEFAULT NOW()                        | Last modification timestamp            |

**Relationships:**
- A Task **belongs to one Project**
- A Task **is optionally assigned to one User**
- A Task **has many Comments**
- A Task **has many Notifications** (triggered by status changes, assignments)

---

### 4. Comment

Represents a message left by a user on a specific task.

| Field        | Type      | Constraints           | Description                         |
|--------------|-----------|-----------------------|-------------------------------------|
| `id`         | UUID      | PRIMARY KEY            | Unique identifier                   |
| `task_id`    | UUID      | FK → Task.id, NOT NULL | Parent task                         |
| `author_id`  | UUID      | FK → User.id, NOT NULL | Comment author                      |
| `body`       | TEXT      | NOT NULL              | Comment text content                |
| `mentions`   | UUID[]    | NULLABLE              | Array of mentioned User IDs         |
| `created_at` | TIMESTAMP | DEFAULT NOW()         | Comment creation timestamp          |
| `updated_at` | TIMESTAMP | DEFAULT NOW()         | Last edit timestamp                 |

**Relationships:**
- A Comment **belongs to one Task**
- A Comment **belongs to one User** (author)
- A Comment **can mention many Users**

---

### 5. Notification

Represents an in-app alert generated by system or user events.

| Field         | Type      | Constraints              | Description                              |
|---------------|-----------|--------------------------|------------------------------------------|
| `id`          | UUID      | PRIMARY KEY               | Unique identifier                        |
| `user_id`     | UUID      | FK → User.id, NOT NULL   | Recipient of the notification            |
| `type`        | ENUM      | `assignment`, `mention`, `status_change`, `invite` | Event type |
| `entity_type` | ENUM      | `task`, `project`, `comment` | What the notification refers to      |
| `entity_id`   | UUID      | NOT NULL                 | ID of the referenced entity              |
| `message`     | TEXT      | NOT NULL                 | Human-readable notification text         |
| `is_read`     | BOOLEAN   | DEFAULT FALSE            | Whether user has seen the notification   |
| `created_at`  | TIMESTAMP | DEFAULT NOW()            | When notification was created            |

**Relationships:**
- A Notification **belongs to one User** (recipient)
- A Notification **references one entity** (Task, Project, or Comment)

---

## Join Tables

### ProjectMember

Links Users to Projects with a role.

| Field        | Type      | Constraints                        | Description               |
|--------------|-----------|------------------------------------|---------------------------|
| `project_id` | UUID      | FK → Project.id, NOT NULL         | The project               |
| `user_id`    | UUID      | FK → User.id, NOT NULL            | The member                |
| `role`       | ENUM      | `viewer`, `contributor`, `lead`   | Role within the project   |
| `joined_at`  | TIMESTAMP | DEFAULT NOW()                     | When user joined           |

**Primary Key:** (`project_id`, `user_id`)

---

## Entity Relationship Diagram (Text)

```
User ──< ProjectMember >── Project
User ──< Task (assignee)
User ──< Task (created_by)
User ──< Comment
User ──< Notification

Project ──< Task
Task ──< Comment
Task ──< Notification (entity)
```

---

## Notes

- All primary keys use **UUID v4** to support distributed generation without collision.
- `ai_description` and `ai_summary` fields store AI-generated content alongside original user content, keeping both versions accessible.
- `tags` on Task is a text array to support AI sprint planning by skill matching without a separate join table.
- Soft deletes (an `is_deleted` flag) may be added in a future iteration to preserve audit history.