# Project Tasks & To-Do List - CodeTrendz

This document tracks the development tasks for the Open Source Language Trends Tracker project, based on the Product Requirements Document (PRD).

## Legend

*   `[ ]` To Do
*   `[x]` Done
*   `[-]` In Progress / Blocked
*   `(P#)` Priority (P1=High, P2=Medium, P3=Low)
*   `(PRD: X.Y)` Reference to relevant PRD section

## Phase 1: Project Setup & Core Infrastructure (P1)

*   [ ] (P1) Initialize Git repository and define branching strategy (e.g., Gitflow).
*   [ ] (P1) Choose primary backend language/framework (Python/Flask, Node/Express, etc.).
*   [ ] (P1) Choose primary frontend framework (React, Vue, etc.).
*   [ ] (P1) Choose charting library (Chart.js, Plotly.js, etc.).
*   [ ] (P1) Setup basic project structure (backend, frontend, docker).
*   [ ] (P1) Setup Docker configuration (`Dockerfile` for services, `docker-compose.yml` for local dev). (PRD: 8)
*   [ ] (P1) Configure environment variable handling (`.env` files, `.env.example`). (PRD: 4.4.3)
*   [ ] (P2) Setup initial database schema (PostgreSQL + TimescaleDB recommended). (PRD: 6)
*   [ ] (P2) Setup task queue system (Celery + Redis/RabbitMQ). (PRD: 7)
*   [ ] (P2) Setup basic CI/CD pipeline (Linting, basic build). (PRD: 8)
*   [ ] (P3) Choose and setup logging framework/aggregator basics. (PRD: 8)
*   [ ] (P3) Choose and setup basic monitoring placeholders. (PRD: 8)
*   [ ] (P3) Define coding standards and setup linters/formatters. (PRD: NFR4)

## Phase 2: Data Acquisition & Processing Backend (P1)

*   [ ] (P1) Implement GitHub API client wrapper (handling authentication). (PRD: F1.1)
*   [ ] (P1) Implement robust GitHub API rate limit handling (backoff, retry). (PRD: F1.1, R1)
*   [ ] (P1) Develop repository discovery logic (using GitHub Search API, configurable criteria). (PRD: F1.1)
*   [ ] (P1) Implement task to fetch language statistics for a single repository. (PRD: F1.2)
*   [ ] (P1) Design and implement database schema for storing repository metadata and trend snapshots. (PRD: 6)
*   [ ] (P2) Develop data aggregation logic (calculate language percentages per period). (PRD: F1.3)
*   [ ] (P1) Implement scheduler (Celery Beat) to trigger discovery and aggregation tasks periodically. (PRD: F4.1)
*   [ ] (P2) Implement basic job monitoring/logging for data tasks. (PRD: F4.2)
*   [ ] (P2) Write unit and integration tests for data acquisition and processing logic. (PRD: NFR4)
*   [ ] (P3) Consider initial data backfill strategy (or decide to start fresh). (PRD: R7)

## Phase 3: API Backend (P1)

*   [ ] (P1) Setup backend API framework (Flask/Django/Express).
*   [ ] (P1) Develop API endpoint to serve aggregated language trend data (time series). (PRD: F2.1)
*   [ ] (P2) Implement filtering capabilities in the API (by language, time range). (PRD: F2.2, F2.3)
*   [ ] (P2) Implement API endpoint to serve current language snapshot data (for bar/pie charts). (PRD: F2.1)
*   [ ] (P2) Implement API endpoint to serve list of available languages for filtering.
*   [ ] (P2) Implement API caching (e.g., Redis) for trend data endpoints. (PRD: 7, NFR1)
*   [ ] (P2) Write API tests (unit/integration tests for endpoints). (PRD: NFR4)
*   [ ] (P3) Implement basic API security measures (HTTPS setup handled by infra, consider input validation). (PRD: NFR5)
*   [ ] (P3) Add endpoint to show "Last Updated" timestamp. (PRD: F2.4)

## Phase 4: Frontend & Visualization (P1)

*   [ ] (P1) Setup frontend project structure.
*   [ ] (P1) Implement basic layout and routing.
*   [ ] (P1) Integrate chosen charting library.
*   [ ] (P1) Develop main chart component to display language trends (line chart). (PRD: F2.1)
*   [ ] (P1) Fetch data from the backend API and display it in the chart.
*   [ ] (P2) Implement chart interactivity (tooltips, toggling lines). (PRD: F2.1)
*   [ ] (P2) Implement language selection/filtering UI controls. (PRD: F2.2)
*   [ ] (P2) Implement time range selection UI controls. (PRD: F2.3)
*   [ ] (P2) Implement alternative chart views (bar chart/pie chart for current snapshot). (PRD: F2.1)
*   [ ] (P1) Ensure basic responsive design for different screen sizes. (PRD: F2.5)
*   [ ] (P2) Display "Last Updated" timestamp fetched from API. (PRD: F2.4)
*   [ ] (P3) Write basic frontend component tests. (PRD: NFR4)

## Phase 5: Learning Resources Feature (P2)

*   [ ] (P2) Design simple database schema or configuration format for learning resources. (PRD: F3.3, 6)
*   [ ] (P2) Develop API endpoint(s) to CRUD learning resources (Admin only). (PRD: F3.3)
*   [ ] (P2) Develop API endpoint to fetch curated resources for display (filtered by language). (PRD: F3.2)
*   [ ] (P2) Create basic Admin UI (or script) for managing resources. (PRD: F3.3)
*   [ ] (P2) Develop frontend section/page to display learning resources grouped by language. (PRD: F3.2)
*   [ ] (P3) Implement logic to automatically identify "trending" languages to feature. (PRD: F3.1)
*   [ ] (P3) Curate initial set of high-quality learning resources for top 5-10 languages.

## Phase 6: Testing & Quality Assurance (P1/P2)

*   [ ] (P1) Ensure adequate unit test coverage for backend logic (data processing, API).
*   [ ] (P2) Write integration tests for API endpoints.
*   [ ] (P2) Write basic integration tests for data pipeline (e.g., trigger job, check DB).
*   [ ] (P2) Write frontend component tests.
*   [ ] (P3) Plan for End-to-End (E2E) testing setup (e.g., Cypress, Playwright).
*   [ ] (P2) Perform manual testing and User Acceptance Testing (UAT) in the Test environment. (PRD: 8)
*   [ ] (P3) Setup performance testing baseline. (PRD: NFR1)

## Phase 7: Deployment & Operations (P2)

*   [ ] (P1) Finalize Docker configurations for all environments.
*   [ ] (P2) Choose cloud provider and setup basic infrastructure (VMs/Containers, DB service, Cache service, Load Balancer). (PRD: 7)
*   [ ] (P2) Configure separate Dev, Test, and Prod environments (secrets management, DBs, etc.). (PRD: 8)
*   [ ] (P1) Enhance CI/CD pipeline for automated testing and deployment to Test env. (PRD: 8)
*   [ ] (P2) Configure CI/CD pipeline for deployment to Prod (with manual trigger/approval). (PRD: 8)
*   [ ] (P2) Setup monitoring and alerting for Prod environment (Application errors, Infra metrics, Job failures). (PRD: 8, F4.2)
*   [ ] (P2) Implement database backup strategy. (PRD: NFR3)
*   [ ] (P3) Configure web server (Nginx/Apache) for proxying, HTTPS. (PRD: 7, NFR5)

## Phase 8: Documentation (P2)

*   [ ] (P1) Complete `README.md` with final setup instructions.
*   [ ] (P2) Document API endpoints (e.g., using OpenAPI/Swagger).
*   [ ] (P2) Add code comments where necessary.
*   [ ] (P3) Write basic architecture overview document. (PRD: NFR4)
*   [ ] (P3) Document deployment process and operational procedures (runbooks).
*   [ ] (P1) Add `LICENSE` file.
*   [ ] (P3) Create `CONTRIBUTING.md` guidelines (optional for initial phase).

## Future Considerations (Post V1.0)

*   [ ] Explore adding GitLab/Bitbucket support. (PRD: 9)
*   [ ] Plan advanced filtering options. (PRD: 9)
*   [ ] Design language drill-down features. (PRD: 9)
*   [ ] Investigate framework/library trend analysis feasibility. (PRD: 9) 