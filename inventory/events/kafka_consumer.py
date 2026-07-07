import os
from confluent_kafka import Consumer, KafkaError

TOPIC = "order-events"

KAFKA_BOOTSTRAP_SERVERS = os.environ["KAFKA_BOOTSTRAP_SERVERS"]


def build_consumer() -> Consumer:
    return Consumer({
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "group.id": "inventory-service",
        "auto.offset.reset": "earliest",
    })


def handle_order_event(event: dict) -> None:
    event_type = event.get("type")
    if event_type == "order.created":
        _on_order_created(event)
    elif event_type == "order.cancelled":
        _on_order_cancelled(event)


def _on_order_created(event: dict) -> None:
    pass


def _on_order_cancelled(event: dict) -> None:
    pass


def run() -> None:
    consumer = build_consumer()
    consumer.subscribe([TOPIC])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() != KafkaError._PARTITION_EOF:
                    raise Exception(msg.error())
                continue
            import json
            handle_order_event(json.loads(msg.value()))
    finally:
        consumer.close()
