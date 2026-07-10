import json
import os
from datetime import date
import boto3

# panopticon-interface inventory-snapshots
SNAPSHOTS_BUCKET = os.environ["INVENTORY_SNAPSHOTS_BUCKET"]

_s3 = boto3.client("s3")


def upload_snapshot(snapshot_date: date, data: dict) -> str:
    key = f"snapshots/{snapshot_date.isoformat()}/inventory.json"
    _s3.put_object(
        Bucket=SNAPSHOTS_BUCKET,
        Key=key,
        Body=json.dumps(data),
        ContentType="application/json",
    )
    return key


def download_snapshot(snapshot_date: date) -> dict:
    key = f"snapshots/{snapshot_date.isoformat()}/inventory.json"
    response = _s3.get_object(Bucket=SNAPSHOTS_BUCKET, Key=key)
    return json.loads(response["Body"].read())


def list_snapshots() -> list[str]:
    response = _s3.list_objects_v2(Bucket=SNAPSHOTS_BUCKET, Prefix="snapshots/")
    return [obj["Key"] for obj in response.get("Contents", [])]
