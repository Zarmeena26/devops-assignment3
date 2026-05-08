# Uses a much smaller base image
FROM python:3.10-slim

WORKDIR /app

# Only install Flask to save space (skip mysql-connector if not needed for the demo)
RUN pip install --no-cache-dir flask

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
