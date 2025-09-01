# Service Health Checker

A simple Python script to monitor the health of your key services. It periodically checks if Nginx and PostgreSQL are online and responsive. If a service is found to be down, it sends an immediate notification to a specified Slack channel.

It's a lightweight tool designed to help you catch infrastructure issues before they impact your users.


### How It Works

* **Nginx Check**: Sends an HTTP request to your Nginx URL and verifies it returns a successful status code (2xx).
* **PostgreSQL Check**: Attempts to establish a connection to your PostgreSQL database to confirm it's online and accepting connections.
* **Slack Notifications**: Pushes an alert to your designated Slack channel via an incoming webhook if any check fails.
* **Configurable Interval**: Allows you to define the delay in seconds between each health check cycle.


### Prerequisites

* Python 3.6+
* The `requests` library
* The `psycopg2-binary` library


### Setup

**1. Create a Virtual Environment**

Using a virtual environment is best practice for managing project dependencies. Since you're on Arch Linux, the process is straightforward.

```bash
# Creates a new directory named '.venv' to house the virtual environment's files.
# The '-m venv' flag invokes Python's built-in 'venv' module to handle the creation.
python -m venv .venv
# The 'source' command executes the activation script within the current shell session.
# This prepends the virtual environment's 'bin' directory to your $PATH, ensuring
# that commands like 'python' and 'pip' use the versions inside '.venv'.
source .venv/bin/activate
```
**2. Install Dependencies**

With the virtual environment active, install the necessary packages.

```bash

# Use pip to install the required libraries from the Python Package Index.
# 'requests' is used for sending HTTP requests to the Nginx server.
# 'psycopg2-binary' is the PostgreSQL database adapter for Python.
pip install requests psycopg2-binary
```

**3. Configure the Script**

* Before running, you need to edit health_checker.py and set your configuration variables, which are located at the top of the file:

* NGINX_URL: The complete URL of your Nginx server (e.g., "http://localhost").

* POSTGRES_PARAMS: A dictionary with your PostgreSQL connection details (host, dbname, user, password).

* SLACK_WEBHOOK_URL: The incoming webhook URL provided by Slack for your channel.

* CHECK_INTERVAL_SECONDS: The number of seconds the script will wait between checks.

Running the Script
With your environment activated and the configuration set, run the script from your terminal.

```Bash

# Executes the script using the Python interpreter from your active virtual environment.
python health_checker.py
```

The script will begin the monitoring loop, printing status updates to your console and sending Slack alerts upon failure.

To stop the process, press Ctrl+C.
