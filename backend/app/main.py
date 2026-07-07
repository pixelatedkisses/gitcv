from fastapi import FastAPI

app = FastAPI(
    title="GitCV API",
    description="Generates a polished LaTeX CV from a GitHub profile and opens it in Overleaf.",
    version="0.1.0",
)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "gitcv"}