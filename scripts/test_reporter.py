import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_tests_and_generate_report(test_dir="test", output_file="results/test_report.json"):
    """
    Run pytest tests and generate a JSON report with test results.
    
    Args:
        test_dir: Directory containing test files
        output_file: Path to output JSON report
    
    Returns:
        dict: Test report containing all results
    """
    
    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Run pytest with JSON report plugin
    pytest_args = [
        "pytest",
        test_dir,
        "-v",
        "--tb=short",
        f"--json-report",
        f"--json-report-file={output_file}",
        "-p", "no:debugging"
    ]
    
    try:
        result = subprocess.run(pytest_args, capture_output=True, text=True)
    except Exception as e:
        # Fallback if json-report plugin is not available
        print(f"Note: json-report plugin not found. Using alternative method: {e}")
        return run_tests_with_custom_parser(test_dir, output_file)
    
    return load_report(output_file)


def run_tests_with_custom_parser(test_dir="test", output_file="results/test_report.json"):
    """
    Run pytest and parse output to generate custom JSON report.
    
    Args:
        test_dir: Directory containing test files
        output_file: Path to output JSON report
    
    Returns:
        dict: Test report containing all results
    """
    
    # Run pytest with minimal output
    pytest_args = [
        "pytest",
        test_dir,
        "-v",
        "--tb=short",
        "-p", "no:debugging"
    ]
    
    result = subprocess.run(pytest_args, capture_output=True, text=True)
    
    # Parse pytest output
    lines = result.stdout.split('\n')
    tests = []
    test_summary = {"passed": 0, "failed": 0, "skipped": 0, "error": 0}
    
    for line in lines:
        if "PASSED" in line or "FAILED" in line or "SKIPPED" in line or "ERROR" in line:
            parts = line.split(" ")
            if len(parts) > 1:
                test_name = parts[0]
                if "PASSED" in line:
                    status = "passed"
                    test_summary["passed"] += 1
                elif "FAILED" in line:
                    status = "failed"
                    test_summary["failed"] += 1
                elif "SKIPPED" in line:
                    status = "skipped"
                    test_summary["skipped"] += 1
                else:
                    status = "error"
                    test_summary["error"] += 1
                
                tests.append({
                    "name": test_name,
                    "status": status,
                    "output": line.strip()
                })
    
    # Create report
    report = {
        "timestamp": datetime.now().isoformat(),
        "test_directory": test_dir,
        "return_code": result.returncode,
        "tests": tests,
        "summary": {
            "total": len(tests),
            "passed": test_summary["passed"],
            "failed": test_summary["failed"],
            "skipped": test_summary["skipped"],
            "error": test_summary["error"]
        },
        "stdout": result.stdout,
        "stderr": result.stderr
    }
    
    # Write report to JSON file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Test report generated: {output_file}")
    print(json.dumps(report["summary"], indent=2))
    
    return report


def load_report(report_file):
    """
    Load and parse a JSON report file.
    
    Args:
        report_file: Path to JSON report
    
    Returns:
        dict: Parsed report data
    """
    
    try:
        with open(report_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Report file not found: {report_file}")
        return None


def print_report_summary(report):
    """
    Print a formatted summary of the test report.
    
    Args:
        report: Test report dictionary
    """
    
    if not report:
        return
    
    print("\n" + "="*60)
    print("TEST REPORT SUMMARY")
    print("="*60)
    print(f"Timestamp: {report.get('timestamp', 'N/A')}")
    print(f"Test Directory: {report.get('test_directory', 'N/A')}")
    print("\nTest Results:")
    
    summary = report.get("summary", {})
    print(f"  Total Tests: {summary.get('total', 0)}")
    print(f"  Passed: {summary.get('passed', 0)}")
    print(f"  Failed: {summary.get('failed', 0)}")
    print(f"  Skipped: {summary.get('skipped', 0)}")
    print(f"  Errors: {summary.get('error', 0)}")
    print(f"\nReturn Code: {report.get('return_code', 'N/A')}")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Run tests and generate report
    report = run_tests_with_custom_parser(
        test_dir="test",
        output_file="results/test_report.json"
    )
    
    # Print summary
    print_report_summary(report)
