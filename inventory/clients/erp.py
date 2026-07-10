import os
import httpx

# panopticon-interface warehouse-erp
ERP_BASE_URL = os.environ["WAREHOUSE_ERP_URL"]


def get_warehouse_stock(sku: str) -> dict:
    with httpx.Client(base_url=ERP_BASE_URL) as client:
        response = client.get(f"/stock/{sku}")
        response.raise_for_status()
        return response.json()


def request_replenishment(sku: str, quantity: int) -> dict:
    with httpx.Client(base_url=ERP_BASE_URL) as client:
        response = client.post("/replenishment", json={"sku": sku, "quantity": quantity})
        response.raise_for_status()
        return response.json()
