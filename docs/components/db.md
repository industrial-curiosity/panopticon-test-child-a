# db

## Responsibility

PostgreSQL catalog persistence via psycopg2 (`inventory/db/catalog.py`). Reads the
`postgres-catalog` database: product lookup, product listing, and search. Deliberately out of
scope: REST surfaces (api), outbound clients (clients).

## Interfaces

- `postgres-catalog` (database) — **consumed**; the catalog PostgreSQL database.

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/db/catalog.py` — `get_connection` (RealDictCursor over `CATALOG_DB_DSN`),
  `get_product`, `list_products`, `search_products` (name/SKU `ILIKE` search).

## Configuration

- `CATALOG_DB_DSN` (required) — psycopg2 connection DSN for the catalog database.

## Failure modes

- `psycopg2.connect(DSN)` raises when the database is unreachable or the DSN is invalid;
  queries raise on connection failure mid-call. No connection pooling or retry is present.
