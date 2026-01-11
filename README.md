🕵️‍♂️ SilentTrace

Tracing the Absence: Detecting Log Silencing Attacks via Behavioral Analysis

“No logs doesn’t mean no attack. Sometimes silence is the signal.”

SilentTrace is a cybersecurity detection tool designed to identify log silencing attacks by analyzing temporal gaps, behavioral indicators, and contextual signals in system logs.

The project provides:

A CLI-based detection engine for analysts and automation

A SOC-style dark-mode web interface for investigation and visualization

SilentTrace simulates how real-world SOC and detection engineering teams hunt attackers who attempt to disable, clear, or evade logging during intrusions.

🚨 Why Log Silencing Matters

Modern attackers don’t just generate malicious events —
they remove visibility.

Common attacker behaviors include:

Stopping logging services (auditd, sysmon, EDR agents)

Clearing Windows / Linux event logs

Modifying logging configurations

Performing malicious actions during periods of log silence

Traditional detections focus on what happened.
SilentTrace focuses on what didn’t happen — and why.

✨ Key Features
🔍 Detection Capabilities

Detects abnormal log gaps per host

Scores silence windows using multiple behavioral signals

Classifies findings into:

Benign Silence

Suspicious Silence

Confirmed Log Silencing

🧠 Behavioral Signals Used

Log clear events (e.g., Windows Event IDs)

Logging / audit configuration changes

Logging agent or service stops

External or suspicious activity during silence windows

Rule-based scoring with confidence levels

🖥️ Interfaces

CLI Tool – for SOC analysts, hunters, and automation pipelines

Flask Web UI – SOC-style dark dashboard with:

Drag & drop log upload

Severity badges (LOW / MEDIUM / HIGH)

Summary stat cards

Timeline visualization of silence windows

🧱 Project Architecture
SilentTrace/
│
├── app.py                 # Flask SOC web dashboard
├── cli.py                 # Command-line detection tool
├── detector/              # Core detection engine
│   ├── loader.py
│   ├── normalize.py
│   ├── silence.py
│   ├── scoring.py
│   ├── rules.py
│   └── timeline.py
│
├── config/
│   └── rules.yaml         # Detection logic & thresholds
│
├── data/
│   ├── sample_logs.csv
│   ├── confirmed_silencing.csv
│   └── benign_silence.csv
│
├── static/                # Dark-mode SOC UI
├── templates/             # Flask HTML templates
├── output/                # Generated results
│
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/vaishnav-g-nair/SilentTrace.git
cd SilentTrace

2️⃣ Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🧪 Usage
▶️ CLI Mode (Analyst / Automation Friendly)
python3 cli.py -f data/confirmed_silencing.csv


CLI Output

Printed detection results

CSV report saved to output/log_silencing_findings.csv

Use cases

SOC investigations

Threat hunting

Detection engineering labs

CI/CD or automation workflows

🌐 Web Mode (SOC Dashboard)
python3 app.py


Open in browser:

http://127.0.0.1:5000

Web UI Highlights

Dark SOC theme (eye-friendly)

Drag & drop log upload

Immediate analysis feedback

Severity-coded results

Timeline visualization of silence windows

🧠 Detection Logic (High Level)

Normalize logs (CSV / JSON)

Group events by host

Detect silence windows exceeding the threshold

Score windows using behavioral rules

Assign confidence levels:

LOW

MEDIUM

HIGH (Confirmed Log Silencing)

Visualize and export findings

Detection logic and thresholds are configurable via:

config/rules.yaml

🎯 Who SilentTrace Is For

SOC Analysts

Threat Hunters

Blue Team Engineers

Detection Engineers

Cybersecurity Students

Anyone learning behavioral detection engineering

🛣️ Roadmap

 Sigma rule export

 MITRE ATT&CK mapping

 Elastic / Splunk ingestion

 Streaming log analysis

 Advanced Gantt-style timeline

 Docker support

📸 Screenshots
<img width="1920" height="792" alt="Screenshot_2026-01-11_01_02_27" src="https://github.com/user-attachments/assets/d010ef99-1473-40c7-bf4d-398bcacbfd7b" />

<img width="1920" height="778" alt="Screenshot_2026-01-11_01_00_21" src="https://github.com/user-attachments/assets/6fbd25dd-b4f0-4f0f-9d2e-2b75f96aba59" />

🧑‍💻 Author

Vaishnav G Nair
Cybersecurity | Threat Detection | Digital Forensics

If this project helped or inspired you, ⭐ the repository and feel free to connect.

⚠️ Disclaimer

SilentTrace is intended for educational and defensive security research purposes only.
Use only on systems you own or have explicit permission to analyze.
