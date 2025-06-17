import os
from dotenv import load_dotenv
import time
import psycopg2
from psycopg2 import OperationalError

# Load environment variables from .env file
load_dotenv()

data = "Sample population record for testing"

for _ in range(10):
    try:
        print("Connecting to the database...")
        print(os.getenv("POSTGRES_DB"))
        print(os.getenv("POSTGRES_USER"))
        print(os.getenv("POSTGRES_PASSWORD"))
        print(os.getenv("POSTGRES_HOST"))
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB") or "geo_data",
            user=os.getenv("POSTGRES_USER") or "postgres",
            password=os.getenv("POSTGRES_PASSWORD") or "password",
            host=os.getenv("POSTGRES_HOST") or "db"
        )
        break
    except OperationalError as e:
        print("⏳ Waiting for database to be ready...")
        time.sleep(2)
else:
    raise Exception("❌ Could not connect to the database after multiple attempts.")

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS sample_table (id SERIAL PRIMARY KEY, info TEXT)")
cursor.execute("INSERT INTO sample_table (info) VALUES (%s)", (data,))
conn.commit()

print("Data inserted successfully")
cursor.close()
conn.close()
