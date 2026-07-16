from fastapi import FastAPI, Request
from tasks.routes import router as tasks_routes

app = FastAPI(
    title="Task Api", version="1.0", summary="Api to create tasks", redoc_url="/redocs"
)


@app.get("/")
def home():
    return {"name": "Task Api", "version": "1.0", "endpoint": ["/tasks"]}


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(router=tasks_routes)
