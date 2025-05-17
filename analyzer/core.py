import re
import json
import requests
from collections import Counter
from pathlib import Path

def geo_lookup(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=2)
        data = response.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "org": data.get("org")
        }
    except Exception as e:
        return {"ip": ip, "error": str(e)}

def parse_auth_log(log_file):
    pattern = re.compile(
        r'(?P<timestamp>\w+\s+\d+\s[\d:]+).*Failed password for (?P<user_type>invalid user\s)?(?P<user>\w+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    )
    results = []
    with open(log_file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                entry = {
                    "timestamp": match.group("timestamp"),
                    "username": match.group("user"),
                    "user_type": "invalid" if match.group("user_type") else "valid",
                    "ip": match.group("ip")
                }
                results.append(entry)
    return results

def generate_report(entries):
    ip_counter = Counter(entry["ip"] for entry in entries)
    unique_ips = {entry["ip"] for entry in entries}
    geo_data = {ip: geo_lookup(ip) for ip in unique_ips}
    report = []
    for entry in entries:
        ip = entry["ip"]
        report.append({
            **entry,
            "attempts": ip_counter[ip],
            "geo": geo_data.get(ip, {})
        })
    return report

def save_report(report, path):
    Path(path).parent.mkdir(exist_ok=True)
    with open(path, 'w') as f:
        json.dump(report, f, indent=2)
