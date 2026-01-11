# 🕵️‍♂️ SilentTrace  
### Tracing the Absence: Detecting Log Silencing Attacks via Behavioral Analysis

> _“No logs doesn’t mean no attack. Sometimes silence is the signal.”_

**SilentTrace** is a cybersecurity detection tool designed to identify **log silencing attacks** by analyzing **temporal gaps**, **behavioral indicators**, and **contextual signals** in system logs.

The project provides:
- A **CLI-based detection engine** for analysts and automation
- A **SOC-style dark-mode web interface** for investigation and visualization

SilentTrace simulates how **real-world SOC and detection engineering teams** hunt attackers who attempt to **disable, clear, or evade logging** during intrusions.

---

## 🚨 Why Log Silencing Matters

Modern attackers don’t just generate malicious events —  
**they remove visibility**.

Common attacker behaviors include:
- Stopping logging services (`auditd`, `sysmon`, EDR agents)
- Clearing Windows / Linux event logs
- Modifying logging configurations
- Performing malicious actions **during periods of log silence**

Traditional detections focus on **what happened**.  
**SilentTrace focuses on what didn’t happen — and why.**

---

## ✨ Key Features

### 🔍 Detection Capabilities
- Detects **abnormal log gaps** per host
- Scores silence windows using **multiple behavioral signals**
- Classifies findings into:
  - **Benign Silence**
  - **Suspicious Silence**
  - **Confirmed Log Silencing**

### 🧠 Behavioral Signals Used
- Log clear events (e.g., Windows Event IDs)
- Logging / audit configuration changes
- Logging agent or service stops
- External or suspicious activity during silence windows
- Rule-based scoring with confidence levels

### 🖥️ Interfaces
- **CLI Tool** – for SOC analysts, hunters, and automation pipelines
- **Flask Web UI** – SOC-style dark dashboard featuring:
  - Drag & drop log upload
  - Severity badges (**LOW / MEDIUM / HIGH**)
  - Summary stat cards
  - Timeline visualization of silence windows

---

## 
---

📸 Screenshots
<img width="1920" height="792" alt="SilentTrace Dashboard" src="https://github.com/user-attachments/assets/d010ef99-1473-40c7-bf4d-398bcacbfd7b" /> <img width="1920" height="778" alt="SilentTrace Detection Results" src="https://github.com/user-attachments/assets/6fbd25dd-b4f0-4f0f-9d2e-2b75f96aba59" />

🧑‍💻 Author

Vaishnav G Nair

  Cybersecurity | Threat Detection | Digital Forensics

If this project helped or inspired you, ⭐ the repository and feel free to connect.

⚠️ Disclaimer

SilentTrace is intended for educational and defensive security research purposes only.
Use only on systems you own or have explicit permission to analyze.

🔥 Final Note

SilentTrace focuses on an under-detected attack technique — log silencing.
It demonstrates behavioral detection thinking, not signature-based detection.




