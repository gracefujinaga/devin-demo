# Devin Automated Code Quality Scanner

An autonomous code quality scanning system using Devin API to detect and remediate security vulnerabilities, runtime errors, and latent bugs in the Apache Superset codebase.

## Overview

This system demonstrates how Devin API can be integrated into CI/CD pipelines to provide contextual code analysis and automated remediation. It:

- **Detects** - Security vulnerabilities, runtime errors, logic errors, latent bugs
- **Remediates** - Automatically applies fixes via Devin API
- **Observes** - Tracks findings and generates reports

## Quick Start

### Setup

1. Clone the repository
```bash
git clone https://github.com/gracefujinaga/devin-demo.git
cd devin-demo
```

2. Configure API key
```bash
cp .env.example .env
# Edit .env and add your Devin API key
```

3. Run with Docker
```bash
docker-compose -f docker/docker-compose.yml up
```

### Configuration

Required environment variables in `.env`:
```bash
DEVIN_API_KEY=your_api_key_here
DEVIN_ORG_ID=your_org_id_here
GITHUB_TOKEN=your_github_token_here
```

## Architecture

### Devin API Integration

The system uses the Devin API to:
1. Create sessions programmatically
2. Execute analysis skills (security-check, bug-scan, latent-bugs)
3. Retrieve findings and apply fixes
4. Track session status and results

### Skills

1. **security-check** - Identifies vulnerabilities and security issues
2. **bug-scan** - Detects existing bugs and defects
3. **latent-bugs** - Finds hidden bugs and edge cases

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

## Output

### Scan Results
- Location: `scan-results/` directory
- Format: JSON files with structured findings
- Categories: security, bugs, latent

### Reports
- Location: `reports/` directory
- Format: JSON summary reports
- Includes: Total findings, severity breakdown, detailed findings

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

## Next Steps for Production

### Phase 1: Production Readiness
1. Configure real Devin API key
2. Test actual Devin API endpoints
3. Implement real remediation (not simulated)
4. Add GitHub token for PR creation

### Phase 2: Enterprise Hardening
1. Add secret management (GitHub Actions secrets)
2. Add access controls (who can trigger scans)
3. Add audit logging (track all Devin API calls)

### Phase 3: Advanced Features
1. Learning from historical data (reduce false positives)
2. Integration with existing security scanners
3. Custom skills for Superset-specific patterns

## Repository Links

- Apache Superset Fork: https://github.com/gracefujinaga/superset
- Original Superset: https://github.com/apache/superset
- Devin API Docs: https://docs.devin.ai/api-reference/overview

## License

Apache License 2.0 - See LICENSE file for details
