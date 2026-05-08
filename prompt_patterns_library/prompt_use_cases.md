$content = @"
# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and reduce complexity
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code with explanation of changes

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting standards
  - **Input**: Code block with inconsistent style
  - **Output**: Rewritten code following a style guide such as PEP8 or ESLint

- **Code Review**
  - **Goal**: Identify anti-patterns and improvements before merging
  - **Input**: Function or pull request diff
  - **Output**: Annotated review with suggested fixes

## Debugging
- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime or logic error
  - **Input**: Buggy code with error message or stack trace
  - **Output**: Explanation of the bug and suggested fix

- **Silent Bug Detection**
  - **Goal**: Find bugs that return wrong results without throwing errors
  - **Input**: Function with incorrect output and expected behavior description
  - **Output**: Root cause analysis and corrected version

- **Regression Identification**
  - **Goal**: Determine which change caused a previously passing test to fail
  - **Input**: Before and after code diff with failing test output
  - **Output**: Identification of the breaking change and a fix

## Documentation
- **Docstring Generation**
  - **Goal**: Generate accurate and complete function documentation
  - **Input**: Function signature and body in [LANGUAGE]
  - **Output**: Docstring in the appropriate format such as JSDoc or Python docstring

- **README Creation**
  - **Goal**: Generate a professional README for a project or repository
  - **Input**: Project name, purpose, tech stack, and usage examples
  - **Output**: Structured Markdown README with installation and usage sections

- **Inline Comment Writing**
  - **Goal**: Add clear inline comments to complex code sections
  - **Input**: Uncommented code block
  - **Output**: Same code with concise and accurate inline comments

## Testing
- **Unit Test Generation**
  - **Goal**: Create unit tests covering normal and edge cases
  - **Input**: Function or class in [LANGUAGE]
  - **Output**: Test file using the appropriate framework such as pytest or Jest

- **Edge Case Identification**
  - **Goal**: Discover inputs likely to cause failures or unexpected behavior
  - **Input**: Function signature and description of intended behavior
  - **Output**: List of edge cases with test inputs and expected outputs

- **Mock and Stub Generation**
  - **Goal**: Create mock objects for external dependencies in tests
  - **Input**: Function that calls an API or database
  - **Output**: Mock implementation with configurable return values
"@
[System.IO.File]::WriteAllText("D:\bug_descriptions.md\prompt_patterns_library\prompt_use_cases.md", $content, [System.Text.Encoding]::UTF8)