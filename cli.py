#!/usr/bin/env python3

import argparse
import pandas as pd

from detector.loader import load_logs
from detector.normalize import normalize_columns
from detector.silence import detect_silence_windows
from detector.scoring import score_silence
from detector.rules import load_rules


def parse_args():
    parser = argparse.ArgumentParser(
        description="Detect log silencing attacks from CSV or JSON logs"
    )
    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Path to CSV or JSON log file"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Load rules
    rules = load_rules()
    score_threshold = rules["silence"]["score_threshold"]

    # Load and normalize logs
    logs = load_logs(args.file)
    logs = normalize_columns(logs)
    logs.sort_values(by=["host", "timestamp"], inplace=True)

    findings = []

    for host, host_logs in logs.groupby("host"):

        silence_windows = detect_silence_windows(
            host_logs,
            rules["silence"]["default_minutes"]
        )

        for window in silence_windows:

            # Focus only on logs around silence window
            window_df = host_logs[
                (host_logs["timestamp"] >= window["start"] - pd.Timedelta(minutes=5)) &
                (host_logs["timestamp"] <= window["end"] + pd.Timedelta(minutes=5))
            ]

            score, confidence, evidence = score_silence(window_df, rules)

            # Ignore suppressed or low-confidence noise
            if confidence == "SUPPRESSED":
                continue

            if score < score_threshold:
                continue

            findings.append({
                "host": host,
                "silence_start": window["start"],
                "silence_end": window["end"],
                "duration_minutes": window["duration"],
                "score": score,
                "confidence": confidence,
                "signals_triggered": len(evidence) - 1,
                "evidence": "; ".join(evidence)
            })

    if not findings:
        print("No log silencing behavior detected.")
        return

    result_df = pd.DataFrame(findings)

    print("\n=== LOG SILENCING DETECTION RESULTS ===\n")
    print(result_df.to_string(index=False))

    result_df.to_csv("output/log_silencing_findings.csv", index=False)
    print("\nResults saved to output/log_silencing_findings.csv")


if __name__ == "__main__":
    main()
