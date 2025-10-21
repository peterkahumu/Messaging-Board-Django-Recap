# Messaging Board Django Concepts Recap

# Messaging Board — Django Concepts Recap & Learning Project

This repository hosts a small Django application called Messaging Board. It is a learning project created to recap core Django concepts and to pick up new ones while experimenting with project structure, models, views, templates, and tests.

Why this project exists
- Recap key Django concepts (models, views, templates, admin, routing, testing).
- Practice new concepts and patterns in a lightweight app.
- Provide a simple, extendable codebase for learning and demos.

# Quick start

1. Create and activate a Python virtual environment:

	```python
    python -m venv .venv
	source .venv/bin/activate
    ```

2. Install Django (and other dependencies you add):

	```python
    pip install django
    ```

3. Run migrations and create a superuser:

    ```python
	python manage.py migrate
	python manage.py createsuperuser
    ```

4. Run the development server:

    ```python
	python manage.py runserver
    ```

5. Open `http://127.0.0.1:8000/` in your browser.

# Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for a concise recap and more details about the project, including structure, models, views, testing, and contributing guidance.

Project layout (high level)

- `manage.py` — Django management utility
- `messaging_board/` — project configuration (settings, urls, wsgi/asgi)
- `posts/` — application containing models, views, admin, and tests for the message posts
- `templates/` — HTML templates used by the app

# Running tests

Run unit tests with:

```python
python manage.py test
```

Contributing

- This is a learning repo — feel free to open issues or PRs to propose exercises, improvements, or additional tests.
- When adding functionality, include tests and update `DOCUMENTATION.md`.

# License

For more details, see [LICENSE](LICENSE)

