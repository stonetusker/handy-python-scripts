# System Resource Monitor

A simple and lightweight Python script to keep an eye on your system's vital resources. It runs in the background to monitor CPU usage, memory consumption, and disk space. If any of these metrics cross a defined limit, it sends an alert to a specified Slack channel, helping you to proactively manage your system's health.

## Features

-   **CPU Usage Monitoring**: Tracks the percentage of CPU being used.
-   **Memory Usage Monitoring**: Checks the percentage of RAM currently consumed.
-   **Disk Space Monitoring**: Monitors the usage of the primary disk partition.
-   **Slack Integration**: Sends real-time alerts to a configured Slack channel.
-   **Customizable Thresholds**: Easily adjust the alert triggers for CPU, memory, and disk within the script.

## Requirements

-   Python 3.x
-   The `psutil` and `requests` Python libraries.

## Setup and Installation

Follow these steps to get the monitor up and running.

1.  **Clone the Repository**
    First, clone this repository to your local machine.

    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Install Dependencies**
    The script depends on two external libraries. You can install them using pip. It's recommended to do this in a virtual environment.

    ```bash
    pip install psutil requests
    ```

3.  **Configure Slack Webhook**
    For the script to send notifications, you need to provide a Slack Incoming Webhook URL. For security, the script is designed to read this URL from an environment variable. Set it in your terminal before running the script.

    Since you're on Linux, you can use the `export` command:

    ```bash
    export SLACK_WEBHOOK_URL="your_webhook_url_here"
    ```
    -   `export`: This is a shell command that sets an environment variable for the current terminal session.
    -   `SLACK_WEBHOOK_URL`: This is the name of the variable that our Python script looks for.
    -   `"your_webhook_url_here"`: Replace this with the actual URL you got from Slack.

    *Note: If you don't set this variable, alerts will only be printed to the terminal console.*


## How to Use

With the setup complete, you can start the monitoring script.

```bash
python your_script_name.py
```
*(Replace `your_script_name.py` with the actual name of your file.)*

The script will start printing the current resource usage to your terminal and will run indefinitely. To stop the monitor, simply press `Ctrl+C`.


## Configuration

You can easily adjust the alert thresholds and the check frequency by modifying the constants at the top of the Python script.

```python
# --- Configuration ---
# Define the thresholds for CPU, Memory, and Disk usage (in percent)
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 85.0
DISK_THRESHOLD = 90.0
CHECK_INTERVAL = 60 # How often to check the resources (in sec)
