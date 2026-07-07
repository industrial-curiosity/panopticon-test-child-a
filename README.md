# py-inventory-service

Python inventory and fulfillment service. Manages product stock levels, reserves inventory for orders, and publishes fulfillment tasks.

## Repository structure

```text
py-inventory-service/
├── inventory/
│   ├── api/
│   │   ├── openapi.yaml              # REST API contract
│   │   └── routes.py                 # FastAPI route handlers
│   ├── clients/
│   │   ├── orders.py                 # HTTP client for the orders service
│   │   └── erp.py                    # HTTP client for the warehouse ERP
│   ├── events/
│   │   └── kafka_consumer.py         # Kafka consumer for order events
│   ├── queue/
│   │   └── fulfillment_queue.py      # SQS producer and consumer for fulfillment tasks
│   ├── storage/
│   │   └── snapshots.py              # S3 client for daily inventory snapshots
│   └── db/
│       └── catalog.py                # PostgreSQL client for the product catalog
└── pyproject.toml
```

## Interfaces

| Interface | Type | Direction |
| --- | --- | --- |
| Inventory API | REST | Owned here; consumed by order service |
| Inventory snapshots | S3 | Internal — audit and recovery snapshots |
| Fulfillment queue | SQS | Internal — async fulfillment task queue |
| Orders API | REST | External — consumed from order service |
| Order events | Kafka | External — consumed from order service |
| Warehouse ERP | REST | External — third-party on-premise ERP |
| Product catalog DB | Postgres | External — managed RDS instance |

## Environment variables

| Variable | Used by | Description |
| --- | --- | --- |
| `ORDERS_API_URL` | `inventory/clients/orders.py` | Base URL for the orders service REST API |
| `WAREHOUSE_ERP_URL` | `inventory/clients/erp.py` | Base URL for the on-premise warehouse ERP |
| `KAFKA_BOOTSTRAP_SERVERS` | `inventory/events/kafka_consumer.py` | Kafka bootstrap server addresses |
| `FULFILLMENT_QUEUE_URL` | `inventory/queue/fulfillment_queue.py` | SQS queue URL for fulfillment tasks |
| `INVENTORY_SNAPSHOTS_BUCKET` | `inventory/storage/snapshots.py` | S3 bucket name for daily inventory snapshots |
| `CATALOG_DB_DSN` | `inventory/db/catalog.py` | PostgreSQL DSN for the product catalog RDS instance |

## Setup

Requires Python 3.11+.

```bash
pip install -e .
```
