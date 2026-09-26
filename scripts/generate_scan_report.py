#!/usr/bin/env python3
"""
Generate comprehensive scan report from all scan results
"""
import json
import os
from datetime import datetime
from pathlib import Path

def generate_scan_report():
    """Generate comprehensive report from all scan results"""
    timestamp = datetime.now().isoformat()
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    print(f"[{timestamp}] Generating scan report...")

    # Collect all scan results
    results = {
        "timestamp": timestamp,
        "security": load_scan_results("scan-results/security"),
        "bugs": load_scan_results("scan-results/bugs"),
        "latent": load_scan_results("scan-results/latent")
    }

    # Generate summary statistics
    summary = {
        "total_findings": 0,
        "by_category": {
            "security": len(results["security"].get("findings", [])),
            "bugs": len(results["bugs"].get("findings", [])),
            "latent": len(results["latent"].get("findings", []))
        },
        "by_severity": {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        }
    }

    # Count severity levels
    for category in ["security", "bugs", "latent"]:
        for finding in results[category].get("findings", []):
            severity = finding.get("severity", "low").lower()
            if severity in summary["by_severity"]:
                summary["by_severity"][severity] += 1
            summary["total_findings"] += 1

    # Generate markdown report
    report = f"""# Nightly Scan Report
Generated: {timestamp}

## Summary
- **Total Findings**: {summary['total_findings']}
- **Security Issues**: {summary['by_category']['security']}
- **Bugs**: {summary['by_category']['bugs']}
- **Latent Issues**: {summary['by_category']['latent']}

## Severity Breakdown
- **Critical**: {summary['by_severity']['critical']}
- **High**: {summary['by_severity']['high']}
- **Medium**: {summary['by_severity']['medium']}
- **Low**: {summary['by_severity']['low']}

## Security Issues
{format_findings(results['security'].get('findings', []))}

## Bugs
{format_findings(results['bugs'].get('findings', []))}

## Latent Issues
{format_findings(results['latent'].get('findings', []))}

## Observability
- Scan duration: TODO
- Files analyzed: TODO
- Code coverage: TODO
- Trend analysis: TODO
"""

    # Save report (use safe filename without colons)
    safe_timestamp = timestamp.replace(":", "-").replace(".", "-")
    with open(f"{report_dir}/scan-report-{safe_timestamp}.md", "w") as f:
        f.write(report)

    # Save JSON summary
    with open(f"{report_dir}/scan-summary-{safe_timestamp}.json", "w") as f:
        json.dump({"summary": summary, "details": results}, f, indent=2)

    print(f"[{timestamp}] Scan report generated successfully")
    return summary

def load_scan_results(directory):
    """Load latest scan results from directory"""
    try:
        files = list(Path(directory).glob("*.json"))
        if not files:
            return {"findings": []}
        latest_file = max(files, key=os.path.getctime)
        with open(latest_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading scan results from {directory}: {e}")
        return {"findings": []}

def format_findings(findings):
    """Format findings for markdown report"""
    if not findings:
        return "No findings found."
    
    formatted = []
    for i, finding in enumerate(findings, 1):
        formatted.append(f"{i}. **{finding.get('title', 'Untitled')}** ({finding.get('severity', 'Unknown')})")
        formatted.append(f"   - Location: {finding.get('location', 'Unknown')}")
        formatted.append(f"   - Description: {finding.get('description', 'No description')}")
        formatted.append("")
    
    return "\n".join(formatted)

if __name__ == "__main__":
    generate_scan_report()