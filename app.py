import os

from flask import Flask, jsonify
from psycopg_pool import ConnectionPool

app = Flask(__name__)


def read_secret(path="/run/secrets/pg_password"):
    with open(path, "r") as file:
        return file.read().strip()


db_password = read_secret()

DATABASE_URL = (
    f"postgresql://{os.environ['DB_USER']}:{db_password}"
    f"@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}"
    f"/{os.environ['DB_NAME']}"
)

pool = ConnectionPool(DATABASE_URL)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask + PostgreSQL funcionando"
    })


@app.route("/items")
def get_items():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, task, priority FROM items ORDER BY id"
            )

            rows = cur.fetchall()

    items = [
        {
            "id": row[0],
            "task": row[1],
            "priority": row[2]
        }
        for row in rows
    ]

    return jsonify(items)
