# Regression Identification Prompt Template

**Role**: Senior Developer
**Task**: Identify which change in the given diff caused a previously passing test to fail.
**Input Placeholder**: [CODE_DIFF], [FAILING_TEST_OUTPUT]
**Expected Output**: Identification of the breaking change, explanation of why it caused the regression, and a fix.

---

## Example Prompt

You are a senior developer investigating a regression.
A recent code change caused a previously passing test to fail.

Code diff:
```
[CODE_DIFF]
```

Failing test output:
```
[FAILING_TEST_OUTPUT]
```

Identify the exact change that caused the regression, explain why it broke the test, and suggest a fix.
