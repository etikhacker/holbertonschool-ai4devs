# Risk Assessment
## Project: `legacy_code_interpreter` — `holbertonschool-ai4devs`

> Identified risks in the legacy codebase, each with severity, precise location,
> concrete impact, and a recommended remediation step.

---

## Risk Table

| # | Risk | Severity | Location | Impact | Recommendation |
|---|---|---|---|---|---|
| 1 | No division-by-zero guard | **High** | `Interpreter.evaluate()` | Any expression like `x / 0` raises an unhandled `ZeroDivisionError` that crashes the entire interpreter process with no user-facing message | Add `if right == 0: raise RuntimeError("Division by zero")` before the `/` operation |
| 2 | Infinite loop with no timeout or iteration cap | **High** | `Interpreter.run_program()` — `WHILE` branch | A `while 1:` or any non-terminating condition hangs the interpreter permanently, blocking the process and requiring a manual kill | Introduce a `MAX_ITERATIONS = 100_000` counter; raise `RuntimeError("Loop exceeded max iterations")` when exceeded |
| 3 | Silent `None` return on unrecognised AST node | **High** | `Interpreter.evaluate()` — missing `else` clause | When an unknown node type is evaluated, `None` is silently returned and passed into further arithmetic, producing confusing `TypeError: unsupported operand type NoneType` far from the actual fault | Add a final `else: raise RuntimeError(f"Unknown AST node: {node[0]}")` |
| 4 | No input sanitisation or safe error recovery in Lexer | **High** | `Lexer.tokenize()` | A single unexpected character (e.g. `@`, `$`) raises a bare Python `SyntaxError` with no line/column info and aborts tokenisation of the entire source, giving the user nothing useful to act on | Collect all lexical errors with positions and report them together instead of raising immediately |
| 5 | Missing unit tests across all layers | **High** | Entire codebase | With zero test coverage, any change to the Lexer, Parser, or Evaluator can silently break existing behaviour; bugs are only discovered at runtime by end users | Add `pytest` test suites for each layer; target at least 80 % coverage before further development |
| 6 | Scope mutation inconsistency (`set` vs `assign`) | **High** | `Environment` class | Calling `set()` on a name that already exists in a parent scope creates a shadow variable in the local scope instead of updating the outer binding; programs that rely on outer-variable mutation produce wrong results with no error | Rename `set()` to `define()` for new bindings; make `assign()` the sole method for updating any existing binding |
| 7 | Fragile positional tuple access for AST nodes | **Medium** | `Parser` output consumed by `Interpreter.evaluate()` | Nodes are accessed by raw index (`node[2]`, `node[3]`); if any parser change shifts the tuple layout, the evaluator raises a cryptic `IndexError` with no indication of which node type caused it | Replace tuples with `dataclasses` or `typing.NamedTuple` so fields have names (`node.left`, `node.right`) and type mismatches surface early |
| 8 | No error recovery in the parser | **Medium** | `Parser.parse_expression()` and call chain | The first syntax error immediately aborts parsing; users must fix one error, re-run, find the next, and repeat — a poor developer experience and slow feedback cycle | Implement a synchronisation strategy (skip to the next statement delimiter `;` or newline) so the parser can report multiple errors in one pass |
| 9 | Recursive scope lookup vulnerable to stack overflow | **Medium** | `Environment.get()` and `Environment.assign()` | Programs with deeply nested function calls (>~950 levels on CPython) trigger Python's own `RecursionError`, which leaks implementation details to the user | Rewrite both methods as iterative loops traversing the `parent` chain |
| 10 | Hardcoded global `KEYWORDS` set | **Medium** | `Lexer.tokenize()` — module level | Any module that imports the lexer can accidentally mutate `KEYWORDS`; adding a new reserved word requires hunting for the global rather than changing a single configuration point | Move `KEYWORDS` to a class constant or inject it as a constructor parameter |
| 11 | No float or string literal support | **Medium** | `Lexer.tokenize()` — digit and character branches | Source code containing `3.14` is tokenised as two integers separated by an `OP` dot, silently producing wrong values; string literals are tokenised character-by-character as identifiers with no error | Extend the lexer to recognise float patterns (`\d+\.\d+`) and quoted string literals before the integer branch fires |
| 12 | No logging or structured execution tracing | **Medium** | All interpreter stages | When the interpreter fails, there is no record of what source was being evaluated, which statement caused the failure, or what variable values were in scope — diagnosing bug reports is extremely slow | Integrate Python's `logging` module; emit `DEBUG`-level traces at each eval step and `ERROR`-level entries on all raised exceptions |
| 13 | Tight coupling between Parser tuple format and Evaluator | **Medium** | `Parser` ↔ `Interpreter` interface | The evaluator contains explicit knowledge of every tuple shape the parser produces; changing one requires manually updating the other with no compiler or type system to catch mismatches | Define a shared `ast.py` module with typed node classes that both components import, making the contract explicit |
| 14 | No `break`, `continue`, or `return` control flow | **Low** | `Interpreter.run_program()` | Loops cannot exit early and functions cannot return mid-body; developers working around this write convoluted boolean flags that increase complexity and introduce subtle bugs | Implement a `ControlFlowSignal` exception hierarchy (`BreakSignal`, `ReturnSignal`) caught at the appropriate execution level |
| 15 | Unrestricted variable type assignment | **Low** | `Environment.set()` / `Environment.assign()` | Any Python object — including `None`, functions, or lists — can be stored in a variable; operations on mixed types produce raw Python error messages rather than interpreter-level ones | Add optional type annotations to variable declarations and validate on assignment; surface type mismatches as interpreter errors |
| 16 | Hand-rolled character scanner instead of `re` | **Low** | `Lexer.tokenize()` | The nested `while` loops are ~50 lines of imperative logic that is difficult to read, test in isolation, or extend with new token types; the equivalent using `re.compile` with named groups is ~10 lines | Rewrite the tokeniser using a compiled `re` pattern list; each pattern maps to a token type, making adding new tokens a one-line change |
| 17 | No inline documentation or docstrings | **Low** | Entire codebase | New contributors cannot determine the expected input format, return type, or side effects of any public method without reading the full implementation; onboarding time is significantly higher than necessary | Add `Google-style` or `NumPy-style` docstrings to all public methods and a top-level `README.md` describing the interpreter architecture |

---

## Severity Breakdown

| Severity | Count | Proportion |
|---|---|---|
| 🔴 High | 6 | 35 % |
| 🟡 Medium | 7 | 41 % |
| 🟢 Low | 4 | 24 % |

---

## Top 5 Priority Fixes (Recommended Remediation Order)

| Priority | Risk | Effort | Impact |
|---|---|---|---|
| 1 | Add division-by-zero guard | Very Low (1 line) | Prevents hard interpreter crash |
| 2 | Add `while` loop iteration cap | Low (5 lines) | Prevents process hang |
| 3 | Add `else` error clause in `evaluate()` | Very Low (2 lines) | Eliminates silent `None` propagation |
| 4 | Write unit tests for Lexer, Parser, Evaluator | Medium (1–2 days) | Safety net for all future changes |
| 5 | Refactor AST tuples to `dataclasses` | Medium (half-day) | Removes the root cause of risks 7 and 13 simultaneously |