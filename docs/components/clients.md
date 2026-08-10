# clients

## Responsibility

Outbound HTTP integration clients for external services: warehouse ERP
(`inventory/clients/erp.py`), order processing (`inventory/clients/order_processing.py`), and
orders (`inventory/clients/orders.py`). Consumes the `warehouse-erp-api`,
`order-processing-api`, and `orders-api` REST interfaces. Deliberately out of scope: inbound REST
surfaces (api), catalog persistence (db).

## Interfaces

- `warehouse-erp-api` (rest) — **consumed**; ERP stock and replenishment endpoints.
- `order-processing-api` (rest) — **consumed**; order-processing status endpoint.
- `orders-api` (rest) — **consumed**; order list/get endpoints (the same interface this repo also
  produces via the `api` component).

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/clients/erp.py` — `get_warehouse_stock` (`GET /stock/{sku}`),
  `request_replenishment` (`POST /replenishment`).
- `inventory/clients/order_processing.py` — `get_processing_status`
  (`GET /order-processing/{order_id}`).
- `inventory/clients/orders.py` — `get_order` (`GET /orders/{order_id}`), `list_orders`
  (`GET /orders` with optional status filter).

## Configuration

- `WAREHOUSE_ERP_URL` (required) — ERP base URL.
- `ORDER_PROCESSING_URL` (required) — order-processing base URL.
- `ORDERS_API_URL` (required) — orders API base URL.

## Failure modes

- Each client uses `httpx` and raises on non-2xx responses (`raise_for_status`). Unavailable
  downstream services surface as exceptions at call sites; there is no retry or circuit-breaking.
