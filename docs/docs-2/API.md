# 📘 Symbolic Compression API Documentation

This document describes the available functions and macros in the symbolic compression system.

---

## 🧠 Core Functions

### `encode_symbolic(input_data: str) -> str`
Encodes symbolic data into a compressed binary format.

- **Input**: `input_data` – a symbolic program or number sequence (e.g. "⟦1,2,3⟧")
- **Returns**: A compressed binary or symbolic representation.
- **Example**:
  ```python
  encode_symbolic("⟦1,2,3⟧") → "101001"
  ```

---

### `decode_symbolic(encoded_data: str) -> str`
Decodes compressed symbolic or binary data back to its symbolic form.

- **Input**: `encoded_data` – compressed string from `encode_symbolic`.
- **Returns**: Original symbolic structure.
- **Example**:
  ```python
  decode_symbolic("101001") → "⟦1,2,3⟧"
  ```

---

## 🔁 Macro Folding

### `apply_macro_folding(symbolic_code: str) -> str`
Compresses symbolic code using macro folding rules.

- **Input**: Symbolic code with potential repeating patterns.
- **Returns**: Compressed form with macros substituted.
- **Example**:
  ```python
  apply_macro_folding("⟦1,2⟧⟦1,2⟧") → "MACRO_REPEAT_1"
  ```

---

## 🔍 Symbolic Validator

### `validate_symbolic(symbolic_code: str) -> bool`
Checks if the symbolic code is valid and follows system rules.

- **Returns**: `True` if valid, else `False`.
- **Use case**: Prevents malformed symbolic entries.

---

## 🧪 Unit Testing Interface

### `run_symbolic_tests()`
Runs all predefined symbolic compression and expansion tests.

- **Output**: Summary of test results and pass/fail metrics.
- **Purpose**: Used in CI/CD to maintain system integrity.

---

## 📂 File Utilities

### `load_sym_file(file_path: str) -> str`
Reads a `.sym` symbolic program file.

### `save_sym_file(file_path: str, data: str)`
Saves symbolic data to a `.sym` file.

---

## 📌 Constants

```python
MACRO_PI    = ⟦2,2⟧ ÷ ⟦7⟧
MACRO_SQRT2 = ⟦9,9⟧ ÷ ⟦7,0⟧
MACRO_PHI   = ⟦8,9⟧ ÷ ⟦5,5⟧
```

---

## 📜 Notes

- The system **rejects decimals and negatives**.
- Compression rates can exceed **90%** and are measurable in benchmark tests.
- Mirrored symbolic digits: `1 ↔ 11`, `2 ↔ 12`, etc.
- Encoded output is **fully reversible and lossless**.

---

## 📎 Related Files

- `src/encoder.py` — Main compression logic
- `examples/` — Sample symbolic programs
- `tests/` — Unit and regression tests
- `benchmark/` — Performance logs

---