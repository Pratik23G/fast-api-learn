from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts: list[dict] = [
  {
    "id": 1,
    "title": "Getting Started with FastAPI and UV",
    "author": "Pratik",
    "date_posted": "2026-07-03"
  },
  {
    "id": 2,
    "title": "Mastering Python Package Management",
    "author": "Jane Doe",
    "date_posted": "2026-07-02"
  },
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts