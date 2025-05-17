import argparse
from analyzer.core import parse_auth_log, generate_report, save_report

def main():
    parser = argparse.ArgumentParser(description="Analyze SSH auth.log files")
    parser.add_argument("logfile", help="Path to auth.log file")
    parser.add_argument("-o", "--output", default="report/suspicious_activity.json", help="Output path")
    args = parser.parse_args()

    entries = parse_auth_log(args.logfile)
    report = generate_report(entries)
    save_report(report, args.output)

    print(f"Report written to {args.output}")
