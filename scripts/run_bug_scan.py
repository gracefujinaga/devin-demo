#!/usr/bin/env python3
"""
Bug Scan Script
Invokes Devin CLI with bug-scan skill for nightly automation
"""
import subprocess
import json
import os
from datetime import datetime

def run_devin_bug_scan():
    """Run Devin CLI with bug-scan skill"""
    timestamp = datetime.now().isoformat()
    output_dir = "scan-results/bugs"
    os.makedirs(output_dir, exist_ok=True)

    print(f"[{timestamp}] Starting bug scan...")

    try:
        # Example: devin --non-interactive "/bug-scan"
        result = subprocess.run(
            ["devin", "--non-interactive", "/bug-scan"],
            capture_output=True,
            text=True,
            timeout=3600
        )

        results = {
            "timestamp": timestamp,
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "findings": []
        }

        with open(f"{output_dir}/bug-results-{timestamp}.json", "w") as f:
            json.dump(results, f, indent=2)

        print(f"[{timestamp}] Bug scan completed successfully")
        return True

    except subprocess.TimeoutExpired:
        print(f"[{timestamp}] Bug scan timed out")
        return False
    except Exception as e:
        print(f"[{timestamp}] Bug scan failed: {e}")
        return False

if __name__ == "__main__":
    success = run_devin_bug_scan()
    exit(0 if success else 1)