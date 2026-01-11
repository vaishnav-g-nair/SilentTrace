import sys
from dateutil import parser as dt_parser


def normalize_columns(df):
    """
    Normalize column names and required fields across log sources.
    """

    column_map = {
        "timestamp": ["timestamp", "@timestamp", "timecreated", "log_time", "time"],
        "host": ["host", "hostname", "computer", "device", "machine"],
        "event_id": ["event_id", "eventid", "id"],
        "message": ["message", "msg", "description", "eventdata"],
        "external_activity": ["external_activity"]
    }

    for standard, candidates in column_map.items():
        found = False
        for c in candidates:
            if c in df.columns:
                df[standard] = df[c]
                found = True
                break

        if not found:
            if standard == "external_activity":
                df[standard] = False
            elif standard == "event_id":
                df[standard] = ""
            else:
                print(f"[ERROR] Required column missing: {standard}")
                sys.exit(1)

    # Parse timestamps
    try:
        df["timestamp"] = df["timestamp"].apply(dt_parser.parse)
    except Exception:
        print("[ERROR] Failed to parse timestamp column")
        sys.exit(1)

    # Ensure correct types
    df["message"] = df["message"].astype(str)
    df["event_id"] = df["event_id"].astype(str)

    return df
