# System Architecture – EduTrack MVP

## Overview
EduTrack uses a client-server architecture with a React frontend, a Node.js/Express REST API backend, a PostgreSQL database, and an external AI service for study plan generation.

## High-Level Diagram

```
┌─────────────────────────────────────────────────────┐
│                    CLIENT LAYER                     │
│         React Web App (mobile-responsive)           │
│   Student Dashboard │ Teacher Dashboard │ Settings  │
└────────────────────────┬────────────────────────────┘
                         │ HTTPS / REST API
┌────────────────────────▼────────────────────────────┐
│                   API LAYER                         │
│            Node.js + Express REST API               │
│  /auth  │ /assignments │ /grades │ /attendance      │
│         │ /students    │ /classes│ /study-plan      │
└──────┬──────────────────────┬───────────────────────┘
       │ SQL queries          │ HTTP POST
┌──────▼──────┐      ┌────────▼────────┐
│  PostgreSQL │      │  OpenAI / AI    │
│  Database   │      │  Study Plan API │
│             │      │                 │
│ Users       │      │ Analyzes grades │
│ Assignments │      │ Returns weekly  │
│ Grades      │      │ study plan JSON │
│ Attendance  │      └─────────────────┘
│ Classes     │
└─────────────┘
```

## Components

### Frontend (React)
- Student dashboard with assignment list, grade chart, and GPA display
- Teacher dashboard with class roster, attendance tracker, and grade entry
- Settings screen for language and theme preferences
- Communicates with backend via REST API using JWT tokens

### Backend (Node.js + Express)
- RESTful API with versioned endpoints under `/api/v1/`
- JWT-based authentication middleware for all protected routes
- Business logic for GPA calculation, attendance summaries, and report generation
- Proxies AI study plan requests to the external AI service

### Database (PostgreSQL)
- Stores all users, assignments, grades, attendance records, and class data
- Row-level security enforced at the application layer
- Indexed on student_id, class_id, and due_date for query performance

### AI Service (External)
- Receives student grade data and returns a structured weekly study plan
- Called only when a student has at least 3 graded assignments
- Response cached for 24 hours to minimize API costs
