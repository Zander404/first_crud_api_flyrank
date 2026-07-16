from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/")
def home():
    return {"name": "Task Api", "version": "1.0", "endpoint": ["/tasks"]}


@app.get("/health")
def health():
    return {"status": "ok"}
