from fastapi import FastAPI
from app.api import upload

app = FastAPI(title="AWS Resume Analyzer")

# Register API routes
app.include_router(upload.router)

@app.get("/")
def health_check():
    return {"status": "running"}