from fastapi import FastAPI, Request, HTTPException, status
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

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
      request, "home.html", {"posts": posts, "title": "Home"},
    )

@app.get("/posts/{post_id}", include_in_schema=False)
def post_page(request:Request, post_id: int):
  for post in posts:
    if post.get("id") == post_id:
      title = post["title"][:50]
      return templates.TemplateResponse(
      request, "post.html", {"post": post, "title": ""},
    )
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
  for post in posts:
    if post.get("id") == post_id:
      return post
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")