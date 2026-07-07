import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventory API", version="1.0.0")


class InventoryItem(BaseModel):
    sku: str
    quantity_available: int
    quantity_reserved: int


class InventoryUpdate(BaseModel):
    quantity_available: int


class ReservationRequest(BaseModel):
    order_id: str
    items: list[dict]


class ReleaseRequest(BaseModel):
    reservation_id: str


@app.get("/inventory")
def list_inventory(limit: int = 100, offset: int = 0):
    return {"items": [], "total": 0}


@app.get("/inventory/{sku}")
def get_inventory_item(sku: str):
    raise HTTPException(status_code=404, detail="SKU not found")


@app.put("/inventory/{sku}")
def update_inventory_item(sku: str, body: InventoryUpdate):
    return {"sku": sku, "quantity_available": body.quantity_available, "quantity_reserved": 0}


@app.post("/inventory/reserve")
def reserve_inventory(body: ReservationRequest):
    return {"reservation_id": "res-placeholder", "order_id": body.order_id, "status": "confirmed"}


@app.post("/inventory/release")
def release_inventory(body: ReleaseRequest):
    return {"status": "released"}
