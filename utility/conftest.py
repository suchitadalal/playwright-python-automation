import json
import os

results = []


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        outcome = "passed" if call.excinfo is None else "failed"

        results.append({
            "test_name": item.name,
            "outcome": outcome,
            "duration": call.duration
        })


def pytest_sessionfinish(session, exitstatus):
    os.makedirs("results", exist_ok=True)

    with open("results/custom_report.json", "w") as f:
        json.dump(results, f, indent=4)