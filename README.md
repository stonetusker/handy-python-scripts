1. **Automated Log Analyzer**
   - Scans server or application logs for errors, warnings, or specific patterns and summarizes findings in a report. Pick /var/log/ files and logs of Apache and Anginx
  
2. **Service Health Checker**
   - Periodically pings service endpoints (web servers, APIs, databases) and notifies via Slack/Teams if any services are down or unresponsive. Pick Postgresql, Nginx as example
  
3. **SSL Certificate Expiry Checker**
    - Monitors SSL/TLS certificates for websites and sends alerts ahead of expiry to prevent outages.
  
4. **Automated Incident Response Script**  
   - Automatically detects alerts from monitoring tools and triggers predefined recovery actions, like restarting services or rolling back deployments.

5. **Container Image Vulnerability Monitor**  
   - Periodically scans Docker images in your registry for known CVEs using APIs of scanners like Clair or Trivy, and creates detailed vulnerability reports.
   
6. **Infrastructure Cost Optimization Advisor**  
   - Reviews cloud resource usage and cost data, identifies underutilized or oversized resources, and suggests or applies cost-saving measures.

7. **System Resource Monitoring & Alerting**
   - Scripts that monitor CPU, memory, disk, and network resource usage, then send alerts if thresholds are exceeded. Widely used for real-time server health checks and proactive incident respons

8. **Permissions and Ownership Auditor**
   - Scans directories (e.g., /etc, /var/www) for files with incorrect permissions or ownership, suggests or applies fixes, and logs changes for compliance purposes

