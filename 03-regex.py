import re

def analyze_log_file(filename, search):
    suspicious_activity = []
    with open(filename, 'r') as f:
        for line in f:
            # Regex pattern to match suspicious activity
            pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[.*\] \"[A-Z]+\s+\/[^\s]+\s+HTTP\/\d\.\d\" \d{3} \d+"

            match = re.search(pattern, line)
            if match:
                ip_address = match.group(1)

                # Add additional checks for suspicious activity, e.g.,
                if ip_address in ["192.168.1.100", "10.0.0.1"]:  # Known internal IPs
                    continue

                # Check for failed login attempts
                if search in line:
                    suspicious_activity.append(line)

    return suspicious_activity

log_file = "samples/access.log"

# Ask what to find in the logs
search = input("Enter a search term: ")

suspicious_logs = analyze_log_file(log_file, search)

if suspicious_logs:
    print("Suspicious activity found:")
    for log in suspicious_logs:
        print(log)
else:
    print("No suspicious activity detected.")