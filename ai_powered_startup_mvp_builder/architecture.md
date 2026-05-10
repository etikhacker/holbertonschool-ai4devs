# System Architecture

## Overview
This document describes the high-level architecture of the AI-Powered Student Management MVP. The system follows a three-tier client-server architecture consisting of a frontend client, a backend REST API, and a relational database.

---

## System Diagram

```
┌─────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                      │
│                                                         │
│   ┌─────────────────┐        ┌──────────────────────┐  │
│   │   Web Browser   │        │    Mobile Browser    │  │
│   │  (React / HTML) │        │   (Responsive UI)    │  │
│   └────────┬────────┘        └──────────┬───────────┘  │
│            │                            │               │
└────────────┼────────────────────────────┼───────────────┘
             │         HTTPS              │
             ▼                            ▼
┌─────────────────────────────────────────────────────────┐
│                      API LAYER                           │
│                                                         │
│   ┌─────────────────────────────────────────────────┐  │
│   │              REST API (Node.js / Express)        │  │
│   │                                                  │  │
│   │  ┌───────────┐  ┌───────────┐  ┌─────────────┐ │  │
│   │  │   Auth    │  │  Classes  │  │ Assignments │ │  │
│   │  │  Module   │  │  Module   │  │   Module    │ │  │
│   │  └───────────┘  └───────────┘  └─────────────┘ │  │
│   │                                                  │  │
│   │  ┌───────────┐  ┌───────────┐                   │  │
│   │  │  Grades   │  │Attendance │                   │  │
│   │  │  Module   │  │  Module   │                   │  │
│   │  └───────────┘  └───────────┘                   │  │
│   └─────────────────────────────────────────────────┘  │
│                                                         │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│                     DATA LAYER                           │
│                                                         │
│   ┌──────────────────────────────────────────────────┐ │
│   │           Relational Database (PostgreSQL)        │ │
│   │                                                   │ │
│   │   Users │ Classes │ Assignments │ Grades │        │ │
│   │                          Attendance               │ │
│   └──────────────────────────────────────────────────┘ │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Component Descriptions

### Client Layer
- **Web Browser**: The primary user interface built with React. Students, teachers, and admins interact with the system through this interface.
- **Mobile Browser**: A responsive version of the web UI accessible from mobile devices without requiring a native app.

### API Layer
- **REST API (Node.js / Express)**: Handles all business logic and serves data to the client. Organized into modules by feature area.
- **Auth Module**: Manages user registration, login, logout, and JWT token validation.
- **Classes Module**: Handles creation, retrieval, update, and deletion of classes.
- **Assignments Module**: Manages assignment creation, listing, and deadline tracking per class.
- **Grades Module**: Records and retrieves grades per student per assignment.
- **Attendance Module**: Records and retrieves attendance status per student per class session.

### Data Layer
- **PostgreSQL Database**: Stores all persistent data including users, classes, assignments, grades, and attendance records. Relational structure ensures referential integrity across all entities.

---

## Key Design Decisions

| Decision | Choice | Reason |
|---|---|---|
| API style | REST | Simple, widely understood, easy to test |
| Authentication | JWT tokens | Stateless, scalable, no server-side session storage |
| Database | PostgreSQL | Strong relational support, ACID compliance |
| Frontend | React | Component-based, easy to scale UI |
| Hosting | Cloud (e.g., Render / Railway) | Free tiers available for MVP deployment |