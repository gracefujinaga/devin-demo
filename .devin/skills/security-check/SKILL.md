# Security Check

Perform comprehensive security analysis of the codebase to identify vulnerabilities, security issues, and potential exploits.

## Usage

```
/security-check [scope]
```

## Examples

- Full scan: `/security-check`
- Specific directory: `/security-check superset/charts/`
- File type specific: `/security-check python files only`

## What it does

Performs security analysis across the codebase:

**Vulnerability Detection:**
- SQL injection vulnerabilities
- Cross-site scripting (XSS) risks
- Authentication/authorization issues
- Input validation problems
- Dependency vulnerabilities
- Secret/key exposure risks
- Path traversal vulnerabilities

**Code Security Patterns:**
- Insecure random number generation
- Weak cryptographic implementations
- Unsafe deserialization
- Resource exhaustion risks
- Race conditions
- Timing attack vulnerabilities

**Configuration Security:**
- Insecure configurations
- Exposed sensitive endpoints
- Missing security headers
- CORS misconfigurations
- Authentication bypasses

**Output:**
- Creates GitHub issues for critical security findings
- Generates security report with severity levels
- Proposes fixes for identified vulnerabilities
- Tracks security debt over time

## Context

This skill uses static analysis and pattern matching to identify security issues. It leverages the project's security guidelines from AGENTS.md and SECURITY.md to ensure findings align with the project's security model. Issues are prioritized by severity and potential impact.

## Observability

Generates:
- Security summary report (high/medium/low severity counts)
- Trend analysis of security issues over time
- Comparison with previous scans
- Coverage statistics (files analyzed vs total)