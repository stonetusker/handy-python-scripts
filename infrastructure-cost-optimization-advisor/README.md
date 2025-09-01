# Infrastructure Cost Optimization Advisor

A Python script that analyzes your cloud usage from a CSV file to find underutilized resources and suggest ways to save money. It's a straightforward tool for DevOps and FinOps teams looking to trim their cloud bill.


## Table of Contents

- [What It Does](#what-it-does)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Requirements](#requirements)
- [Example Output](#example-output)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contact](#contact)


## What It Does

This script helps you get a handle on your cloud spending by analyzing usage data from a simple CSV file. It automatically flags inefficiencies, like idle or oversized servers, and provides clear, actionable recommendations to help you cut down on waste and improve your cloud efficiency.


## How It Works

The script reads a `cloud_usage.csv` file containing your resource data (CPU, memory, cost, etc.). It then loops through each resource, checking its utilization against predefined thresholds to identify if it's **underutilized**, **oversized**, or **idle**. Based on its findings, it suggests an action (like downsizing or termination) and even gives you an estimate of the potential monthly savings for each recommendation.


## Getting Started

1.  **Get the script:**
    Clone this repository or just download the `infrastructure-cost-optimization-advisor.py` file.

2.  **Prepare your data file:**
    Create a CSV file named `cloud_usage.csv` and place it in the same directory as the script. It must contain the following columns:
    * `id`: A unique identifier for the resource.
    * `name`: The name of the resource.
    * `cpu`: The CPU utilization percentage.
    * `memory`: The memory utilization percentage.
    * `cost`: The monthly cost of the resource (e.g., in INR or USD).

    Here's an example of how the CSV should be structured:
    ```csv
    id,name,cpu,memory,cost
    101,WebServer-A,8,20,1500
    102,Database-Main,45,60,4000
    103,Test-Environment,1,5,1800
    ```


## Usage

To run the analysis, navigate to the script's directory in your terminal and execute it using Python 3.

```bash
python3 infrastructure-cost-optimization-advisor.py
```

You can also schedule the script to run automatically. For example, to run it every Monday at 9:00 AM using a cron job on a Linux system, you would add the following line to your crontab:

```bash
# This command breaks down as follows:
# 0 9 * * 1  - The schedule: Run at minute 0, hour 9, on any day, any month, but only on Monday (1).
# /usr/bin/python3 - The full path to your Python 3 interpreter.
# /path/to/infrastructure-cost-optimization-advisor.py - The full path to your script.
0 9 * * 1 /usr/bin/python3 /path/to/infrastructure-cost-optimization-advisor.py
```


## Requirements

-   Python 3.x
-   A `cloud_usage.csv` file formatted correctly and located in the same directory as the script.

## Example Output

Here's what a sample report from the script looks like:

```text
===============================================
### Infrastructure Cost Optimization Advisor Report
===============================================

Analyzing resource usage and cost data...
Applying optimization logic and recommendations...

ID      Name            Status          Suggested Action    Estimated Savings
----------------------------------------------------------------------------------
1       web-server-1    Underutilized   Downsize            ₹1250.00
2       db-server-1     Oversized       Review Scaling      ₹0.00
3       backup-1        Idle            Terminate           ₹1800.00
4       app-server-2    Underutilized   Downsize            ₹1500.00
5       api-server      OK              -                   ₹0.00

===============================================
### Analysis complete. Review suggested actions
### to reduce cloud infrastructure costs.
===============================================
```


## Troubleshooting

-   **Getting a `KeyError: 'cpu'` (or similar)?**
    This usually means a required column is missing from your `cloud_usage.csv` file or is named incorrectly. Remember that column names are case-sensitive.

-   **Is the script crashing or failing to parse data?**
    Check your CSV file for errors. Make sure all numeric fields (`cpu`, `memory`, `cost`) contain valid numbers and that there are no empty cells or missing values.

-   **No optimization suggestions are generated?**
    This could mean your resources are already running efficiently! If you think that's not the case, you can adjust the utilization thresholds directly within the script to be more aggressive in flagging potential savings.


## License

This project is licensed under the [MIT License](LICENSE).
