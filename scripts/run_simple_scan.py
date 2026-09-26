#!/usr/bin/env python3
"""
Simple scan runner for demo
Runs all three scans and generates report
"""
import json
import os
from datetime import datetime
from devin_api_client import run_scan_and_remediate

def main():
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] Starting Devin Scan Demo")
    
    # Run all three scans
    skills = ["security-check", "bug-scan", "latent-bugs"]
    all_findings = []
    
    for skill in skills:
        result = run_scan_and_remediate(skill, "superset")
        if result.get("success"):
            all_findings.extend(result.get("findings", []))
        print(f"[{timestamp}] {skill} completed")
    
    # Generate simple report
    report = {
        "timestamp": timestamp,
        "total_findings": len(all_findings),
        "by_skill": {
            "security-check": len([f for f in all_findings if f["severity"] == "high"]),
            "bug-scan": len([f for f in all_findings if f["severity"] == "medium"]),
            "latent-bugs": len([f for f in all_findings if f["severity"] == "low"])
        },
        "findings": all_findings
    }
    
    # Save report
    os.makedirs("reports", exist_ok=True)
    with open(f"reports/scan-report-{timestamp.replace(':', '-').replace('.', '-')}.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"[{timestamp}] Scan complete. Total findings: {len(all_findings)}")
    print(f"[{timestamp}] Report saved to reports/")
    
    return report

if __name__ == "__main__":
    main()
