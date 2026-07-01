import sys
from pathlib import Path
from contextlib import asynccontextmanager

# Ensure the Backend root directory is on sys.path so local imports work
current_file = Path(__file__).resolve()
project_root = current_file.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router
from app.core import settings, async_init_settings


@asynccontextmanager
async def lifespan(app: FastAPI):

    try:
        await async_init_settings()
        print(f"🚀 Starting {settings.api_title}")
    except Exception as exc:
        print("Warning: failed to initialize settings on startup:", exc)
    yield
    print(f"🛑 Shutting down {settings.api_title}")


app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description=settings.api_description,
    debug=settings.debug,
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
