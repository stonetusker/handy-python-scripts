
# Automated Incident Response Script

This project demonstrates a straightforward Python script that applies the fundamentals of automated incident response. It is intended as a hands-on learning resource for students, system administrators, and developers interested in DevOps and Site Reliability Engineering (SRE).

The script continuously monitors a log file for error patterns. When an error is detected, it attempts a predefined recovery action. If that action does not succeed, the script simulates escalation by notifying a human operator.



## Features

- **Log Monitoring**: Continuously tracks a specified log file for new entries.  
- **Alert Detection**: Identifies incidents by scanning for patterns such as "ERROR".  
- **Automated Recovery**: Executes a configurable shell command to attempt recovery (for example, restarting a service).  
- **Escalation Handling**: Escalates the incident if automated recovery fails, ensuring that unresolved issues reach human oversight.  
- **Configuration Driven**: Key parameters—such as file paths, commands, and monitoring intervals—are stored in a `config.json` file, so the script can adapt to new environments without code modifications.  
- **Detailed Logging**: Records all actions in a log file for auditing, debugging, or analysis.  



## How It Works

The script operates in a continuous loop with the following workflow:

1. **Load Configuration**: Reads settings from the `config.json` file.  
2. **Scan Logs**: Checks the most recent lines of the monitored log file.  
3. **Incident Detection**: Treats any line containing "ERROR" as an incident.  
4. **Recovery Attempt**: Runs the recovery action defined in the configuration.  
5. **Verification and Escalation**:  
   - If recovery succeeds, the script records the outcome and continues monitoring.  
   - If recovery fails, the failure is logged and an escalation alert is triggered.  
6. **Repeat Cycle**: Waits the configured interval before scanning again.  



## Getting Started

### Prerequisites

- Python 3.x  
- No external dependencies are required (only Python’s standard libraries are used).  

### Installation and Setup

1. Clone or download the repository:  
   ```sh
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. Confirm the following files exist in the project directory:  
   - `incident_responder.py` (main script)  
   - `config.json` (configuration file)  
   - `application.log` (sample log file for monitoring)  

### Running the Script

1. Open a terminal in the project directory.  
2. Run the script:  
   ```sh
   python3 incident_responder.py
   ```
3. The script begins monitoring immediately and checks `application.log` for errors.  


## Configuration

All runtime settings are defined in the `config.json` file.  

Example configuration:

```json
{
  "monitoring_target": "application.log",
  "log_file": "incident_response.log",
  "check_interval_seconds": 10,
  "recovery_action": "echo 'Simulating restart of the web service... Service is now OK.'",
  "escalation_contact": "devops-team@example.com"
}
```

**Parameter details**:  
- `monitoring_target`: Log file to monitor.  
- `log_file`: File where script actions are logged.  
- `check_interval_seconds`: Time delay (in seconds) between each monitoring cycle.  
- `recovery_action`: The shell command to run when an error is detected.  
- `escalation_contact`: The address or alias to notify if recovery fails.  



## Testing the Script

To simulate an incident:

1. Start the script in a terminal.  
2. Open `application.log` in a text editor.  
3. Append a new line containing the word **ERROR**:  
   ```
   2023-10-27 11:00:00 - ERROR - Critical failure in payment module.
   ```
4. Save the file.  
5. Within the configured interval (10 seconds by default), the script will detect the error and execute the recovery action.  



## Best Practices Demonstrated

This script is structured to reflect several DevOps and SRE principles:

- **Configuration over Hardcoding**: All operational settings are externalized.  
- **Idempotent Recovery**: Recovery actions can safely be run multiple times without side effects.  
- **Transparent Logging**: Each action is logged with context and status.  
- **Modular Code**: Functions are cleanly separated (`check_for_alerts`, `run_recovery_action`, etc.) for readability and maintainability.  
- **Fail-Safe Design**: Escalation to a human ensures that automation never silently fails.  


