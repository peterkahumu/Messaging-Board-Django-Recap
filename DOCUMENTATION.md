# Messaging Board — Documentation (Learning / Recap)

This document is a clear recap of the Django Concepts and explicitly states that the project is intended as a learning resource to review core Django concepts and to pick up new ones.

## Purpose — Learning & Recap

Messaging Board is a small Django application created as a learning project. The goals are:

- Recap foundational Django concepts: models, migrations, admin, views (function-based and/or class-based), templates, URL routing, and testing.

- Provide a minimal, extendable codebase for exercises and demonstrations.

If you're using this repo to learn, try these exercises:

1. Inspect `posts/models.py` and add a new field to the `Post` model. Run migrations and update tests.
2. Convert a function-based view to a class-based view and compare the code size and readability.
3. Add authentication so that only logged-in users can create posts.
4. Add pagination to the posts list view.

## Project structure

- `manage.py` — Django management helper
- `messaging_board/` — Django project settings and configs
- `posts/` — application with `models.py`, `views.py`, `admin.py`, `tests.py`, and `migrations/`
- `templates/` — HTML templates

## Models

See `posts/models.py` for the exact model definitions. Typical fields in a `Post` model include `id` and 'text`.

## Views and templates

Views are defined in `posts/views.py` and render templates from `templates/posts`. Look for list and detail views for posts and the create/edit forms.

## Admin

`posts/admin.py` registers models for the Django admin interface; after creating a superuser, manage data at `/admin/`.

## Tests

Tests are in `posts/tests.py`. Use:

```python
python manage.py test
```

Add tests for any new behavior you introduce.

## Contributing (learning-friendly)

- Keep changes small and well-scoped.
- Include tests for new behavior.
- Document learning exercises and decisions in this file or in a `docs/` folder.


This file is intentionally concise as a recap and learning guide. Expand it with concrete examples and code snippets as you learn.
