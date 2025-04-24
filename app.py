from flask import Flask, render_template
from agents.observer_agent import get_logs
from agents.planner_agent import get_response_action

app = Flask(__name__)

# Global history list (MUST be outside the route!)
history = []

@app.route('/')
def home():
    log, _ = get_logs()
    action = get_response_action(log)

    # Store in history
    history.append({'log': log, 'action': action})
    if len(history) > 20:
        history.pop(0)

    return render_template('index.html', log=log, action=action, history=history)

if __name__ == "__main__":
 app.run(debug=True, use_reloader=False)

