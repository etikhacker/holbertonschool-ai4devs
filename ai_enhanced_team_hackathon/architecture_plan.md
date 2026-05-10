# Architecture Plan
## AI Study Plan Generator

## Overview
The AI Study Plan Generator follows a three-tier architecture: a React frontend, a Node.js REST API backend, and a PostgreSQL database. An external AI service (OpenAI API) is integrated to generate personalized study schedules and subject-specific study tips.

---

## System Diagram

```
┌──────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                         │
│                                                          │
│       ┌──────────────────────────────────────────┐      │
│       │         Web App (React / Tailwind)        │      │
│       │  Dashboard │ Plan Generator │ Progress    │      │
│       └─────────────────────┬────────────────────┘      │
└─────────────────────────────────────────────────────────-┘
                              │ HTTPS / REST
                              ▼
┌──────────────────────────────────────────────────────────┐
│                       API LAYER                           │
│                                                          │
│       ┌──────────────────────────────────────────┐      │
│       │       REST API (Node.js / Express)        │      │
│       │                                           │      │
│       │  ┌───────────┐  ┌──────────────────────┐ │      │
│       │  │   Auth    │  │  Study Plan Module   │ │      │
│       │  │  Module   │  │  (generate / CRUD)   │ │      │
│       │  └───────────┘  └──────────────────────┘ │      │
│       │                                           │      │
│       │  ┌───────────┐  ┌──────────────────────┐ │      │
│       │  │  Progress │  │    AI Integration    │ │      │
│       │  │  Module   │  │       Module         │ │      │
│       │  └───────────┘  └──────────────────────┘ │      │
│       └──────────────────────┬────────────────────┘      │
└─────────────────────────────────────────────────────────-┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
┌──────────────────────┐         ┌─────────────────────────┐
│      DATA LAYER       │         │     AI SERVICE LAYER    │
│                       │         │                         │
│  PostgreSQL Database  │         │   OpenAI API (GPT-4o)  │
│  ┌─────────────────┐ │         │  - Study plan generation│
│  │ Users           │ │         │  - Subject study tips   │
│  │ StudyPlans      │ │         │  - Schedule optimization│
│  │ Subjects        │ │         └─────────────────────────┘
│  │ Topics          │ │
│  └─────────────────┘ │
└───────────────────────┘
```

---

## Component Descriptions

### Client Layer
- **Web App (React)**: Single-page application where students input their subjects, exam dates, and available hours, then view and interact with their AI-generated study plan.

### API Layer
- **Auth Module**: Handles user registration, login, logout, and JWT token validation.
- **Study Plan Module**: Manages creation, retrieval, update, and deletion of study plans, subjects, and topics.
- **Progress Module**: Handles marking topics as completed and retrieving progress statistics per plan.
- **AI Integration Module**: Sends student inputs (subjects, dates, hours) to the OpenAI API and parses the structured response into study plan data.

### Data Layer
- **PostgreSQL**: Stores all persistent data including user accounts, study plans, subjects, and individual topics with their completion status.

### AI Service Layer
- **OpenAI API (GPT-4o)**: Receives subject names, exam dates, priority levels, and available hours. Returns a structured day-by-day study schedule and subject-specific study tips.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Log in and receive JWT token |
| GET | `/plans` | Get all study plans for the logged-in user |
| POST | `/plans` | Create a new study plan (triggers AI generation) |
| GET | `/plans/:id` | Get a specific study plan with subjects and topics |
| DELETE | `/plans/:id` | Delete a study plan |
| PATCH | `/topics/:id/complete` | Mark a topic as completed |
| POST | `/plans/:id/regenerate` | Regenerate the plan with updated inputs |

---

## Key Design Decisions

| Decision | Choice | Reason |
|---|---|---|
| AI Provider | OpenAI GPT-4o | Best quality for structured schedule generation |
| API Style | REST | Simple, well-understood, easy to test |
| Authentication | JWT | Stateless and scalable |
| Database | PostgreSQL | Relational structure suits hierarchical plan data |
| Frontend | React + Tailwind | Fast UI development with responsive design |
| Hosting | Railway / Render | Free tiers suitable for MVP deployment |
