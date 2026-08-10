# storage

## Responsibility

S3 snapshot storage for inventory state (`inventory/storage/snapshots.py`). Uploads, downloads,
and lists daily inventory snapshots on the `inventory-snapshots-bucket`. Deliberately out of
scope: catalog persistence (db), REST surfaces (api).

## Interfaces

- `inventory-snapshots-bucket` (s3) — **produced** (uploads snapshots) and **consumed**
  (downloads snapshots); bucket infrastructure is configured externally via environment.

See [interfaces.md](../interfaces.md).

## Key modules

- `inventory/storage/snapshots.py` — `upload_snapshot` (`PutObject` at
  `snapshots/{date}/inventory.json`), `download_snapshot` (`GetObject`), `list_snapshots`
  (`ListObjectsV2` under `snapshots/`).

## Configuration

- `INVENTORY_SNAPSHOTS_BUCKET` (required) — the S3 bucket holding inventory snapshots.

## Failure modes

- boto3 S3 calls raise on unreachable or misconfigured buckets or missing objects
  (`download_snapshot` on an absent snapshot). No retry is present.
