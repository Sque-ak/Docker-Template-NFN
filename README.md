# Docker Template: FastAPI + Nuxt + Nginx + i18n

This project is a template for deploying a web application using FastAPI for the backend, Vue.js for the frontend, and Nginx as a reverse proxy. All components are packaged into Docker containers for easy deployment and management.

## Project Structure

- **backend/**: Directory containing FastAPI code.
- **frontend/**: Directory containing Nuxt code.
- **nginx/**: Configuration files for Nginx.
- **docker-compose.yml**: File for managing containers with Docker Compose.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Sque-ak/Docker-Template-NFN.git
cd Docker-Template-NFN
```

2. **Configure environment variables:**

Create a `.env` file in the root of the project and add the necessary environment variables for configuring the database and other services.

3. **Start the containers:**

```bash
docker-compose up --build
```

This will build and start the containers for FastAPI, Vue, and Nginx.

## Usage

- **Frontend** will be accessible at `http://localhost`.
- **Backend API** will be accessible through Nginx at `http://localhost/api`.