# py-inventory-service fixture notes

This repository is a Panopticon child fixture. Its local interface index is the authoritative
record of the interfaces evidenced by source and configuration.

## Current interface evidence

- `inventory-api` is produced by the OpenAPI contract and FastAPI routes.
- `orders-api` is produced by `inventory/api/orders_routes.py` and consumed by
  `inventory/clients/orders.py` under the same explicit canonical-name hint.
- `warehouse-erp`, `order-processing-status`, `order-events`, and `product-catalog-db` are
  locally recorded consumers with no locally established owner.
- `fulfillment-queue` and `inventory-snapshots` are produced and consumed by this repository.

All entries are LLM-extracted because this fixture has no deterministic parser for these source
patterns. The local index has no cross-repository conflict records.

## Files under extraction

| Source | Interface | Role |
| --- | --- | --- |
| `inventory/api/openapi.yaml`, `inventory/api/routes.py` | `inventory-api` | producer |
| `inventory/api/orders_routes.py` | `orders-api` | producer |
| `inventory/clients/orders.py` | `orders-api` | consumer |
| `inventory/clients/erp.py` | `warehouse-erp` | consumer |
| `inventory/clients/order_processing.py` | `order-processing-status` | consumer |
| `inventory/events/kafka_consumer.py` | `order-events` | consumer |
| `inventory/queue/fulfillment_queue.py` | `fulfillment-queue` | producer and consumer |
| `inventory/storage/snapshots.py` | `inventory-snapshots` | producer and consumer |
| `inventory/db/catalog.py` | `product-catalog-db` | consumer |

See [the generated local interface documentation](docs/interfaces.md) for the rendered index.
