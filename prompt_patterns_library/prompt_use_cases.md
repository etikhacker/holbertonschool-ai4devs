# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and reduce code complexity
  - **Input**: Source function in any language
  - **Output**: Optimized code with explanation of changes

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting
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
  - **Goal**: Find bugs that return wrong results without errors
  - **Input**: Function with incorrect output
  - **Output**: Root cause analysis and corrected version

- **Regression Identification**
  - **Goal**: Find which change caused a test to fail
  - **Input**: Before and after code diff with failing test
  - **Output**: Identification of the breaking change and fix

## Documentation
- **Docstring Generation**
  - **Goal**: Generate complete function documentation automatically
  - **Input**: Function signature and body in any language
  - **Output**: Docstring in JSDoc or Python format

- **README Creation**
  - **Goal**: Generate a professional project README
  - **Input**: Project name, purpose, tech stack, and examples
  - **Output**: Structured Markdown README with all sections

- **Inline Comment Writing**
  - **Goal**: Add clear comments to complex code sections
  - **Input**: Uncommented code block
  - **Output**: Same code with accurate inline comments

## Testing
- **Unit Test Generation**
  - **Goal**: Create tests covering normal and edge cases
  - **Input**: Function or class in any language
  - **Output**: Test file using pytest, Jest, or JUnit

- **Edge Case Identification**
  - **Goal**: Discover inputs likely to cause failures
  - **Input**: Function signature and intended behavior description
  - **Output**: Edge case list with inputs and expected outputs

- **Mock Generation**
  - **Goal**: Create mocks for external dependencies in tests
  - **Input**: Function that calls an API or database
  - **Output**: Mock implementation with configurable return values

## Code Generation
- **Boilerplate Scaffolding**
  - **Goal**: Generate project structure to avoid repetitive setup
  - **Input**: Project type, language, and framework name
  - **Output**: Starter code with folder structure and entry point

- **Algorithm Implementation**
  - **Goal**: Implement a known algorithm from a description
  - **Input**: Algorithm name or pseudocode steps
  - **Output**: Clean implementation in the requested language

- **API Integration**
  - **Goal**: Generate code to connect with a third-party API
  - **Input**: API endpoint description or documentation link
  - **Output**: Working integration code with error handling