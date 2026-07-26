# py-inventory-service

[panopticon-test-child-a architecture](docs/architecture.md)
[org architecture](https://github.com/industrial-curiosity/panopticon-test/blob/main/docs/architecture.md#panopticon-test-child-a)

Python modules for inventory APIs, upstream clients, order-event consumption, fulfillment tasks,
snapshot storage, and product-catalog access.

## Interfaces

The local Panopticon index documents the inventory REST API, an Orders REST API, a Kafka topic,
an SQS queue, an S3 bucket, a database, and three REST clients. See
[the generated interface index](docs/interfaces.md) for the authoritative local view.

## Configuration

| Variable | Used by |
| --- | --- |
| `ORDERS_API_URL` | `inventory/clients/orders.py` |
| `WAREHOUSE_ERP_URL` | `inventory/clients/erp.py` |
| `ORDER_PROCESSING_URL` | `inventory/clients/order_processing.py` |
| `KAFKA_BOOTSTRAP_SERVERS` | `inventory/events/kafka_consumer.py` |
| `FULFILLMENT_QUEUE_URL` | `inventory/queue/fulfillment_queue.py` |
| `INVENTORY_SNAPSHOTS_BUCKET` | `inventory/storage/snapshots.py` |
| `CATALOG_DB_DSN` | `inventory/db/catalog.py` |

## Setup

Requires Python 3.11+.

```bash
pip install -e .
```
