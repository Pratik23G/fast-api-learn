<h1 style="font-family: 'Sora', sans-serif;">03 · Jinja2Templates & Dynamic Rendering</h1>

<p style="font-family: 'Sora', sans-serif;"><strong>Key concept:</strong>
<code>Jinja2Templates</code> turns a template file + a Python dict of context data into an HTML
response — no manual string concatenation.</p>

## Wiring it up

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"},
    )
```

- `directory="templates"` — where `.html` template files live.
- `TemplateResponse` needs the `request` object (Starlette requirement) plus the template name and
  a context dict — every key in that dict becomes a variable inside the template.

## Looping over data with `{% for %}`

```jinja
{% for post in posts %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.author }}</p>
{% endfor %}
```

- `{{ post.title }}` — "dot access" into a dict, same syntax as attribute access. Jinja2 tries
  attribute access first, then falls back to `dict[key]` — so this works whether `post` is a dict
  or an object.
- The loop body re-renders once per item in `posts`, so adding a post to the Python list is enough
  to add a rendered block — no template changes needed.

```mermaid
flowchart LR
    Route["route handler"] -->|"context dict\n{posts, title}"| TR["TemplateResponse"]
    TR --> Engine["Jinja2 engine"]
    Engine -->|"{% for post in posts %}"| Loop["renders once per post"]
    Loop --> HTML["final HTML"]
```

<p style="font-family: 'Sora', sans-serif;"><strong>Why it matters:</strong> this is the core
loop (pun intended) of server-rendered apps — Python data in, HTML out, with the template staying
dumb and the data staying in Python.</p>
