# Prompt Use Cases

---

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability, reduce complexity, and enhance performance
  - **Input**: Source function in [LANGUAGE]
  - **Output**: Optimized code with explanation of changes made

- **Style Enforcement**
  - **Goal**: Enforce consistent naming conventions and formatting standards
  - **Input**: Code block with inconsistent style
  - **Output**: Rewritten code following a defined style guide (e.g., PEP8, ESLint)

- **Code Review**
  - **Goal**: Identify potential issues, anti-patterns, and improvements before merging
  - **Input**: Pull request diff or function block
  - **Output**: Annotated review with severity levels and suggested fixes

---

## Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime or logic error
  - **Input**: Buggy code + error message or stack trace
  - **Output**: Explanation of the bug and one or more suggested fixes

- **Silent Bug Detection**
  - **Goal**: Find bugs that produce no error but return wrong results
  - **Input**: Function with incorrect output and expected behavior description
  - **Output**: Root cause analysis and corrected version

- **Regression Identification**
  - **Goal**: Determine which change caused a previously passing test to fail
  - **Input**: Before/after code diff + failing test output
  - **Output**: Identification of the breaking change and a fix

---

## Documentation

- **Docstring Generation**
  - **Goal**: Automatically generate accurate and complete function documentation
  - **Input**: Function signature and body in [LANGUAGE]
  - **Output**: Docstring in the appropriate format (e.g., JSDoc, Python docstring)

- **README Creation**
  - **Goal**: Generate a professional README for a project or repository
  - **Input**: Project name, purpose, tech stack, and usage examples
  - **Output**: Structured Markdown README with sections for installation, usage, and contribution

- **Inline Comment Writing**
  - **Goal**: Add clear inline comments to complex or non-obvious code sections
  - **Input**: Uncommented code block
  - **Output**: Same code with concise and accurate inline comments

---

## Testing

- **Unit Test Generation**
  - **Goal**: Create comprehensive unit tests covering normal and edge cases
  - **Input**: Function or class in [LANGUAGE]
  - **Output**: Test file using the appropriate framework (e.g., pytest, Jest, JUnit)

- **Edge Case Identification**
  - **Goal**: Discover inputs that are likely to cause failures or unexpected behavior
  - **Input**: Function signature and description of intended behavior
  - **Output**: List of edge cases with test inputs and expected outputs

- **Mock and Stub Generation**
  - **Goal**: Create mock objects or stubs for external dependencies in tests
  - **Input**: Function that calls an API, database, or external service
  - **Output**: Mock implementation with configurable return values

---

## Code Generation

- **Boilerplate Scaffolding**
  - **Goal**: Quickly generate project or file structure to avoid repetitive setup
  - **Input**: Project type, language, and framework (e.g., REST API in Node.js)
  - **Output**: Starter code with folder structure, config files, and entry point

- **Algorithm Implementation**
  - **Goal**: Implement a well-known algorithm from a description or pseudocode
  - **Input**: Algorithm name or step-by-step description in plain language
  - **Output**: Clean, commented implementation in the requested language

- **API Integration**
  - **Goal**: Generate code to connect and interact with a third-party API
  - **Input**: API documentation URL or endpoint description
  - **Output**: Working integration code with authentication and error handling
