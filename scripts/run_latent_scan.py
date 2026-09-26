#!/usr/bin/env python3
"""
Latent Bugs Scan Script
Invokes Devin CLI with latent-bugs skill for nightly automation
"""
import subprocess
import json
import os
from datetime import datetime

def run_devin_latent_scan():
    """Run Devin CLI with latent-bugs skill"""
    timestamp = datetime.now().isoformat()
    output_dir = "scan-results/latent"
    os.makedirs(output_dir, exist_ok=True)

    print(f"[{timestamp}] Starting latent bugs scan...")

    try:
        # Example: devin --non-interactive "/latent-bugs"
        result = subprocess.run(
            ["devin", "--non-interactive", "/latent-bugs"],
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

        with open(f"{output_dir}/latent-results-{timestamp}.json", "w") as f:
            json.dump(results, f, indent=2)

        print(f"[{timestamp}] Latent bugs scan completed successfully")
        return True

    except subprocess.TimeoutExpired:
        print(f"[{timestamp}] Latent bugs scan timed out")
        return False
    except Exception as e:
        print(f"[{timestamp}] Latent bugs scan failed: {e}")
        return False

if __name__ == "__main__":
    success = run_devin_latent_scan()
    exit(0 if success else 1)