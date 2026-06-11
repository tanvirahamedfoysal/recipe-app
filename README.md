# Recipe App

A practice assignment implementing a simple recipe-style app with a Flutter frontend and a FastAPI backend.

## Overview

- **Frontend:** Flutter app for mobile and desktop UI.
- **Backend:** FastAPI REST API powered by SQLAlchemy and asyncpg.
- **Purpose:** Assignment / practice project demonstrating a full-stack architecture.

## Repository structure

- `backend/` — FastAPI application and backend service logic.
  - `api/routes/` — API route modules.
  - `crud/` — database CRUD operations.
  - `schemas/` — Pydantic request and response models.
  - `services/` — business logic and service layer.
  - `core/` — configuration and security utilities.
  - `db/` — database setup and SQL schema.

- `frontend/` — Flutter application.
  - `lib/` — Flutter Dart source code.
  - `android/`, `ios/`, `macos/`, `linux/`, `windows/`, `web/` — platform folders.

## Backend

### Requirements

- Python 3.12+
- `uv` or another Python package manager

### Install dependencies

```bash
cd backend
uv install
```

If you do not have a lock file or want to install manually, use the package names from `pyproject.toml`:

```bash
uv add fastapi[standard] sqlalchemy asyncpg pydantic-settings
```

### Configuration

Create a `.env` file in the `backend/` directory with your own secure values for database connection, secret key, and debug settings.

### Run backend

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Frontend

### Requirements

- Flutter SDK
- Platform tooling for your target device (`android`, `ios`, `macos`, `linux`, `windows`, or `web`)

### Run frontend

```bash
cd frontend
flutter pub get
flutter run
```

This starts the Flutter app and connects to the configured backend API if implemented.

## Notes

- The backend uses environment variables loaded from `.env` via `pydantic-settings`.
- The frontend is a Flutter starter app and can be extended with screens, API integration, and state management.
- This repository is built as an assignment and is a good base for expanding into a full recipe or review application.

## Recommended next steps

- Implement API endpoints in `backend/api/routes/`.
- Connect the Flutter UI to backend endpoints.
- Add database migrations or initialization for the backend schema.
- Expand frontend screens for recipes, reviews, and user authentication.
