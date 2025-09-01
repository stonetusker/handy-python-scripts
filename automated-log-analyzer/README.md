# Automated Log Analyzer Script  
> A Python-based tool to scan system and server logs for errors, warnings, and failures—ideal for DevOps teams needing a quick snapshot of critical log events.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Setup & Configuration](#setup--configuration)
- [Usage](#usage)
- [Requirements](#requirements)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This Python script scans selected system and server log files for patterns like `ERROR`, `WARNING`, `CRITICAL`, `Traceback`, and `Failed`. It generates a clear summary report that makes it easier to monitor, audit, and troubleshoot Linux-based systems.

## How It Works

- Scans specific log files (e.g., `/var/log/syslog`, `/var/log/auth.log`, Apache, and Nginx logs).
- Searches each line for known error patterns.
- Outputs a structured report containing matched log entries, with line numbers and file paths.
- Saves the final summary report to the user’s `~/Downloads` folder to avoid permission issues.

## Setup & Configuration

1. **Clone the repository or download the script.**
2. **Modify script parameters as needed:**  
   - `log_paths`: List of log files to analyze.
   - `patterns`: List of keywords or regex patterns to search for.
   - `output_file`: Default path is `~/Downloads/log-report.txt`.

3. **Permissions:**  
   Ensure the script is executable:
   ```bash
   chmod +x automated-log-analyzer.py
   ```

## Usage
```bash
Run the script manually:
./automated-log-analyzer.py
```
```bash
Or run with Python:
python3 automated-log-analyzer.py
```
- To schedule daily at midnight with cron:
 ```
0 0 * * * /path/to/automated-log-analyzer.py
```

## Requirements
- Python 3.6+
- User must have read access to the specified log files
- User must have Write access to the output location (default: Downloads folder)

## Example Output
 ```
============================================
 Starting Automated Log Analyzer
============================================

user@ubuntu-pc:~/log-analyzer$ chmod +x automated-log-analyzer.py
user@ubuntu-pc:~/log-analyzer$ ./automated-log-analyzer.py
scanning /var/log/syslog...
scanning /var/log/auth.log...
scanning /var/log/apache2/access.log...
scanning /var/log/apache2/error.log...
scanning /var/log/nginx/access.log...
scanning /var/log/nginx/error.log...
analysis complete. report saved to: /home/user/Downloads/log-report.txt

============================================
 Log analysis finished.
============================================
 ```
## Troubleshooting

- **Permission denied reading log file:**  
  Run the script with elevated privileges using `sudo`, or ensure the current user has read access to the specified log files.

- **Report not generated or permission error while writing:**  
  Make sure the `output_file` path (e.g., `~/Downloads/log-report.txt`) is writable. We can change the path to a directory where the user has write permission.

- **No matches found in the report:**  
  Confirm that the log files contain entries matching the defined patterns (e.g., `ERROR`, `WARNING`). You can customize the `patterns[]` list in the script to include additional terms if needed.


## License
[MIT License](LICENSE)























   







