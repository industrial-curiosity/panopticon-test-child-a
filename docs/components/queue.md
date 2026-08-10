# queue

## Responsibility

SQS fulfillment-task queue usage (`inventory/queue/fulfillment_queue.py`): enqueues fulfillment
tasks (`order_id`, `items`) and polls/acknowledges them on the `fulfillment-queue`. Deliberately
out of scope: Kafka consumption (events), REST surfaces (api).

## Interfaces

- `fulfillment-queue` (sqs) — **produced** (enqueues tasks) and **consumed** (polls and deletes
  tasks); queue infrastructure is configured externally via environment.

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/queue/fulfillment_queue.py` — `enqueue_fulfillment_task` (`SendMessage`),
  `poll_fulfillment_tasks` (`ReceiveMessage`, 5 s wait), `delete_fulfillment_task`
  (`DeleteMessage`).

## Configuration

- `FULFILLMENT_QUEUE_URL` (required) — the SQS queue URL.

## Failure modes

- boto3 SQS calls raise on unreachable or misconfigured queues. The module holds a module-level
  SQS client; no retry or dead-letter handling is present.
