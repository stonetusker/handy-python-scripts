import json
import logging
import time
import subprocess
import os
from datetime import datetime

# --- Best Practice: Configuration over Hardcoding ---
# We store our settings in a separate config file.
# This makes the script flexible and easy to update without changing the code.
CONFIG_FILE = 'config.json'

def load_config():
    """
    Loads the configuration from a JSON file.
    This helps separate our settings from our code logic.
    """
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file '{CONFIG_FILE}' not found. Please create it.")
        # In a real script, you might create a default one here.
        exit(1)
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from '{CONFIG_FILE}'. Please check its format.")
        exit(1)

def setup_logging(log_file):
    """
    --- Best Practice: Clear & Verbose Logging ---
    Configures a centralized logger to write to both the console and a file.
    Good logging is crucial for auditing and debugging what the script does.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler() # To also print to console
        ]
    )

def check_for_alerts(monitoring_target):
    """
    Simulates checking a log file or an API for alerts.
    In a real-world scenario, this function would connect to our monitoring system.
    For this example, it just reads a text file.
    """
    logging.info(f"Checking for alerts in '{monitoring_target}'...")
    try:
        with open(monitoring_target, 'r') as f:
            # We only care about the last few lines to be efficient
            lines = f.readlines()
            last_lines = lines[-5:] # Check the last 5 lines for recent errors
            for line in last_lines:
                if "ERROR" in line:
                    # We found an error! Return the line as the alert details.
                    logging.warning(f"Alert detected: {line.strip()}")
                    return line.strip()
    except FileNotFoundError:
        logging.error(f"Monitoring target '{monitoring_target}' not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while checking for alerts: {e}")
    
    logging.info("No new alerts found.")
    return None

def run_recovery_action(action_command):
    """
    --- Best Practice: Modularity & Idempotency ---
    Executes a predefined recovery action using a shell command.
    The command should be idempotent (running it multiple times has the same effect).
    For example, `systemctl restart my-service` is idempotent.
    """
    logging.info(f"Executing recovery action: '{action_command}'")
    try:
        # We use subprocess to run shell commands from Python.
        # 'shell=True' can be a security risk if the command comes from user input,
        # but here it's safe as it's from our trusted config file.
        # For this example, we'll just echo a message.
        # In a real scenario, this could be: "sudo systemctl restart nginx"
        result = subprocess.run(
            action_command,
            shell=True,
            check=True, # This will raise an exception if the command fails (returns non-zero exit code)
            capture_output=True,
            text=True
        )
        logging.info(f"Recovery action successful. Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Recovery action failed! Command: '{e.cmd}', Exit Code: {e.returncode}")
        logging.error(f"Stderr: {e.stderr.strip()}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred during recovery action: {e}")
        return False

def escalate_incident(alert_details, escalation_contact):
    """
    Simulates escalating the incident to a human.
    In a real system, this would send an email, a Slack message, or a PagerDuty alert.
    """
    message = f"Automated recovery failed for alert: '{alert_details}'. Manual intervention required!"
    logging.critical("ESCALATING INCIDENT!")
    logging.critical(message)
    # Simulate sending a notification
    print(f"\n--- SIMULATING ESCALATION to {escalation_contact} ---")
    print(message)
    print("--------------------------------------------------\n")


def main():
    """
    The main function that orchestrates the incident response workflow.
    """
    # 1. Load configuration and set up logging
    config = load_config()
    setup_logging(config.get('log_file', 'incident_response.log'))
    logging.info("--- Automated Incident Response Script Started ---")

    monitoring_target = config.get('monitoring_target')
    recovery_action = config.get('recovery_action')
    escalation_contact = config.get('escalation_contact')
    check_interval_seconds = config.get('check_interval_seconds', 60)

    # 2. Main loop: Check for alerts periodically
    try:
        while True:
            alert = check_for_alerts(monitoring_target)
            
            if alert:
                # 3. An alert was found, trigger the recovery action
                success = run_recovery_action(recovery_action)
                
                if not success:
                    # 4. The recovery action failed, escalate to a human
                    escalate_incident(alert, escalation_contact)
            
            logging.info(f"Waiting for {check_interval_seconds} seconds before next check.")
            time.sleep(check_interval_seconds)

    except KeyboardInterrupt:
        logging.info("--- Script stopped by user. ---")
    except Exception as e:
        logging.error(f"An unhandled exception occurred in the main loop: {e}")

if __name__ == "__main__":
    # This standard Python construct ensures the main() function is called
    # only when the script is executed directly.
    main()


