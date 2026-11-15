from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Frontend ko connect hone ki ijazat dena (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Qadir DevOps Project Backend API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "project": "EKS-Cost-Optimized"}