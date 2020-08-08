gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --workers=9 src.frameworks.fastapi_app.runner:app
