from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Live Blog API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema data blog
class Blog(BaseModel):
    id: int
    title: str
    content: str
    author: str

# Dummy database
database_blog: List[Blog] = []

# Root endpoint
@app.get("/")
def root():
    return {"message": "Live Blog API Running"}

# GET semua blog
@app.get("/api/blogs")
def get_blogs():
    return database_blog

# POST tambah blog
@app.post("/api/blogs")
def add_blog(blog: Blog):
    database_blog.append(blog)
    return {
        "message": "Blog berhasil ditambahkan",
        "data": blog
    }