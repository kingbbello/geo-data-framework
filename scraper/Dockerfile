FROM python:3.11-slim
WORKDIR /scraper
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]