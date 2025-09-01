import ssl
import socket
import datetime
import time
import requests

# --- Configuration ---

# A list of websites we want to monitor

Websites = [
    'google.com',
    'github.com',
    'expired.badssl.com' # <- expired cert for testing
]

# send warning if the cert expires in this many days or less
EXPIRY_THRESHOLD_DAYS = 30     

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/sercices/xxxxxxxxxxxx'

# How often to run the checks, in seconds. (86400 sec = 24 hours)
CHECK_INTERVAL_SEC = 86400

# --- Nodification Functions ---
def send_slack_notification(message):
    """ sends a message to your slack channel. """
    if not SLACK_WEBHOOK_URL or "xxxxxxxxxxxx" in SLACK_WEBHOOK_URL:
        print('Slack webhook URL not configured. Skipping notification')
        return
    try:
        payload = {'text' : message}
        request.post(SLACK_WEBHOOK_URL, json=payload)
        print(f"slack notification sent: {message}")
        
    except Exception as e:
        print(f"Error sending Notification: {e}")

# --- Certificate Check Function ---
def get_ssl_expiry_days(hostname):
    """
    Connects to a host and returns the number of days until its SSL cert expires.
    """
    # SSl context helps manage certifications, protocols, and other SSL settings.
    context = ssl.create_default_context()

    try:
        #We wrap a standard socket in our SSL context.
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock,server_hostname=hostname) as ssock:
                # getpeercert() returns the certificate from the other side of the connection
                cert = ssock.getpeercert()

                # the expiry date is in the 'notAfter' field.
                expiry_date_str = cert['notAfter']

                # The date string can have variable spaces (e.g., 'Feb  5' vs 'Feb 15').
                # We split the string by spaces and rejoin with a single space to create a consistent format.
                expiry_date_str_normalized = " ".join(expiry_date_str.split())

                # The format is now consistently 'Mon Day HH:MM:SS YYYY TZN'.
                # We parse up to the year and ignore the timezone name ('%Z'), as it can be unreliable.
                expiry_date = datetime.datetime.strptime(expiry_date_str_normalized, '%b %d %H:%M:%S %Y %Z')

                # Calculate the difference between now and the expiry date.
                days_remaining = (expiry_date - datetime.datetime.now()).days
                return days_remaining, None # Return days and no error
    
    except ssl.SSLCertVerificationError:
        # This specific error is often because the cert is already expired.
        return 0, f"Certificate verification failed for {hostname}. It might be expired or self-signed."
    except Exception as e:
        # Catch other errors like connection failures.
        return -1, f"Could not connect to {hostname} or get certificate. Error: {e}"

# --- Main Loop ---

if __name__ == "__main__":
    print("Starting SSL Expiry Checker...")
    while True:
        print(f"\n --- Running new check cycle at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

        for site in Websites:
            days_left, error = get_ssl_expiry_days(site)

            if error:
                print(error)
                send_slack_notification(f"ALERT: Could not check SSL for `{site}`. Reason: {error}")
                continue
            if days_left <= 0:
                message = f"ALERT: The SSL certificate for {site} has EXPIRED!"
                print(message)
                send_slack_notification(message)
            elif days_left < EXPIRY_THRESHOLD_DAYS:
                message = f"WARNING! : Rhe SSl certificate for {site} expires in {days_left} days"
                print(message)
                send_slack_notification(message)
            else:
                print(f"OK! : The SSL certificate for {site} is valid {days_left} more days.")

        print(f"--- Checks complete. Waiting for {CHECK_INTERVAL_SEC / 3600} hours. ---")

        time.sleep(CHECK_INTERVAL_SEC)

