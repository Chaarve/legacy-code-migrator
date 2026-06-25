# Multi-Agent Code Migration Pipeline

A 3-agent AI pipeline that automatically migrates legacy source code (Java, COBOL, JCL) to modern languages (Python, Go) using LangChain and a Groq-hosted LLM.

## Overview

The pipeline chains three specialized agents — **Analyzer → Migrator → Validator** — each with its own tools. If validation fails, the Migrator automatically re-runs with the validator's feedback, up to 3 times.

```
Source File
    │
    ▼
🔍 Analyzer Agent   →  Migration Brief
    │
    ▼
🔄 Migrator Agent   →  Migrated File
    │
    ▼
✅ Validator Agent  →  PASS / FAIL
    │                       │
    └──── (retry up to 3x) ◄┘
```

## Requirements

```bash
pip install langchain langchain-openai openai ipywidgets
```

- Python 3.8+
- A [Groq](https://console.groq.com) API key
- Jupyter Notebook / JupyterLab

## Setup

1. Clone or download the notebook.
2. Set your Groq API key in the notebook:
   ```python
   GROQ_API_KEY = "your-key-here"
   ```
3. Run all cells in order.

## Agents & Tools

### 🔍 Analyzer Agent
Reads and analyzes the source file before migration.

| Tool | Description |
|---|---|
| `analyzer_read_file` | Reads the source file with metadata (size, line count, content) |
| `detect_language` | Identifies source language and suggests migration target |
| `extract_structure` | Extracts classes, methods, and imports |
| `assess_complexity` | Rates complexity (Simple / Medium / Complex) and checks for error handling, file I/O |

Outputs a **Migration Brief** passed to the Migrator.

### 🔄 Migrator Agent
Converts source code to the target language following language-specific rules.

| Tool | Description |
|---|---|
| `migrator_read_file` | Reads the original source file |
| `get_migration_rules` | Fetches conversion rules for the language pair (e.g. Java → Python type mapping, naming conventions) |
| `write_migrated_file` | Writes the final migrated file, stripping any markdown fences |

### ✅ Validator Agent
Verifies the migrated code is correct and complete.

| Tool | Description |
|---|---|
| `validator_read_file` | Reads the migrated file |
| `check_syntax` | Compiles the Python file to check for syntax errors |
| `run_python_code` | Executes the file and captures stdout/stderr (15s timeout) |
| `compare_structures` | Compares class/method counts between original and migrated file |

Ends every response with `VERDICT: PASS` or `VERDICT: FAIL` + issue list.

## Supported Languages

| Source | Target | Extensions |
|---|---|---|
| Java | Python | `.java` |
| COBOL | Python | `.cob`, `.cbl`, `.cpy` |
| JCL | Go | `.jcl` |

## Usage

### Migrate a single file

```python
result = run_multi_agent_pipeline(
    input_path="./app/BankApp.java",
    output_dir="./migrated"
)
print(result["status"])  # "PASS" or "BEST_EFFORT"
```

### Migrate an entire folder

```python
results = migrate_folder(
    input_dir="./legacy_code",
    output_dir="./migrated"
)
```

The migrated files mirror the original folder structure under `output_dir`.

## Return Values

`run_multi_agent_pipeline` returns a dict:

```python
{
    "input":      "/path/to/BankApp.java",
    "output":     "/path/to/migrated/bankapp.py",
    "status":     "PASS",           # or "BEST_EFFORT"
    "time":       "42.3s",
    "analysis":   "...",            # Analyzer agent output
    "validation": "...",            # Validator agent output
}
```

## Configuration

| Variable | Default | Description |
|---|---|---|
| `MAX_RETRIES` | `3` | Max validation + re-migration attempts |
| `temperature` | `0.2` | LLM temperature (lower = more deterministic) |
| `max_tokens` | `4096` | Max tokens per LLM response |
| Model | `llama-3.3-70b-versatile` | Groq model used |

## Notes

- The validator runs the migrated code in a subprocess with a **15-second timeout**. Make sure migrated files don't have long-running side effects.
- `BEST_EFFORT` status means the pipeline exhausted all retries without a clean PASS — the file is still written and may be partially correct.
- The Groq API key in the original notebook is **hardcoded and should be rotated** before sharing the notebook.
