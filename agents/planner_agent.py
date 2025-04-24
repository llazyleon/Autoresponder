def get_response_action(log: str) -> str:
    try:
        # real OpenAI logic (disabled or replaced with mock)
        return mock_response(log)
    except Exception:
        return mock_response(log)

def mock_response(log: str) -> str:
    log = log.lower()
    if "unauthorized" in log:
        return "Isolate affected server and reset credentials."
    elif "malware" in log:
        return "Run antivirus scan and monitor system."
    elif "phishing" in log:
        return "Notify user and block sender."
    else:
        return "Log the event and monitor for escalation."
