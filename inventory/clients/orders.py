import os
import httpx

# panopticon-interface orders-api
ORDERS_BASE_URL = os.environ["ORDERS_API_URL"]


def get_order(order_id: str) -> dict:
    with httpx.Client(base_url=ORDERS_BASE_URL) as client:
        response = client.get(f"/orders/{order_id}")
        response.raise_for_status()
        return response.json()


def list_orders(status: str | None = None) -> list[dict]:
    params = {}
    if status:
        params["status"] = status
    with httpx.Client(base_url=ORDERS_BASE_URL) as client:
        response = client.get("/orders", params=params)
        response.raise_for_status()
        return response.json().get("orders", [])
