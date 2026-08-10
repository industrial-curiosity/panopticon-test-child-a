from fastapi import FastAPI

# panopticon-interface orders-api
app = FastAPI(title="Orders API (inventory-owned)", version="0.1.0")


@app.get("/orders")
def list_orders(status: str | None = None):
    return {"orders": []}


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return {"order_id": order_id, "status": "unknown"}
