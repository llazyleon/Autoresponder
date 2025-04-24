from agents.observer_agent import get_logs
from agents.anomaly_detector_agent import detect_anomalies
from agents.planner_agent import get_response_action
import time

def run_pipeline():
    logs = get_logs()
    if not logs:
        print("No logs found.")
        return

    print("Running detection...")
    threats = detect_anomalies(logs)

    if not threats:
        print("✅ No threats detected.")
        return

    for threat in threats:
        print(f"🚨 Threat: {threat}")
        action = get_response_action(threat)
        print(f"🤖 AI Decision: {action}")

if __name__ == "__main__":
    while True:
        run_pipeline()
        time.sleep(5)
