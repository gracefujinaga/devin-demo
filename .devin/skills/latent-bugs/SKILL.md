# Latent Bugs and Edge Cases

Identify hidden bugs, edge cases, and potential failure modes that aren't immediately apparent but could cause issues in production.

## Usage

```
/latent-bugs [scope]
```

## Examples

- Full scan: `/latent-bugs`
- Critical paths: `/latent-bugs critical code paths`
- Edge case focus: `/latent-bugs boundary conditions`

## What it does

Performs deep analysis to identify subtle bugs and edge cases:

**Edge Case Detection:**
- Boundary condition errors
- Empty/null input handling
- Concurrent access issues
- Large dataset handling
- Special character/encoding issues
- Timezone and locale problems
- Floating point precision issues
- Integer overflow risks

**Latent Bug Detection:**
- Race conditions in concurrent code
- Memory leaks in long-running processes
- Resource exhaustion under load
- Cache invalidation issues
- Deadlock potential
- Starvation scenarios
- Performance degradation patterns
- State synchronization issues

**Error Handling Gaps:**
- Missing error handling paths
- Incomplete error recovery
- Silent failures
- Error message clarity issues
- Exception swallowing
- Error state corruption

**Configuration Edge Cases:**
- Missing default configurations
- Invalid configuration handling
- Configuration conflicts
- Environment-specific edge cases
- Feature flag edge cases
- Dependency version conflicts

**Integration Edge Cases:**
- API version compatibility
- Network failure handling
- Service dependency failures
- Data format edge cases
- Timeout handling under stress
- Retry logic edge cases

**Output:**
- Creates GitHub issues for latent bugs and edge cases
- Prioritizes by likelihood and potential impact
- Provides reproduction scenarios
- Suggests defensive programming improvements
- Tracks technical debt related to edge cases

## Context

This skill performs sophisticated analysis beyond standard bug detection, looking for subtle issues that only manifest under specific conditions. It uses control flow analysis, data flow analysis, and domain-specific patterns for web applications, databases, and visualization systems.

## Observability

Generates:
- Latent bug summary (by category, risk level)
- Edge case coverage analysis
- Production risk assessment
- Code complexity vs risk correlation
- Monitoring recommendations for detected issues
- Comparison with previous edge case scans