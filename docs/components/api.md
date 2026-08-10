# api

## Responsibility

REST HTTP surface of this service: two FastAPI apps. `inventory-api`
(`inventory/api/routes.py`) serves inventory list/get/update and reserve/release; `orders-api`
(`inventory/api/orders_routes.py`) serves order list/get. Produces both interfaces; owns their
API component. Deliberately out of scope: catalog persistence (db), outbound clients (clients),
background consumption (events, queue), snapshots (storage).

## Interfaces

- `inventory-api` (rest) — **produced**, owned by this repo (api component).
- `orders-api` (rest) — **produced**, owned by this repo (api component).

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/api/routes.py` — `inventory-api` FastAPI app: `GET /inventory`, `GET /inventory/{sku}`,
  `PUT /inventory/{sku}`, `POST /inventory/reserve`, `POST /inventory/release`.
- `inventory/api/orders_routes.py` — `orders-api` FastAPI app: `GET /orders`, `GET /orders/{order_id}`.

## Configuration

The route modules read no configuration. The FastAPI apps are constructed at import time with
fixed titles and versions; no application bootstrap in this repo mounts or configures them.

## Failure modes

- `inventory-api` / `orders-api` endpoints unavailable → inventory and order operations fail for
  callers. The apps return 404 for unknown SKUs and otherwise produce placeholder responses; no
  persistence or retry logic lives in this component.
