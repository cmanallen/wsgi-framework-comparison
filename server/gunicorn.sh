gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --workers=9 fastapi_runner:app
