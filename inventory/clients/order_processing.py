import os
import httpx

# panopticon-interface order-processing-queue
ORDER_PROCESSING_BASE_URL = os.environ["ORDER_PROCESSING_URL"]


def get_processing_status(order_id: str) -> dict:
    with httpx.Client(base_url=ORDER_PROCESSING_BASE_URL) as client:
        response = client.get(f"/order-processing/{order_id}")
        response.raise_for_status()
        return response.json()
