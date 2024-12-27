#!/bin/sh

set -e

# Start Gunicorn with Uvicorn worker
exec gunicorn app.api:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000 --forwarded-allow-ips='*'
