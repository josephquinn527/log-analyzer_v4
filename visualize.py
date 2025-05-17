import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load JSON report
with open("report/suspicious_activity.json", "r") as f:
    data = json.load(f)

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Plot 1: Top IPs by number of attempts
top_ips = df.groupby("ip").size().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_ips.plot(kind="bar")
plt.title("Top 10 Attacking IPs")
plt.xlabel("IP Address")
plt.ylabel("Number of Failed Logins")
plt.xticks(rotation=45)
plt.tight_layout()
Path("report").mkdir(exist_ok=True)
plt.savefig("report/top_ips.png")
plt.show()

# Plot 2: Targeted usernames
top_users = df.groupby("username").size().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_users.plot(kind="bar", color="orange")
plt.title("Most Targeted Usernames")
plt.xlabel("Username")
plt.ylabel("Number of Failed Logins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("report/top_usernames.png")
plt.show()
