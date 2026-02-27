from fastapi import FastAPI
from app.api import upload
from app.api import analyze
from app.api import history

app = FastAPI(title="AWS Resume Analyzer")


app.include_router(upload.router)
app.include_router(analyze.router)
app.imclude_router(history.router)

@app.get("/")
def health_check():
    return {"status": "running"}