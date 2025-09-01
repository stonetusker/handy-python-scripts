import time
import requests
import psycopg2

# --- Configrations ---

NGINX_URL = "http://127.0.0.1:80"

POSTGRES_PARAMS = {
    'host' : 'localhost',
    'port' : '5432',
    'dbname' : 'postgres',
    'user' : 'db_user',  # <- CHANGE THIS
    'password' : 'db_password' # <- CHANGE THIS

}

SLACK_WEBHOOK_URL = "https://hooks.slack.com/sercices/xxxxxxxx" # <- CHANGE THIS

CHECK_INTERVAL_SEC = 30 # CHECK EVERY 30 SEC

# --- Nodification Function ---

def send_slack_nodification(message):
    """ Sends a message to your Slack channel. """
    try:
        # the payload is a simple JSON object with the message text. 
        payload = {'test' : message}
        requests.post(SLACK_WEBHOOK_URL, json=payload)
        print("slack message send successfully.")

    except Exception as e:
        #if sending fails, we print an error to the console.
        print(f'Error sending slack nodification: {e}')

# --- Health Check Functions ---
# --- Checking Nginx Server ---

def check_nginx():
    """ Checks if the Nginx web server is responding correctly. """
    try:
        # We send a GET request and wait a max of 5 sec for a response.
        response = requests.get(NGINX_URL, timeout=5)
        # A status code of 200 means "OK". If we get that, the server is up
        if response.status_code == 200:
            print("Nginx is UP.")
        else:
            # If we get any other status code (like 404 or 500), it's a problem.
            print(f'Nginx is DOWN. Status code: {response.status_code}')
            send_slack_nodification(f"ALERT: Nginx is down! Status Code: {response.status_code}")
            
    except Exception as e:
        # this except block catches error like commection failures or timeouts.
        print(f'Nginx is DOWN. Error: {e}')
        send_slack_nodification(f"Alert: Nginx is down! Could not connect.")

# --- Checking Postgres Server ---

def check_postgres():
    pass

# --- main Loop ---

if __name__ == "__main__":

    print("Starting simple health checker...")
    # This is an infinite loop that runs our checks forever.
    while True:
        print("---- Running new check Cycle ----")
        check_nginx()
        check_postgres()
        print(f" --- Checks complete. Waiting for {CHECK_INTERVAL_SEC} second. --- ")
        # time.sleep() pauses the script for the specified number of seconds.
        time.sleep(CHECK_INTERVAL_SEC)
