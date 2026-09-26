# Bug Scan

Identify existing bugs, errors, and defects in the codebase through static analysis and pattern detection.

## Usage

```
/bug-scan [scope]
```

## Examples

- Full scan: `/bug-scan`
- Specific module: `/bug-scan superset/charts/`
- Recent changes: `/bug-scan last 7 days`

## What it does

Performs comprehensive bug detection across the codebase:

**Runtime Error Detection:**
- Null pointer/reference errors
- Index out of bounds issues
- Type mismatches
- Division by zero risks
- Uncaught exceptions
- Resource leaks

**Logic Errors:**
- Incorrect conditionals
- Off-by-one errors
- Infinite loops
- Dead code paths
- Unreachable code
- Missing return statements

**Data Flow Issues:**
- Uninitialized variables
- Use before initialization
- Unused variables/imports
- Parameter validation issues
- Data type inconsistencies

**API Usage Errors:**
- Incorrect API calls
- Missing error handling
- Timeout issues
- Connection leak detection
- Race conditions in async code

**Configuration Bugs:**
- Missing required configuration
- Invalid configuration values
- Environment-specific issues
- Feature flag problems

**Output:**
- Creates GitHub issues for identified bugs
- Categorizes bugs by severity and type
- Provides code snippets showing the issues
- Suggests fixes with examples
- Tracks bug debt and resolution trends

## Context

This skill uses static analysis, pattern matching, and the project's test suite to identify bugs. It leverages existing test failures, error patterns, and common Python/JavaScript bug patterns. Findings are prioritized by likelihood of occurrence and potential impact.

## Observability

Generates:
- Bug summary report (by type, severity, location)
- Trend analysis of bug detection over time
- Comparison with previous scans
- Hotspot identification (files/modules with most bugs)
- Fix rate tracking (bugs found vs bugs fixed)