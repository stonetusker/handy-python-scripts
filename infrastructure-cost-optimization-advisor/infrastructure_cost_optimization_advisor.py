#!/usr/bin/env python3

# Infrastructure Cost Optimization Advisor
# Analyzes cloud usage and cost data to detect underutilized or oversized resources
# and recommends or applies cost-saving actions.

import csv

# Simulated CSV: id, name, cpu, memory, cost
with open('cloud_usage.csv', 'r') as file:
    reader = csv.DictReader(file)
    print("ID\tName\t\tStatus\t\tSuggested Action\t\tEstimated Savings")
    print("-" * 80)

    for row in reader:
        cpu = float(row['cpu'])
        mem = float(row['memory'])
        cost = float(row['cost'])
        status = "OK"
        action = "-"
        savings = 0

        if cpu == 0 and mem == 0:
            status = "Idle"
            action = "Terminate"
            savings = cost
        elif cpu < 10 and mem < 20:
            status = "Underutilized"
            action = "Downsize"
            savings = cost * 0.5
        elif cpu > 90 or mem > 90:
            status = "Oversized"
            action = "Review Scaling"
            savings = 0

        print(f"{row['id']}\t{row['name']}\t{status}\t{action}\t\t₹{savings:.2f}")

