# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and reduce code complexity
  - **Input**: Source function in any language
  - **Output**: Optimized code with explanation of changes

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting standards
  - **Input**: Code block with inconsistent style
  - **Output**: Rewritten code following PEP8 or ESLint rules

- **Code Review**
  - **Goal**: Identify issues and improvements before merging
  - **Input**: Function or pull request diff
  - **Output**: Annotated feedback with suggested fixes

## Debugging
- **Error Diagnosis**
  - **Goal**: Find root cause of a runtime or logic error
  - **Input**: Buggy code with error message or stack trace
  - **Output**: Explanation of the bug and suggested fix

- **Silent Bug Detection**
  - **Goal**: Find bugs that return wrong results without throwing errors
  - **Input**: Function with incorrect output and expected behavior
  - **Output**: Root cause analysis and corrected version

- **Regression Identification**
  - **Goal**: Find which change caused a previously passing test to fail
  - **Input**: Before and after code diff with failing test output
  - **Output**: Identification of the breaking change and a fix

## Documentation
- **Docstring Generation**
  - **Goal**: Generate complete and accurate function documentation
  - **Input**: Function signature and body in any language
  - **Output**: Docstring in JSDoc or Python docstring format

- **README Creation**
  - **Goal**: Generate a professional README for a project
  - **Input**: Project name, purpose, tech stack, and usage examples
  - **Output**: Structured Markdown README with all standard sections

- **Inline Comment Writing**
  - **Goal**: Add clear explanatory comments to complex code
  - **Input**: Uncommented or poorly commented code block
  - **Output**: Same code with concise and accurate inline comments

## Testing
- **Unit Test Generation**
  - **Goal**: Create tests that cover normal cases and edge cases
  - **Input**: Function or class in any language
  - **Output**: Test file using the appropriate framework such as pytest or Jest

- **Edge Case Identification**
  - **Goal**: Discover inputs that are likely to cause failures
  - **Input**: Function signature and description of intended behavior
  - **Output**: List of edge cases with test inputs and expected outputs

- **Mock Generation**
  - **Goal**: Create mock objects for external dependencies in tests
  - **Input**: Function that calls an API or database
  - **Output**: Mock implementation with configurable return values