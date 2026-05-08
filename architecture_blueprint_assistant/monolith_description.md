# Monolithic Architecture – EduTrack

All components of the EduTrack platform are packaged and deployed as a single unified application. The frontend communicates directly with the backend monolith, which handles all business logic internally.

- **Frontend App**: Web and mobile interface for students, teachers, and admins. Sends HTTP requests to the backend monolith.
- **Authentication Module**: Manages user registration, login, session handling, and role-based access control for students, teachers, and admins.
- **Assignment Module**: Handles creation, distribution, retrieval, and submission tracking of assignments for all classes and users.
- **Grade Calculator Module**: Processes student grades, calculates GPA, and generates performance history and visual reports.
- **AI Study Plan Module**: Analyzes student grade data and generates personalized weekly study plans using AI recommendations.
- **Attendance Module**: Records and manages daily attendance for each class, tracks absences, and generates attendance summary reports.
- **Notification Service**: Sends deadline reminders, grade updates, and attendance alerts via email and in-app notifications.
- **Admin Panel**: Provides school administrators with tools to manage user accounts, monitor platform usage, and generate institutional reports.
- **Database**: Central relational database that stores all application data including users, assignments, grades, attendance records, and notifications.
