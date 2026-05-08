# Error Diagnosis Prompt Template

**Role**: Debugging Specialist
**Task**: Analyze the given [LANGUAGE] code and its error message to identify the root cause and provide a fix.
**Input Placeholder**: [CODE_BLOCK] and [ERROR_MESSAGE]
**Expected Output**: Root cause explanation, corrected code, and steps to prevent the same error in future.

---

## Example Prompt

You are a debugging specialist.
The following [LANGUAGE] code throws an error. Identify the root cause and explain how to fix it.

Code:
```
[CODE_BLOCK]
```

Error:
```
[ERROR_MESSAGE]
```

Return the root cause explanation, the fixed code, and one tip to prevent this error in the future.
