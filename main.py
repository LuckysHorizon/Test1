import json
from datetime import datetime


# IMPLEMENT: convert ISO timestamp to milliseconds
def iso_to_millis(timestamp):
    """
    Converts ISO 8601 timestamp to milliseconds.
    Example: "2022-11-11T10:25:44.000Z" -> 1668162344000
    """
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# IMPLEMENT: normalize telemetry message
def normalize_message(message):
    """
    Normalizes the telemetry message into the unified format.
    Converts ISO timestamps to milliseconds when required.
    """
    normalized = message.copy()

    if isinstance(normalized.get("timestamp"), str):
        normalized["timestamp"] = iso_to_millis(normalized["timestamp"])

    return normalized


def main():
    with open("data-1.json") as f1, open("data-2.json") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    normalized_1 = normalize_message(data1)
    normalized_2 = normalize_message(data2)

    print(json.dumps(normalized_1, indent=2))
    print(json.dumps(normalized_2, indent=2))


if __name__ == "__main__":
    main()
