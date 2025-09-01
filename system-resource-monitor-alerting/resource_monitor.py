import os
import time
import psutil # main library for fetching system info
import requests
import json

# --- Configuration ---
# Define the thresholds for CPU, Memory, and Disk usage (in percent)
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 85.0
DISK_THRESHOLD = 90.0
CHECK_INTERVAL = 60 # How often to check the resources (in sec)

# The slack Webhook URL is now fetched from an environment variable for security.
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/"

def send_alert(message):
    if not SLACK_WEBHOOK_URL:
        print("ALERT!, Slack not Configured)", message)
        return 
    
    try:
        payload = {'text' : message}
        request.post(SLACK_WEBHOOK_URL, json=payload)
        print(f"slack notification sent : {message}")

    except Exception as e:
        print(f"Error sending Notification: {e}")

def check_cpu_usage():
    """ Checks the current CPU usage and sends an alert if it exceeds the threshold. """
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {usage}%")

    if usage > CPU_THRESHOLD:
        send_alert(f'High CPU Alert! Usage is at {usage}%')

def check_memory_usage():
    """ Checks the current memory usage and sends an alert if it exceeds the threshold. """
    memory = psutil.virtual_memory()
    usage = memory.percent
    print(f"Memory Usage: {usage}%")

    if usage > MEMORY_THRESHOLD:
        send_alert(f'High Memory Alert! Usage is at {usage}%')

def check_disk_usage():
    """ Checks the current disk usage and sends an alert if it exceeds the threshold. """
    disk = psutil.disk_usage('/')
    usage = disk.percent
    print(f"Disk Usage: {usage}%")

    if usage > DISK_THRESHOLD:
        send_alert(f'Low Disk Space Alert! Usage is at {usage}%')


def main():
    """ The main function to run the monitoring loop. """
    print("Starting System Resource Monitoring...")
    try:
        while True:
            print("-" * 30)
            check_cpu_usage()
            check_memory_usage()
            check_disk_usage()
            print(f"--- Waiting for {CHECK_INTERVAL} seconds ---")
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n Monitoring stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()




