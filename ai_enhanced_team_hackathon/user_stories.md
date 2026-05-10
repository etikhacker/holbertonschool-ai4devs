# User Stories

## Project: AI-Enhanced Team Collaboration Platform

---

### Epic 1: User Authentication & Onboarding

**US-001 — User Registration**
As a **new user**, I want to **register an account using my email and password**, so that I can **access the platform and collaborate with my team**.

*Acceptance Criteria:*
- User can fill in name, email, and password fields
- Email must be unique; duplicate registration shows an error message
- Password must be at least 8 characters with at least one number
- Upon successful registration, user is redirected to the onboarding flow

---

**US-002 — User Login**
As a **registered user**, I want to **log in with my credentials**, so that I can **securely access my workspace and team data**.

*Acceptance Criteria:*
- User can log in with email and password
- Failed login shows a clear error without revealing which field is wrong
- Successful login redirects user to their dashboard
- Session persists across page refreshes (token-based auth)

---

### Epic 2: Project & Task Management

**US-003 — Create a Project**
As a **team lead**, I want to **create a new project and invite team members**, so that I can **organize work and collaborate effectively**.

*Acceptance Criteria:*
- User can create a project with a name, description, and deadline
- User can invite members by email
- Invited members receive a notification/email
- Project appears on all members' dashboards

---

**US-004 — Create and Assign Tasks**
As a **project manager**, I want to **create tasks within a project and assign them to team members**, so that **everyone knows their responsibilities**.

*Acceptance Criteria:*
- Tasks have a title, description, priority (low/medium/high), due date, and assignee
- Assignee receives a notification upon being assigned
- Tasks are visible in the project board view
- Tasks can be reassigned at any time

---

**US-005 — Track Task Status**
As a **team member**, I want to **update the status of my tasks (To Do / In Progress / Done)**, so that **the whole team can see real-time progress**.

*Acceptance Criteria:*
- Status can be changed via a dropdown or drag-and-drop on a Kanban board
- Status changes are timestamped and visible in task history
- Dashboard reflects updated task counts automatically

---

### Epic 3: AI-Powered Features

**US-006 — AI Task Summary Generation**
As a **project manager**, I want to **generate an AI-powered summary of all open tasks and blockers**, so that I can **quickly understand the state of the project without reading every task**.

*Acceptance Criteria:*
- A "Generate Summary" button is available on the project dashboard
- The AI returns a concise paragraph summarizing progress, pending items, and any flagged risks
- Summary is saved with a timestamp for future reference
- User can regenerate the summary at any time

---

**US-007 — AI-Assisted Task Description Writing**
As a **team member**, I want to **get AI suggestions when writing a task description**, so that I can **write clearer, more actionable task definitions faster**.

*Acceptance Criteria:*
- An "Improve with AI" button appears in the task description field
- AI enhances clarity, adds acceptance criteria suggestions, and flags vague language
- User can accept, reject, or edit the AI suggestion before saving
- Original text is preserved if the user dismisses the suggestion

---

**US-008 — AI Sprint Planning Assistant**
As a **team lead**, I want to **get AI recommendations on how to distribute tasks across team members for the upcoming sprint**, so that I can **balance workload fairly and meet deadlines**.

*Acceptance Criteria:*
- AI analyzes team members' current workload, skills (tags), and task complexity
- Recommendations are presented as a proposed sprint plan with reasoning
- User can accept recommendations fully or partially
- Plan can be re-generated if the user changes sprint parameters

---

### Epic 4: Communication & Notifications

**US-009 — In-App Notifications**
As a **team member**, I want to **receive in-app notifications for task assignments, status changes, and mentions**, so that I **stay informed without checking email constantly**.

*Acceptance Criteria:*
- Notification bell icon shows unread count
- Notifications are grouped by project
- Clicking a notification navigates to the relevant task or comment
- User can mark all notifications as read

---

**US-010 — Comment on Tasks**
As a **team member**, I want to **leave comments on tasks and mention teammates using @username**, so that I can **discuss details and get feedback in context**.

*Acceptance Criteria:*
- Comments support plain text and @mentions
- Mentioned users receive a notification
- Comments are ordered chronologically with author name and timestamp
- Comments can be edited or deleted by the author within 10 minutes of posting