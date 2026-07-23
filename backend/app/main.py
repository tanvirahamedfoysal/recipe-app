import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

app = FastAPI(
    title="FastAPI Application to Manage Recipe App's API",
    description="A simple FastAPI application for managing recipes",
    version="1.0.0",
    debug=True,
)

app.include_router(v1_router)