# panopticon-test-child-a — operations

<!-- panopticon-analysis-scope:start -->
## Panopticon analysis scope

Panopticon excludes illustrative material from interface, dependency, and doc-drift analysis.

### Excluded directories currently in this repository

- None currently detected.

Directories whose exact path component is one of `examples`, `samples`, `fixtures`, `testdata`, `demos`, `scaffolding`, `demo`, `scaffold` are excluded case-insensitively.
Similar production paths, such as `src/sample-service`, remain in scope.

Use `panopticon-ignore file` in one of a file's first five nonblank lines to exclude the whole file. Use `panopticon-ignore declaration` on a declaration line or the line immediately before it to exclude only that declaration.
<!-- panopticon-analysis-scope:end -->

## Running locally

The repository is a Python service package (`py-inventory-service`). There is no application
bootstrap that mounts the FastAPI apps or starts the consumers; the packages are importable and
each module's entry points are callable directly:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
python3 -c "from inventory.events.kafka_consumer import run; run()"   # start the Kafka consumer
python3 -c "from inventory.queue.fulfillment_queue import poll_fulfillment_tasks; ..."  # poll queue
```

Required environment variables must be set before importing the modules that read them at import
time (see Required configuration).

## Testing

This repository contains no test suite.

## Deployment

No deployment pipeline is defined in this repository. Deployment is owned elsewhere or not yet
wired.

## Required configuration

Environment variables read by the modules (names only):

- `WAREHOUSE_ERP_URL` (required) — ERP base URL.
- `ORDER_PROCESSING_URL` (required) — order-processing base URL.
- `ORDERS_API_URL` (required) — orders API base URL.
- `CATALOG_DB_DSN` (required) — catalog PostgreSQL DSN.
- `KAFKA_BOOTSTRAP_SERVERS` (required) — Kafka bootstrap servers.
- `FULFILLMENT_QUEUE_URL` (required) — SQS fulfillment queue URL.
- `INVENTORY_SNAPSHOTS_BUCKET` (required) — S3 inventory snapshot bucket.

## Observability

No logging, metrics, or alerting infrastructure is defined in this repository. Failures surface
as exceptions from the client libraries (httpx, psycopg2, boto3, Confluent Kafka); the Kafka
consumer prints no structured logging and closes its consumer on exit.
