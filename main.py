from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
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

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
      request, "home.html", {"posts": posts, "title": "Home"},
    )


@app.get("/api/posts")
def get_posts():
    return posts