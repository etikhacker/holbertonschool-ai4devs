# Architecture Plan

## Project: AI-Enhanced Team Collaboration Platform

---

## 1. Overview

This document describes the high-level architecture for an AI-Enhanced Team Collaboration Platform — a web application that enables teams to manage projects and tasks, communicate in context, and leverage AI-powered features such as task description improvement, project summarization, and sprint planning recommendations.

The system follows a **client-server architecture** with a decoupled frontend, a RESTful backend API, a relational database, and integration with an external AI provider (Anthropic Claude API).

---

## 2. Architecture Style

**Pattern:** Monolithic Backend with Service Separation (modular monolith)

This approach is chosen for hackathon-scale development speed while keeping the codebase organized enough to extract microservices later if needed.

- **Frontend:** Single Page Application (SPA)
- **Backend:** REST API server (Node.js / Express)
- **AI Layer:** Dedicated service module within the backend that interfaces with the Anthropic Claude API
- **Database:** PostgreSQL (relational)
- **Real-time:** WebSockets for live notifications
- **Auth:** JWT-based stateless authentication

---

## 3. High-Level Component Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                         │
│                                                             │
│   ┌──────────────────────────────────────────────────┐      │
│   │         React SPA (Vite + TailwindCSS)           │      │
│   │  - Dashboard / Projects / Tasks / Notifications  │      │
│   │  - AI-powered UI components (summaries, hints)   │      │
│   └────────────────────┬─────────────────────────────┘      │
└────────────────────────┼────────────────────────────────────┘
                         │ HTTPS / WebSocket
┌────────────────────────▼────────────────────────────────────┐
│                       API LAYER                             │
│                                                             │
│   ┌──────────────────────────────────────────────────┐      │
│   │          Node.js / Express REST API              │      │
│   │                                                  │      │
│   │  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │      │
│   │  │  Auth    │  │ Projects │  │     Tasks      │  │      │
│   │  │ Module   │  │ Module   │  │    Module      │  │      │
│   │  └──────────┘  └──────────┘  └───────────────┘  │      │
│   │  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │      │
│   │  │Comments  │  │Notif.    │  │   AI Service  │  │      │
│   │  │ Module   │  │ Module   │  │    Module     │  │      │
│   │  └──────────┘  └──────────┘  └──────┬────────┘  │      │
│   └─────────────────────────────────────┼────────────┘      │
└─────────────────────────────────────────┼────────────────────┘
                                          │ HTTPS
                              ┌───────────▼──────────┐
                              │  Anthropic Claude API │
                              │  (claude-sonnet-4)    │
                              └──────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                      DATA LAYER                             │
│                                                             │
│   ┌──────────────────────────────────────────────────┐      │
│   │              PostgreSQL Database                 │      │
│   │  Users | Projects | Tasks | Comments | Notifs   │      │
│   └──────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Frontend Architecture

**Technology:** React 18 + Vite + TailwindCSS

### Structure
```
src/
├── components/         # Reusable UI components (Button, Card, Modal)
├── pages/              # Route-level page components
│   ├── Dashboard.jsx
│   ├── ProjectView.jsx
│   ├── TaskView.jsx
│   └── Login.jsx
├── features/           # Feature slices (auth, projects, tasks, ai)
├── hooks/              # Custom React hooks
├── services/           # API client functions (axios)
├── store/              # Global state (Zustand or React Context)
└── utils/              # Helpers and formatters
```

### Key Design Decisions
- **Routing:** React Router v6 with protected routes for authenticated users
- **State Management:** Zustand for lightweight global state (user session, notifications)
- **API Communication:** Axios with interceptors for JWT token injection and error handling
- **Real-time:** WebSocket client (native or Socket.IO) for live notification updates
- **AI UX:** AI features are non-blocking; results render asynchronously with loading states

---

## 5. Backend Architecture

**Technology:** Node.js + Express.js

### Structure
```
src/
├── routes/             # Express route definitions
│   ├── auth.js
│   ├── projects.js
│   ├── tasks.js
│   ├── comments.js
│   └── notifications.js
├── controllers/        # Request handlers (thin layer)
├── services/           # Business logic
│   ├── authService.js
│   ├── projectService.js
│   ├── taskService.js
│   └── aiService.js    # AI integration logic
├── models/             # Database query functions (no ORM or Sequelize)
├── middleware/         # Auth guard, error handler, rate limiter
├── websocket/          # WebSocket server and event handlers
└── config/             # Environment config, DB pool, constants
```

### API Design (REST)

| Method | Endpoint                          | Description                        |
|--------|-----------------------------------|------------------------------------|
| POST   | `/api/auth/register`              | Register new user                  |
| POST   | `/api/auth/login`                 | Log in, receive JWT                |
| GET    | `/api/projects`                   | List user's projects               |
| POST   | `/api/projects`                   | Create a project                   |
| GET    | `/api/projects/:id`               | Get project details                |
| POST   | `/api/projects/:id/tasks`         | Create a task in a project         |
| PATCH  | `/api/tasks/:id`                  | Update task (status, assignee...)  |
| POST   | `/api/tasks/:id/comments`         | Add a comment                      |
| GET    | `/api/notifications`              | Get user notifications             |
| PATCH  | `/api/notifications/read`         | Mark notifications as read         |
| POST   | `/api/ai/summarize/:projectId`    | Generate AI project summary        |
| POST   | `/api/ai/improve-task/:taskId`    | AI-improve a task description      |
| POST   | `/api/ai/sprint-plan/:projectId`  | AI sprint planning suggestion      |

---

## 6. AI Service Module

The AI Service is a dedicated module inside the backend that encapsulates all calls to the Anthropic Claude API.

### Responsibilities
- **Task Description Improvement:** Sends the raw task description and returns a polished, structured version with suggested acceptance criteria
- **Project Summary Generation:** Aggregates task data (titles, statuses, assignees) and generates a narrative summary
- **Sprint Planning Recommendations:** Analyzes team workload and task metadata to suggest task-to-member assignments

### Design
- All Claude API calls go through a single `claudeClient.js` wrapper for centralized error handling and token logging
- Prompts are stored as versioned templates in `src/ai/prompts/` for easy iteration
- AI responses are validated before being saved to the database
- Rate limiting is applied per user on AI endpoints (max 10 AI requests/hour)

```
aiService.js
├── improveTaskDescription(taskId)   → calls Claude → returns improved text
├── generateProjectSummary(projectId) → aggregates tasks → calls Claude → saves + returns summary
└── sprintPlanningAdvice(projectId, sprintParams) → analyzes members + tasks → calls Claude → returns plan
```

---

## 7. Database

**Technology:** PostgreSQL 15

- **Connection Pooling:** `pg` (node-postgres) with a pool of 10 connections
- **Migrations:** Raw SQL migration files managed with `node-pg-migrate`
- **No ORM:** Direct parameterized queries to keep full control and performance transparency
- **Indexing Strategy:**
  - `tasks.project_id` — supports project board queries
  - `tasks.assignee_id` — supports "my tasks" views
  - `notifications.user_id + is_read` — supports unread notification queries
  - `comments.task_id` — supports comment thread loading

---

## 8. Authentication & Security

- **Auth Method:** JWT (JSON Web Tokens) with 7-day expiry, stored in `httpOnly` cookies
- **Password Hashing:** bcrypt with salt rounds = 12
- **Input Validation:** `express-validator` on all incoming request bodies
- **Rate Limiting:** `express-rate-limit` — global 100 req/min per IP; AI endpoints 10 req/hour per user
- **CORS:** Restricted to the frontend origin domain
- **Environment Variables:** All secrets (DB credentials, Claude API key, JWT secret) stored in `.env`, never committed

---

## 9. Real-Time Notifications

- **Technology:** Socket.IO (WebSocket with fallback)
- **Pattern:** Server emits events to user-specific rooms (e.g., `room:user_{id}`)
- **Events:**
  - `notification:new` — triggers bell badge update
  - `task:updated` — triggers board refresh for project members
- **Scalability Note:** For multi-instance deployment, a Redis pub/sub adapter can be added to Socket.IO

---

## 10. Deployment & Environment

### Environments
| Environment | Purpose                   |
|-------------|---------------------------|
| Development | Local development (`localhost`) |
| Production  | Deployed app              |

### Infrastructure (MVP)
- **Frontend:** Hosted on **Vercel** (static SPA, auto-deploy from GitHub)
- **Backend:** Hosted on **Render** or **Railway** (Node.js web service)
- **Database:** **Supabase** (managed PostgreSQL) or Railway PostgreSQL

### Environment Variables
```
DATABASE_URL=
JWT_SECRET=
ANTHROPIC_API_KEY=
CLIENT_ORIGIN=
PORT=
```

---

## 11. Development Workflow

- **Repository:** `holbertonschool-ai4devs` → directory `ai_enhanced_team_hackathon`
- **Branching:** `main` (stable) → feature branches → PRs with review
- **Linting:** ESLint + Prettier on both frontend and backend
- **API Testing:** Thunder Client or Postman collections committed to repo

---

## 12. Technology Stack Summary

| Layer         | Technology                        |
|---------------|-----------------------------------|
| Frontend      | React 18, Vite, TailwindCSS       |
| Backend       | Node.js, Express.js               |
| Database      | PostgreSQL 15                     |
| AI Provider   | Anthropic Claude API (Sonnet)     |
| Auth          | JWT + bcrypt                      |
| Real-Time     | Socket.IO                         |
| Hosting (FE)  | Vercel                            |
| Hosting (BE)  | Render / Railway                  |
| DB Hosting    | Supabase / Railway PostgreSQL     |