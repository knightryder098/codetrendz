# Open Source Language Trends Tracker (CodeTrendz)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](<!-- Link to your CI/CD pipeline -->)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) <!-- Choose appropriate license -->

## Overview

CodeTrendz is a web application designed to track and visualize the usage trends of programming languages within the public open-source software ecosystem, initially focusing on GitHub repositories. It provides developers, tech leads, students, and researchers with dynamic, data-driven insights into language popularity, helping inform technology choices and learning paths. The application automatically scans for new repositories, processes language data, and updates trend charts periodically.

## Key Features (v1.0)

*   **Automated Data Collection:** Periodically scans public GitHub repositories to gather language usage statistics.
*   **Trend Analysis:** Aggregates data to calculate the percentage usage of different languages over time.
*   **Dynamic Visualization:** Displays language trends using interactive charts (line charts for trends, bar/pie charts for current snapshots).
*   **Filtering & Time Range:** Allows users to filter by specific languages and select different time ranges for analysis.
*   **Curated Learning Resources:** Provides links to high-quality learning materials for popular and trending languages.
*   **Scalable Architecture:** Built with scalability and maintainability in mind.
*   **Separate Environments:** Supports distinct Development, Testing, and Production environments.

## Tech Stack (Planned)

*   **Frontend:** React / Vue / Angular (TBD), Chart.js / Plotly.js / D3.js (TBD)
*   **Backend API:** Python (Flask/Django) / Node.js (Express) (TBD)
*   **Data Processing:** Python, Celery (or RQ), RabbitMQ / Redis (TBD)
*   **Database:** PostgreSQL with TimescaleDB extension (preferred for time-series data)
*   **Caching:** Redis / Memcached
*   **Infrastructure:** Docker, Nginx/Apache, Cloud Provider (AWS/GCP/Azure - TBD)
*   **CI/CD:** GitHub Actions / Jenkins / GitLab CI (TBD)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Git
*   Docker & Docker Compose
*   Python 3.x / Node.js (depending on backend choice)
*   Access to GitHub API (requires a personal access token)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Environment Variables:**
    *   Copy the example environment file: `cp .env.example .env`
    *   Edit the `.env` file and add your necessary configurations (e.g., GitHub API Token, Database credentials, Secret Keys). **DO NOT commit your `.env` file.**

3.  **Build and Run using Docker Compose (Recommended):**
    ```bash
    docker-compose up --build
    ```
    This should build the necessary images and start the services (API, worker, database, frontend server if applicable).

4.  **Manual Setup (Alternative - Requires specific language/framework setup):**
    *   Install backend dependencies: `pip install -r requirements.txt` (Python) or `npm install` (Node.js)
    *   Install frontend dependencies: `cd frontend && npm install`
    *   Setup database manually.
    *   Run migrations (if applicable).

## Running the Application

*   **Using Docker Compose:** `docker-compose up`
*   **Manually:**
    *   Start the database service.
    *   Start the message queue (Redis/RabbitMQ).
    *   Start the backend API server (e.g., `flask run` or `npm start`).
    *   Start the Celery worker(s) (e.g., `celery -A project.celery worker --loglevel=info`).
    *   Start the Celery beat scheduler (e.g., `celery -A project.celery beat --loglevel=info`).
    *   Start the frontend development server (e.g., `cd frontend && npm run dev`).

Access the application via `http://localhost:<FRONTEND_PORT>` (check your configuration).

## Running Tests

*   **Backend Tests:**
    ```bash
    # Example for Python/pytest
    docker-compose exec backend pytest
    # Or run manually within the backend container/environment
    ```
*   **Frontend Tests:**
    ```bash
    # Example for Node.js/Jest
    docker-compose exec frontend npm test
    # Or run manually within the frontend directory
    cd frontend && npm test
    ```

## Deployment

Deployment is managed via a CI/CD pipeline configured for distinct **Development**, **Testing/Staging**, and **Production** environments. Pushes to specific branches trigger automated builds, tests, and deployments (with manual approval for Production).

## Contributing

Please read `CONTRIBUTING.md` (<!-- Add link if you create one -->) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the <!-- Choose License e.g., MIT --> License - see the `LICENSE` file for details.

## Contact

<!-- Optional: Add contact information or link to project page --> 