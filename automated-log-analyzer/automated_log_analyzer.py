#!/usr/bin/env python3

#######################################################################
# Automated Log Analyzer
#
# Scans system and server logs (syslog, auth, Apache, Nginx) for
# patterns such as ERROR, WARNING, CRITICAL, etc., and generates
# a readable summary report.
#
# Location : ~/log-analyzer/automated-log-analyzer.py
# Output   : ~/Downloads/log-report.txt
#######################################################################

import os
import re
from datetime import datetime

# === Configuration ===
log_paths = [
    "/var/log/syslog",
    "/var/log/auth.log",
    "/var/log/apache2/access.log",
    "/var/log/apache2/error.log",
    "/var/log/nginx/access.log",
    "/var/log/nginx/error.log"
]

# Save the report in Downloads to avoid permission issues
output_file = os.path.expanduser("~/Downloads/log-report.txt")

# Patterns to search for in logs
patterns = [
    r"\bERROR\b",
    r"\bWARNING\b",
    r"\bCRITICAL\b",
    r"Traceback",
    r"\bFailed\b"
]

# === Function: Analyze Single Log File ===
def analyze_log_file(file_path):
    findings = []
    if not os.path.exists(file_path):
        return findings

    try:
        with open(file_path, 'r', errors='ignore') as file:
            for line_number, line in enumerate(file, 1):
                for pattern in patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        findings.append((file_path, line_number, line.strip()))
                        break
    except PermissionError:
        print(f"Permission denied for {file_path}")
    return findings

# === Function: Write Report ===
def write_report(findings):
    try:
        with open(output_file, 'w') as file:
            file.write(f"Log Analysis Report - {datetime.now()}\n")
            file.write("=" * 60 + "\n\n")
            for file_path, line_number, line in findings:
                file.write(f"{file_path} [line {line_number}]: {line}\n")
        print(f"\n Analysis complete. Report saved to: {output_file}")
    except PermissionError:
        print(f"❌ Permission denied: Unable to write report to {output_file}")

# === Main Logic ===
def main():
    all_findings = []

    print("============================================")
    print(" Starting Automated Log Analyzer")
    print("============================================\n")

    for path in log_paths:
        print(f"Scanning: {path}")
        findings = analyze_log_file(path)
        all_findings.extend(findings)

    write_report(all_findings)

    print("\n============================================")
    print(" Log analysis finished.")
    print("============================================")

# === Entry Point ===
if __name__ == "__main__":
    main()

