from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload
from app.api import analyze
from app.api import history

app = FastAPI(title="AWS Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(history.router)

@app.get("/")
def health_check():
    return {"status": "running"}