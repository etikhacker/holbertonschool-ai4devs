# Risk Assessment
## Project: `legacy_code_interpreter` — `holbertonschool-ai4devs`

---

## Risk 1 – No Division-by-Zero Guard

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Interpreter.evaluate()` |
| **Notes** | Any expression like `x / 0` raises an unhandled `ZeroDivisionError` that crashes the entire interpreter with no user-facing message. Add `if right == 0: raise RuntimeError("Division by zero")` before the `/` branch. |

---

## Risk 2 – Infinite Loop with No Iteration Cap

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Interpreter.run_program()` — `WHILE` branch |
| **Notes** | A non-terminating `while` condition hangs the interpreter process permanently, requiring a manual kill. Introduce a `MAX_ITERATIONS` counter and raise a `RuntimeError` when it is exceeded. |

---

## Risk 3 – Silent `None` Return on Unknown AST Node

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Interpreter.evaluate()` — missing `else` clause |
| **Notes** | Unrecognised node types return `None` silently. That `None` propagates into arithmetic and produces a confusing `TypeError` far from the actual fault. Add `else: raise RuntimeError(f"Unknown AST node: {node[0]}")`. |

---

## Risk 4 – No Input Sanitisation in the Lexer

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Lexer.tokenize()` |
| **Notes** | A single unexpected character (e.g. `@`, `$`) raises a bare Python `SyntaxError` with no line or column info, aborting tokenisation of the entire source. Errors should be collected with positions and reported together rather than raised immediately. |

---

## Risk 5 – Missing Unit Tests Across All Layers

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | Entire codebase |
| **Notes** | Zero test coverage means any change to the Lexer, Parser, or Evaluator can silently break existing behaviour; bugs are only discovered at runtime. Add `pytest` suites targeting at least 80 % coverage before further development. |

---

## Risk 6 – Scope Mutation Inconsistency (`set` vs `assign`)

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Environment` class |
| **Notes** | `set()` always writes to the local scope even when the variable exists in a parent scope, silently shadowing the outer binding instead of updating it. Rename `set()` to `define()` for new bindings and make `assign()` the sole path for updating existing ones. |

---

## Risk 7 – Fragile Positional Tuple Access for AST Nodes

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Parser` output consumed by `Interpreter.evaluate()` |
| **Notes** | Nodes are accessed by raw index (`node[2]`, `node[3]`). Any parser change that shifts the tuple layout causes a cryptic `IndexError` with no indication of which node type failed. Replace tuples with `dataclasses` or `typing.NamedTuple` so fields have descriptive names. |

---

## Risk 8 – No Error Recovery in the Parser

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Parser.parse_expression()` and its call chain |
| **Notes** | The first syntax error aborts parsing entirely, forcing users to fix one error, re-run, and repeat. Implement a synchronisation strategy that skips to the next statement delimiter so the parser can report multiple errors in a single pass. |

---

## Risk 9 – Recursive Scope Lookup Vulnerable to Stack Overflow

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Environment.get()` and `Environment.assign()` |
| **Notes** | Deeply nested function calls (>~950 levels on CPython) trigger Python's own `RecursionError`, leaking implementation details to the user. Rewrite both methods as iterative loops traversing the `parent` chain instead of recursive calls. |

---

## Risk 10 – Hardcoded Global `KEYWORDS` Set

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Lexer.tokenize()` — module level |
| **Notes** | Any importing module can accidentally mutate `KEYWORDS`, and adding a reserved word requires hunting for the global. Move it to a class constant or inject it as a constructor parameter to centralise control. |

---

## Risk 11 – No Float or String Literal Support

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Lexer.tokenize()` — digit and character branches |
| **Notes** | `3.14` is tokenised as two integers with a dot operator between them, silently producing wrong values. String literals are broken into individual identifier tokens with no error raised. Extend the lexer to handle `\d+\.\d+` patterns and quoted strings. |

---

## Risk 12 – No Logging or Execution Tracing

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | All interpreter stages |
| **Notes** | When the interpreter fails there is no record of which statement was executing or what variables were in scope. Diagnosing bug reports requires reproducing the exact input from scratch. Integrate Python's `logging` module with `DEBUG`-level eval traces and `ERROR`-level exception entries. |

---

## Risk 13 – Tight Coupling Between Parser and Evaluator

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `Parser` ↔ `Interpreter` interface |
| **Notes** | The evaluator hard-codes knowledge of every tuple shape the parser produces. Changing one component requires manually updating the other with no type system to catch mismatches. Define a shared `ast.py` module with typed node classes imported by both sides. |

---

## Risk 14 – No `break`, `continue`, or `return` Support

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | `Interpreter.run_program()` |
| **Notes** | Loops cannot exit early and functions cannot return mid-body. Developers work around this with boolean flag variables, increasing complexity and the likelihood of logic bugs. Implement a `ControlFlowSignal` exception hierarchy caught at the appropriate execution level. |

---

## Risk 15 – Unrestricted Variable Type Assignment

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | `Environment.set()` / `Environment.assign()` |
| **Notes** | Any Python object including `None`, functions, or lists can be stored in any variable. Operations on unexpectedly typed values surface as raw Python errors rather than interpreter-level messages, making them confusing for users. Add type validation on assignment and surface mismatches as interpreter errors. |

---

## Risk 16 – Hand-Rolled Character Scanner Instead of `re`

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | `Lexer.tokenize()` |
| **Notes** | The nested `while` loops are ~50 lines of imperative logic that is hard to read and extend. The equivalent written with `re.compile` and named groups is ~10 lines, and adding a new token type becomes a one-line change. |

---

## Risk 17 – No Docstrings or Inline Documentation

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | Entire codebase |
| **Notes** | No public method has a docstring describing its expected inputs, return value, or side effects. New contributors must read full implementations to understand intent, significantly increasing onboarding time. Add Google-style or NumPy-style docstrings and a top-level `README.md`. |

---

## Summary

| Severity | Count |
|---|---|
| 🔴 High | 6 |
| 🟡 Medium | 7 |
| 🟢 Low | 4 |
| **Total** | **17** |