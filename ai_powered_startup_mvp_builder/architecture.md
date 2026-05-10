# System Architecture
## AI-Powered Job Application Assistant MVP

## Overview
This document describes the high-level architecture of the AI-Powered Job Application Assistant. The system follows a three-tier architecture: a React frontend, a Node.js REST API backend, and a PostgreSQL database. An external AI service (OpenAI API) is integrated to power resume analysis, cover letter generation, and interview preparation features.

---

## System Diagram

```
┌─────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                        │
│                                                         │
│        ┌────────────────────────────────────┐          │
│        │     Web App (React / Tailwind CSS) │          │
│        │  Dashboard │ Resume │ Cover Letter │          │
│        └──────────────────┬─────────────────┘          │
└─────────────────────────────────────────────────────────┘
                            │ HTTPS / REST
                            ▼
┌─────────────────────────────────────────────────────────┐
│                       API LAYER                          │
│                                                         │
│        ┌────────────────────────────────────┐          │
│        │     REST API (Node.js / Express)   │          │
│        │                                    │          │
│        │  ┌──────────┐  ┌────────────────┐ │          │
│        │  │   Auth   │  │ Resume Module  │ │          │
│        │  │  Module  │  │ (upload/parse) │ │          │
│        │  └──────────┘  └────────────────┘ │          │
│        │                                    │          │
│        │  ┌──────────┐  ┌────────────────┐ │          │
│        │  │  Cover   │  │  Application   │ │          │
│        │  │  Letter  │  │    Tracker     │ │          │
│        │  │  Module  │  │    Module      │ │          │
│        │  └──────────┘  └────────────────┘ │          │
│        └───────────────────┬────────────────┘          │
└────────────────────────────┼────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
┌─────────────────────┐       ┌─────────────────────────┐
│    DATA LAYER        │       │     AI SERVICE LAYER    │
│                      │       │                         │
│  PostgreSQL Database │       │   OpenAI API (GPT-4)   │
│  ┌────────────────┐ │       │  - Resume analysis      │
│  │ Users          │ │       │  - Cover letter gen     │
│  │ Resumes        │ │       │  - Match scoring        │
│  │ Applications   │ │       │  - Interview tips       │
│  │ CoverLetters   │ │       └─────────────────────────┘
│  └────────────────┘ │
└──────────────────────┘
```

---

## Component Descriptions

### Client Layer
- **Web App (React)**: Single-page application where users manage resumes, generate cover letters, track applications, and view AI suggestions.

### API Layer
- **Auth Module**: Handles registration, login, and JWT-based session management.
- **Resume Module**: Accepts resume file uploads, extracts text, and sends content to the AI service for analysis.
- **Cover Letter Module**: Accepts a job description and resume content, sends both to the AI service, and returns a tailored cover letter.
- **Application Tracker Module**: Manages CRUD operations for saved job applications and their statuses.

### Data Layer
- **PostgreSQL**: Stores all user data, uploaded resumes, generated cover letters, and application tracking records.

### AI Service Layer
- **OpenAI API (GPT-4)**: Powers all AI features including resume improvement suggestions, cover letter generation, job match scoring, and interview preparation tips.

---

## Key Design Decisions

| Decision | Choice | Reason |
|---|---|---|
| AI Provider | OpenAI GPT-4 | Best-in-class language understanding for resume and job description analysis |
| API Style | REST | Simple, well-understood, easy to test and extend |
| Authentication | JWT | Stateless and scalable |
| Database | PostgreSQL | Relational integrity for user-resume-application relationships |
| Frontend | React | Fast, component-based UI suitable for a dashboard-heavy app |