import sys
import pandas as pd


def load_logs(path):
    """
    Load logs from CSV or JSON file.
    Returns a pandas DataFrame.
    """

    try:
        if path.endswith(".csv"):
            df = pd.read_csv(path)
        elif path.endswith(".json"):
            df = pd.read_json(path, lines=True)
        else:
            print("[ERROR] Only CSV and JSON formats are supported")
            sys.exit(1)

    except Exception as e:
        print(f"[ERROR] Failed to load logs: {e}")
        sys.exit(1)

    if df.empty:
        print("[ERROR] Log file is empty")
        sys.exit(1)

    # Normalize column names early
    df.columns = df.columns.str.strip().str.lower()

    return df
