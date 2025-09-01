# SSL Certificate Expiry Checker (`ssl_expiry_checker.py`)

This Python script monitors SSL/TLS certificates for a defined list of websites. It sends notifications to a Slack channel if a certificate is about to expire or has already expired, helping to avoid disruptions caused by missed renewals.

### Features
- Monitors multiple websites for SSL certificate expiration status.  
- Determines the number of days remaining before a certificate expires.  
- Sends alerts for expired certificates.  
- Issues warnings when certificates are approaching an expiration threshold (e.g., within 30 days).  
- Supports configurable intervals for automated checks (default: every 24 hours).  

### Prerequisites
- Python 3.6+  
- `requests` library  

### Setup and Configuration

**1. Create a Virtual Environment**  
Using a virtual environment is recommended to keep dependencies isolated.

Create a virtual environment directory named .venv
python -m venv .venv

Activate the virtual environment
source .venv/bin/activate


**2. Install Dependencies**  
With the virtual environment enabled, install the required package:

pip install requests

**3. Configure the Script**  
Edit `ssl_expiry_checker.py` to update the configuration parameters:

- `WEBSITES_TO_CHECK`: List of domains to monitor (e.g., `["example.com", "github.com"]`).  
- `EXPIRY_THRESHOLD_DAYS`: Days before expiry when warnings should be sent (e.g., `30`).  
- `SLACK_WEBHOOK_URL`: Your Slack incoming webhook URL.  
- `CHECK_INTERVAL_SECONDS`: Frequency of checks (default: `86400` seconds = 24 hours).  

### Usage
To run the script (inside the virtual environment):

python ssl_expiry_checker.py


The script performs a check immediately and then waits for the configured interval before running again. Notifications are sent to Slack for any certificates nearing expiry or already expired.  

To stop the script, use `Ctrl+C`.
