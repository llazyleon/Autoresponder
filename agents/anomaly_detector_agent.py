def detect_anomalies(logs):
    alerts = []
    for log in logs:
        if "CRITICAL" in log or "ERROR" in log:
            alerts.append(log.strip())
    return alerts

if __name__ == "__main__":
    from observer_agent import get_logs

    logs = get_logs()
    alerts = detect_anomalies(logs)
    for a in alerts:
        print(f"[AnomalyDetector] 🚨 Detected: {a}")
