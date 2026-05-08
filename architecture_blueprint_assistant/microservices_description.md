# Microservices Architecture

## Overview

This document describes the microservices architecture for a ride-sharing application. The system is decomposed into **8 independent services**, each with its own database, communicating via an API Gateway (synchronous REST/gRPC) and a Message Broker (asynchronous events).

---

## Services

### 1. API Gateway
**Role:** Single entry point for all client requests (web and mobile).  
**Responsibilities:**
- Routes incoming requests to the appropriate downstream service.
- Handles SSL termination, rate limiting, and load balancing.
- Enforces authentication tokens in cooperation with the Auth Service.
- Aggregates responses when needed (Backend for Frontend pattern).

---

### 2. Auth Service
**Role:** Manages all authentication and authorization logic.  
**Responsibilities:**
- Issues and validates JWT / OAuth2 tokens.
- Handles user registration, login, logout, and password reset.
- Supports social login (Google, Facebook).
- Stores credentials securely in its own **PostgreSQL** database.

**Interactions:**
- Called by the API Gateway on every protected request.
- Publishes `user.registered` events to the Message Broker.

---

### 3. User Service
**Role:** Manages user profiles for both riders and drivers.  
**Responsibilities:**
- CRUD operations for user profiles (name, photo, contact info).
- Driver profile management (license, vehicle info, availability status).
- Stores data in its own **PostgreSQL** database.

**Interactions:**
- Consumed by Ride Service (to attach driver/rider info to rides).
- Listens to `user.registered` events from the Message Broker to initialize profiles.

---

### 4. Ride Service
**Role:** Core business logic for ride lifecycle management.  
**Responsibilities:**
- Creating, searching, and booking rides.
- Matching riders with available drivers.
- Managing ride states: `REQUESTED → ACCEPTED → IN_PROGRESS → COMPLETED → CANCELLED`.
- Stores ride data in its own **MongoDB** database (flexible schema for ride metadata).

**Interactions:**
- Calls Tracking Service to get real-time driver location.
- Publishes `ride.booked`, `ride.completed`, `ride.cancelled` events to the Message Broker.

---

### 5. Payment Service
**Role:** Handles all financial transactions within the platform.  
**Responsibilities:**
- Calculates fare based on distance, time, and surge pricing.
- Processes payments via an external payment gateway (e.g., Stripe).
- Manages refunds and payment history.
- Stores transaction records in its own **PostgreSQL** database.

**Interactions:**
- Triggered by `ride.completed` events from the Message Broker.
- Publishes `payment.success` and `payment.failed` events.
- Integrates with an **External Payment Gateway** (Stripe / PayPal).

---

### 6. Notification Service
**Role:** Delivers real-time and asynchronous notifications to users.  
**Responsibilities:**
- Sends push notifications, emails, and SMS messages.
- Handles templates for different notification types (ride confirmation, payment receipt, promotions).

**Interactions:**
- Listens to events from the Message Broker: `ride.booked`, `payment.success`, `ride.cancelled`, etc.
- Integrates with **SendGrid** (email) and **Twilio** (SMS) as external providers.
- Does **not** expose a public API — fully event-driven.

---

### 7. Tracking Service
**Role:** Manages real-time GPS location of drivers.  
**Responsibilities:**
- Ingests live location updates from driver mobile apps (via WebSocket).
- Stores the latest driver position in **Redis** (low-latency, in-memory cache).
- Provides nearest-driver lookup for the Ride Service.
- Publishes location update events for the Analytics Service.

**Interactions:**
- Queried synchronously by the Ride Service for driver matching.
- Publishes `location.updated` events to the Message Broker.

---

### 8. Analytics Service
**Role:** Collects, processes, and exposes platform metrics and insights.  
**Responsibilities:**
- Aggregates events (rides, payments, user activity) into analytical data.
- Powers dashboards for business intelligence (active rides, revenue, peak hours).
- Stores data in **ClickHouse** (columnar DB optimized for analytics queries).

**Interactions:**
- Listens to all major events from the Message Broker (read-only consumer).
- Does **not** interact with other services directly — purely event-driven.

---

### 9. Review & Rating Service
**Role:** Manages post-ride reviews and ratings for riders and drivers.  
**Responsibilities:**
- Allows riders to rate drivers (and vice versa) after ride completion.
- Calculates and stores cumulative ratings per user.
- Stores reviews in its own **MongoDB** database.

**Interactions:**
- Triggered by `ride.completed` events from the Message Broker.
- Publishes `review.submitted` events for the Analytics Service.
- Exposes rating data to the User Service for profile display.

---

## Communication Patterns

| Pattern | Used For |
|---|---|
| **Synchronous REST/gRPC** | API Gateway → Services (real-time user requests) |
| **Asynchronous Events (MQ)** | Inter-service communication (Kafka / RabbitMQ) |
| **WebSocket** | Driver location streaming → Tracking Service |

---

## Database Strategy

Each service owns its database — no shared databases between services (Database-per-Service pattern). This ensures loose coupling and independent scalability.

| Service | Database | Reason |
|---|---|---|
| Auth Service | PostgreSQL | ACID compliance for credentials |
| User Service | PostgreSQL | Relational user data |
| Ride Service | MongoDB | Flexible ride metadata |
| Payment Service | PostgreSQL | ACID compliance for transactions |
| Review Service | MongoDB | Flexible review documents |
| Tracking Service | Redis | Low-latency location caching |
| Analytics Service | ClickHouse | Columnar storage for fast aggregations |
