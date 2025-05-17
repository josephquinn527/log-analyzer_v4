# 🔐 log-analyzer_v4

A Python-based CLI and Streamlit dashboard that analyzes Linux `auth.log` files to detect suspicious SSH activity. Enriches attacker IPs with GeoIP info, generates JSON reports, and visualizes trends in an interactive browser-based dashboard.

---

## 🚀 Features

- 🔎 Parse failed and successful SSH login attempts  
- 🌐 GeoIP enrichment using [ipinfo.io](https://ipinfo.io)  
- 📊 Interactive dashboard via Streamlit  
- 📁 JSON output reports  
- 🧰 CLI tools: `loganalyze` and `sshdashboard`  
- ⚙️ Installable Python package (`pip install .`)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/log-analyzer_v4.git
cd log-analyzer_v4
pip install .
Make sure your Python Scripts directory is on your system PATH so that loganalyze and sshdashboard are recognized.

🧪 Usage
Generate JSON Report
bash
Copy
Edit
loganalyze sample_logs/auth.log -o report/suspicious_activity.json
Launch Dashboard
bash
Copy
Edit
sshdashboard
This will open the interactive dashboard in your default browser.

🖥 Dashboard Features
Filter by date
View top attacking IPs
View most targeted usernames
Browse raw failed attempt data

📂 Project Structure
graphql
Copy
Edit
log-analyzer_v4/
├── analyzer/
│   ├── cli.py              # CLI entry point
│   ├── core.py             # Parsing & GeoIP logic
│   ├── dashboard.py        # Streamlit UI
│   └── launch_dashboard.py # CLI launcher for Streamlit
├── sample_logs/
│   └── auth.log            # Sample log data
├── report/
│   └── suspicious_activity.json
├── requirements.txt
├── setup.cfg
├── pyproject.toml
└── README.md

📄 Sample Output (JSON)
json
Copy
Edit
[
  {
    "timestamp": "Jan 10 06:31:55",
    "username": "admin",
    "user_type": "invalid",
    "ip": "203.0.113.42",
    "attempts": 3,
    "geo": {
      "ip": "203.0.113.42",
      "country": "US",
      "org": "Cloudflare, Inc."
    }
  }
]

✅ Requirements
Install via pip install -r requirements.txt:
txt
Copy
Edit
requests
pandas
matplotlib
streamlit

🧠 Future Ideas
Add IP reputation scoring
Integrate alerting (email / Slack)
Export charts to PDF
Provide a Docker container
Support additional log formats (e.g., journalctl)

🛡 License
MIT © Joseph Quinn

📎 Related Links
Streamlit: https://streamlit.io

ipinfo.io: https://ipinfo.io

Linux auth.log: https://help.ubuntu.com/community/LinuxLogFiles

yaml
Copy
Edit

---

## `requirements.txt`

```txt
requests
pandas
matplotlib
streamlit