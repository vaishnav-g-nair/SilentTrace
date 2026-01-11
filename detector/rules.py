import yaml
import sys

def load_rules(path="config/rules.yaml"):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load rules: {e}")
        sys.exit(1)
