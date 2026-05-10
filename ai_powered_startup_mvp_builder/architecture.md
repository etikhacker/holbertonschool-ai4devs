# System Architecture - Smart Task Prioritizer

## High-Level System Diagram
The application is a client-side JavaScript application utilizing a local-first data strategy.



### Core Components:
1. **Frontend View**: Handles all UI rendering and user interactions using modern HTML/CSS/JS.
2. **Priority Engine**: A specialized logic module that weighs 'Urgency' (Deadline) against 'Complexity' (Effort) to generate a numeric Priority Score.
3. **Storage Layer**: Uses Browser LocalStorage to maintain state without a backend database.
4. **Export Module**: Facilitates data portability by converting the internal state into CSV format.