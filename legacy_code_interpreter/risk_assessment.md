# Risk Assessment
## Project: `legacy_code_interpreter` — `holbertonschool-ai4devs`

> Identified risks in the legacy codebase, prioritized by severity.
> Based on static analysis of interpreter architecture: Lexer, Parser, Evaluator, Environment, and runtime execution.

---

## Risk Table

| # | Risk | Severity | Location | Notes |
|---|---|---|---|---|
| 1 | No division-by-zero guard | **High** | `Interpreter.evaluate()` | `left / right` crashes with unhandled `ZeroDivisionError` at runtime |
| 2 | Infinite loop with no timeout | **High** | `Interpreter.run_program()` | `WHILE` loops have no iteration cap — a `while 1:` halts the entire interpreter |
| 3 | Silent `None` return on unknown AST node | **High** | `Interpreter.evaluate()` | Unmatched node types return `None` silently, causing hard-to-trace downstream bugs |
| 4 | No input sanitization in Lexer | **High** | `Lexer.tokenize()` | Malformed or adversarial input raises bare `SyntaxError` with no safe fallback or recovery |
| 5 | Scope mutation inconsistency (`set` vs `assign`) | **High** | `Environment` class | `set()` always writes to local scope; outer variable re-assignment silently creates a shadow variable instead |
| 6 | Missing unit tests | **High** | Entire codebase | No test coverage found for Lexer, Parser, or Evaluator — bugs introduced by changes go undetected |
| 7 | Hardcoded keyword list as global variable | **Medium** | `Lexer.tokenize()` | `KEYWORDS` is a module-level global; adding/removing keywords has no central interface and can cause subtle token misclassification |
| 8 | Fragile tuple-based AST nodes | **Medium** | Parser & Evaluator | Nodes are raw tuples accessed by index (e.g., `node[2]`, `node[3]`); a shape mismatch raises a cryptic `IndexError` with no type safety |
| 9 | No error recovery in parser | **Medium** | `Parser.parse_expression()` | First syntax error aborts parsing entirely — no partial recovery or multiple-error reporting |
| 10 | Recursive scope lookup (stack overflow risk) | **Medium** | `Environment.get()` / `assign()` | Deeply nested scopes use Python recursion; hits `RecursionError` with >~1000 nesting levels |
| 11 | No logging or execution tracing | **Medium** | All interpreter stages | Failures produce raw Python exceptions with no interpreter-level context (line, column, call stack) |
| 12 | No float or string literal support | **Medium** | `Lexer.tokenize()` | Only integer numbers are tokenized; float (`3.14`) and string (`"hello"`) literals silently fail or are misread |
| 13 | Tight coupling between Parser and Evaluator | **Medium** | `Parser` + `Interpreter` | The evaluator directly depends on the internal tuple structure of AST nodes — changing the parser breaks the evaluator |
| 14 | No `break` / `return` / `continue` support | **Low** | `Interpreter.run_program()` | Control flow inside loops cannot exit early; workarounds produce incorrect behavior |
| 15 | No type checking on variable assignment | **Low** | `Environment.set()` | Any value (including `None`) can be assigned to any variable with no validation, making runtime type errors unpredictable |
| 16 | Deprecated / manual string scanning instead of `re` | **Low** | `Lexer.tokenize()` | Hand-rolled character loop is harder to maintain and extend than using Python's `re` module with named groups |
| 17 | No documentation or inline comments | **Low** | Entire codebase | No docstrings on public methods; new contributors cannot understand intent or expected inputs/outputs |

---

## Severity Breakdown

| Severity | Count |
|---|---|
| 🔴 High | 6 |
| 🟡 Medium | 6 |
| 🟢 Low | 5 |

---

## Top Priorities (Recommended Fix Order)

1. **Add division-by-zero guard** in `evaluate()` — one-line fix, prevents hard crashes.
2. **Add loop iteration limit** in `run_program()` — prevents interpreter hangs.
3. **Add default error case** in `evaluate()` — eliminates silent `None` bugs.
4. **Write unit tests** for Lexer, Parser, and Evaluator — foundational safety net before any refactoring.
5. **Refactor AST nodes** from raw tuples to `dataclasses` or `namedtuple` — removes fragile index-based access.
6. **Fix `Environment.set()` vs `assign()` semantics** — correct scoping behavior for variable re-assignment.
