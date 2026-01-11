from flask import Flask, render_template, request
import os
import pandas as pd

from detector.loader import load_logs
from detector.normalize import normalize_columns
from detector.silence import detect_silence_windows
from detector.scoring import score_silence
from detector.rules import load_rules

app = Flask(__name__)

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files.get("logfile")
        if uploaded_file and uploaded_file.filename.endswith((".csv", ".json")):
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            results_df, timeline = process_logs(filepath)

            if results_df.empty:
                return render_template("result.html", message="No log silencing behavior detected.")
            else:
                # Stats
                total_gaps = len(results_df)
                longest_silence = results_df["duration_minutes"].max()
                max_severity = results_df["confidence"].max()

                # Convert DataFrame to HTML with badges
                def highlight(row):
                    cls = "high-confidence" if row["confidence"]=="HIGH" else ""
                    conf_badge = f'<span class="badge {row["confidence"].lower()}">{row["confidence"]}</span>'
                    row["confidence"] = conf_badge
                    return [f'<td>{v}</td>' for v in row]

                table_html = results_df.to_html(classes="table", index=False, escape=False)

                return render_template(
                    "result.html",
                    table=table_html,
                    total_gaps=total_gaps,
                    longest_silence=longest_silence,
                    max_severity=max_severity,
                    timeline=timeline
                )
        else:
            return render_template("index.html", error="Please upload a CSV or JSON file.")
    return render_template("index.html")


def process_logs(file_path):
    rules = load_rules()
    score_threshold = rules["silence"]["score_threshold"]

    logs = load_logs(file_path)
    logs = normalize_columns(logs)
    logs.sort_values(by=["host","timestamp"], inplace=True)

    findings = []

    for host, host_logs in logs.groupby("host"):
        silence_windows = detect_silence_windows(host_logs, rules["silence"]["default_minutes"])

        for window in silence_windows:
            window_df = host_logs[
                (host_logs["timestamp"] >= window["start"] - pd.Timedelta(minutes=5)) &
                (host_logs["timestamp"] <= window["end"] + pd.Timedelta(minutes=5))
            ]
            score, confidence, evidence = score_silence(window_df, rules)

            if confidence != "SUPPRESSED" and score >= score_threshold:
                findings.append({
                    "host": host,
                    "silence_start": window["start"],
                    "silence_end": window["end"],
                    "duration_minutes": window["duration"],
                    "score": score,
                    "confidence": confidence,
                    "evidence": "; ".join(evidence)
                })

    df = pd.DataFrame(findings)

    # Timeline visualization
    timeline = []
    if not df.empty:
        total_duration = df["duration_minutes"].max()
        for _, row in df.iterrows():
            width = min(100, (row["duration_minutes"] / total_duration) * 100)
            color = "#ff4d4d" if row["confidence"]=="HIGH" else "#00ff41"
            timeline.append({"width": width, "color": color, "label": f'{row["host"]}: {row["duration_minutes"]} mins'})

    return df, timeline


if __name__ == "__main__":
    app.run(debug=True)
