import time
import random
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sample_logs.txt")
os.makedirs(LOG_DIR, exist_ok=True)

LOGS = [
    "[INFO] User login from 192.168.0.101",
    "[WARNING] File access pattern anomaly",
    "[ERROR] Multiple failed login attempts",
    "[CRITICAL] Unauthorized root access detected",
    "[INFO] Scheduled backup completed",
    "[WARNING] Suspicious outbound connection detected"
]

def stream_logs():
    with open(LOG_FILE, "a") as f:
        while True:
            log = random.choice(LOGS)
            print(f"[LogStream] {log}")
            f.write(log + "\n")
            f.flush()
            time.sleep(1.5)

if __name__ == "__main__":
    stream_logs()
