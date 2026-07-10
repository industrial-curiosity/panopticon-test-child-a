import json
import os
import boto3

# panopticon-interface fulfillment-queue
QUEUE_URL = os.environ["FULFILLMENT_QUEUE_URL"]

_sqs = boto3.client("sqs")


def enqueue_fulfillment_task(order_id: str, items: list[dict]) -> str:
    message = {"order_id": order_id, "items": items}
    response = _sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message),
    )
    return response["MessageId"]


def poll_fulfillment_tasks(max_messages: int = 10) -> list[dict]:
    response = _sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=max_messages,
        WaitTimeSeconds=5,
    )
    return response.get("Messages", [])


def delete_fulfillment_task(receipt_handle: str) -> None:
    _sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=receipt_handle)
