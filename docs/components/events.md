# events

## Responsibility

Background Kafka consumer for order lifecycle events (`inventory/events/kafka_consumer.py`).
Subscribes to the `order-events` topic and dispatches `order.created` and `order.cancelled`
events to handler functions. Deliberately out of scope: fulfillment queue (queue), REST surfaces
(api).

## Interfaces

- `order-events` (kafka) — **consumed**; the order lifecycle topic.

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/events/kafka_consumer.py` — `build_consumer` (Confluent Consumer, group
  `inventory-service`, `earliest` reset), `handle_order_event` (type dispatch),
  `run` (poll loop, JSON decode, `_PARTITION_EOF` tolerated, consumer closed on exit).

## Configuration

- `KAFKA_BOOTSTRAP_SERVERS` (required) — Kafka bootstrap servers.

## Failure modes

- Poll errors other than `_PARTITION_EOF` raise and terminate the `run` loop; the consumer is
  closed in `finally`. Event handlers are stubs (`pass`) — events are acknowledged by offset
  advance with no processing currently performed.
