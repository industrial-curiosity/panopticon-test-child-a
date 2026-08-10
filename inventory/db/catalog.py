import os
import psycopg2
from psycopg2.extras import RealDictCursor

# panopticon-interface product-catalog-db
DSN = os.environ["CATALOG_DB_DSN"]


def get_connection():
    return psycopg2.connect(DSN, cursor_factory=RealDictCursor)


def get_product(sku: str) -> dict | None:
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM products WHERE sku = %s", (sku,))
        return cur.fetchone()


def list_products(limit: int = 100, offset: int = 0) -> list[dict]:
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM products ORDER BY sku LIMIT %s OFFSET %s", (limit, offset))
        return cur.fetchall()


def search_products(query: str) -> list[dict]:
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM products WHERE name ILIKE %s OR sku ILIKE %s",
            (f"%{query}%", f"%{query}%"),
        )
        return cur.fetchall()
