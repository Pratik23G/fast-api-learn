<h1 style="font-family: 'Sora', sans-serif;">05 · Template Inheritance</h1>

<p style="font-family: 'Sora', sans-serif;"><strong>Key concept:</strong>
<code>{% extends %}</code> + <code>{% block %}</code> let one base template own the shared page
shell, while each page template only fills in the parts that differ.</p>

## The base: `layout.html`

```jinja
<!doctype html>
<html lang="en">
  <head>
    <title>{% if title %} FastAPI Blog - {{ title }} {% else %} FastAPI Blog {% endif %}</title>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

`{% block content %}` is a named slot. On its own, it renders empty — it's a placeholder for a
child template to override.

## The child: `home.html`

```jinja
{% extends "layout.html" %}
{% block content %}
  {% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.author }}</p>
  {% endfor %}
{% endblock content %}
```

- `{% extends "layout.html" %}` must be the first line — it says "render `layout.html`, but let me
  override its blocks."
- Everything inside `{% block content %} ... {% endblock %}` in `home.html` replaces the empty
  block of the same name in `layout.html`.
- Anything outside a `{% block %}` in a child template is ignored — only block overrides matter.

```mermaid
flowchart TB
    subgraph layout.html
        Head["&lt;head&gt; + &lt;title&gt; (if/else logic)"]
        Slot["{% block content %}\n(empty placeholder)"]
    end

    subgraph home.html
        Extends["{% extends 'layout.html' %}"]
        Fill["{% block content %}\nfor-loop over posts\n{% endblock %}"]
    end

    Extends -.->|"inherits shell from"| layout.html
    Fill ==>|"fills"| Slot
```

## Why this replaced copy-pasted HTML

Before inheritance, every page would need its own `<head>`, `<title>` logic, etc. duplicated. Now:

- One place (`layout.html`) owns the `<head>`, title logic, and page shell.
- New pages (post detail, create-post form, etc.) just `{% extends "layout.html" %}` and define
  their own `{% block content %}` — no boilerplate duplication.

<p style="font-family: 'Sora', sans-serif;"><strong>Why it matters:</strong> this is what makes
adding more pages later (post detail, forms, error pages) cheap — each new template is just its
unique content, not a full HTML document.</p>
