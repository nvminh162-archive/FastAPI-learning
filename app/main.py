from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Book Management API",
    description="Simple API to manage books, authors, categories, book covers",
    version="1.0.0"
)

@app.get("/")

def read_root():
    return {
        "message": "Book management API is running"
    }