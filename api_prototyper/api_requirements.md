# API Requirements – EduTrack API

## Domain
Academic management platform for students and teachers to manage assignments, grades, attendance, and AI-powered study plans.

## Target Users
- **Students**: access assignments, view grades, and retrieve personalized study plans
- **Teachers**: create assignments, update grades, and manage attendance records
- **Admins**: manage user accounts and generate institutional reports

## Core Operations
- Register a new user (student or teacher)
- Authenticate user and return JWT token
- Create a new assignment
- Get all assignments for a class
- Get assignment by ID
- Submit an assignment (student)
- Update assignment grade (teacher)
- Get all grades for a student
- Mark attendance for a class session
- Get attendance records by student and date range
- Generate AI study plan for a student
- Get student GPA and performance summary
- Delete an assignment

## Data Rules
- Email must be unique and in valid format
- Password must be at least 8 characters with one uppercase and one number
- Assignment due date must be a future date
- Grade must be a number between 0 and 100
- Attendance status must be one of: present, absent, or late
- Student ID and class ID must exist before creating an assignment record
- AI study plan requires at least 3 graded assignments to generate

## Non-Functional
- Response time under 300ms for all endpoints under normal load
- JWT authentication required for all endpoints except register and login
- Rate limit of 100 requests per minute per user
- All data transmitted over HTTPS
- API versioning via URL prefix: /api/v1/
- Passwords must be hashed using bcrypt before storage
