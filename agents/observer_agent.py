import random

LOG_TEMPLATES = [
    ("[INFO] User login from IP 192.168.1.10", "INFO"),
    ("[WARNING] Multiple failed login attempts", "WARNING"),
    ("[CRITICAL] Unauthorized root access detected", "CRITICAL"),
    ("[ERROR] Malware signature detected on endpoint 32", "ERROR"),
    ("[ALERT] Phishing email opened by employee", "ALERT"),
    ("[NOTICE] Firewall port scan attempt blocked", "NOTICE")
]

def get_logs():
    return random.choice(LOG_TEMPLATES)  # Returns (message, level)
