import json
import os

os.makedirs("results", exist_ok=True)

with open("results/report.json") as f:
    data = json.load(f)

clean_results = []

for test in data["tests"]:
    full_name = test["nodeid"]

    # Extract method name
    method_name = full_name.split("::")[-1]

    # Remove [chromium] or params
    method_name = method_name.split("[")[0]

    clean_results.append({
        "test_name": method_name,
        "outcome": test["outcome"],
        "duration": test["call"]["duration"] if "call" in test else None
    })

with open("results/clean_report.json", "w") as f:
    json.dump(clean_results, f, indent=4)