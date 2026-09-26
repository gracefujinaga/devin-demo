# Devin Automated Code Quality Scanner

An autonomous code quality scanning system using Devin CLI to detect security vulnerabilities, runtime errors, and latent bugs in the Apache Superset codebase.

## Overview

This system demonstrates how Devin CLI can be integrated into CI/CD pipelines to provide contextual code analysis that goes beyond traditional static analysis tools. It detects:

- **Security vulnerabilities** - Contextual security issues that require understanding the security model
- **Runtime errors** - Errors that only manifest during execution
- **Logic errors** - Cross-file logic bugs that static analysis misses
- **Latent bugs** - Edge cases and hidden issues

## Quick Start

### Option 1: Run with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/gracefujinaga/devin-demo.git
cd devin-demo

# Run a single security scan
docker-compose -f docker/docker-compose.yml run devin-scanner

# Run all scans (security, bugs, latent)
docker-compose -f docker/docker-compose.yml run full-scan

# View results
cat reports/scan-report-*.md
```

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/gracefujinaga/devin-demo.git
cd devin-demo

# Install dependencies
pip install -r requirements.txt

# Install Devin CLI (adjust based on actual install method)
npm install -g @devin/cli

# Run security scan
python scripts/run_security_scan.py

# Run bug scan
python scripts/run_bug_scan.py

# Run latent bugs scan
python scripts/run_latent_scan.py

# Generate report
python scripts/generate_scan_report.py
```

## What Makes This Different

### Traditional Static Analysis Tools (mypy, ruff, pylint)
- ✅ Catch type errors and style violations
- ❌ Can't understand business logic
- ❌ Can't check security model compliance
- ❌ Can't analyze complex data flows

### Human Code Review
- ✅ Deep understanding of context
- ❌ Doesn't scale with codebase size
- ❌ Inconsistent across reviewers
- ❌ Fatigue leads to missed issues

### Devin CLI
- ✅ Understands codebase context (docs, patterns, architecture)
- ✅ Checks security model compliance (reads SECURITY.md)
- ✅ Scales to scan entire codebases
- ✅ Consistent results every time
- ✅ Can learn from codebase patterns

## Architecture

### Skill-Based Design

The system uses three focused skills:

1. **security-check** - Identifies vulnerabilities and security issues
   - SQL injection patterns
   - XSS vulnerabilities
   - Authentication/authorization bypasses
   - Dependency vulnerabilities

2. **bug-scan** - Detects existing bugs and defects
   - Runtime errors
   - Logic errors
   - API usage errors
   - Configuration bugs

3. **latent-bugs** - Finds hidden bugs and edge cases
   - Edge cases
   - Race conditions
   - Resource leaks
   - Boundary conditions

### Key Architectural Decisions

**Non-Interactive CLI Execution**
```python
# Scripts run Devin CLI in non-interactive mode
subprocess.run(
    ["devin", "--non-interactive", "/security-check"],
    capture_output=True,
    text=True,
    timeout=3600
)
```

**Structured JSON Output**
```python
results = {
    "timestamp": timestamp,
    "success": result.returncode == 0,
    "stdout": result.stdout,
    "stderr": result.stderr,
    "findings": []
}
```

**GitHub Actions Integration**
```yaml
- name: Run Security Check
  run: |
    python scripts/run_security_scan.py || true
    echo "security_completed=true" >> $GITHUB_OUTPUT
```

## Intentional Defects Demo

This system was tested against intentional defects introduced in Apache Superset. See [INTENTIONAL_DEFECTS.md](INTENTIONAL_DEFECTS.md) for details.

### Example Defects Detected

**1. Security: Bypass Layer Validation**
- File: `superset/commands/annotation_layer/annotation/create.py`
- Issue: Bypasses layer validation, violates SECURITY.md
- Detection: Contextual understanding of security model

**2. Logic Error: AND vs OR**
- File: `superset/commands/chart/utils.py`
- Issue: Incorrect validation logic allows invalid datasources
- Detection: Cross-file analysis of query context loading

**3. Runtime Error: Missing Null Check**
- File: `superset/commands/utils.py`
- Issue: Accesses config["params"] without null check
- Detection: Execution path analysis

## GitHub Actions Integration

The system includes a GitHub Actions workflow for automated nightly scans:

```yaml
name: Nightly Code Scan
on:
  schedule:
    - cron: '0 2 * * *'  # Run at 2 AM UTC
  workflow_dispatch:  # Allow manual triggering
```

**To trigger manually:**
```bash
gh workflow run nightly-scan.yml
```

## Output

### Scan Results
- Location: `scan-results/` directory
- Format: JSON files with structured findings
- Categories: security, bugs, latent

### Reports
- Location: `reports/` directory
- Format: Markdown summary reports
- Includes: Total findings, severity breakdown, detailed findings

## Next Steps for Production

### Phase 1: Production Readiness
1. Install Devin CLI in CI/CD pipeline
2. Extract real findings from Devin output
3. Implement actual PR creation (currently placeholder)

### Phase 2: Enterprise Hardening
1. Add secret management (GitHub Actions secrets)
2. Add access controls (who can trigger scans)
3. Add audit logging (track all Devin invocations)

### Phase 3: Advanced Features
1. Learning from historical data (reduce false positives)
2. Integration with existing security scanners
3. Custom skills for Superset-specific patterns

## Repository Links

- Apache Superset Fork: https://github.com/gracefujinaga/superset
- Original Superset: https://github.com/apache/superset
- Devin CLI: https://devin.ai

## License

Apache License 2.0 - See LICENSE file for details
