from pathlib import Path
import json, datetime

LOG = Path(__file__).resolve().parents[3] / "data" / "kds_log.jsonl"

def fire_to_kitchen(order_dict: dict) -> dict:
    entry = {
        "ts": datetime.datetime.now().isoformat(),
        "order": order_dict
    }
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    return {"status": "sent", "kds_ref": f"KDS-{order_dict.get('id')}"}
