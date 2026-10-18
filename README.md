# AI Coding Workflow Toolkit

A Python-based developer productivity toolkit for repository analysis, Python syntax validation, reusable development templates, and consistent AI-assisted coding workflows.

## Overview

The AI Coding Workflow Toolkit helps developers inspect repository structures, validate Python syntax, organize development tasks, and standardize code review and bug reporting.

It is designed to complement existing development tools while keeping developers in control of code quality, security, and implementation decisions.

## Key Features

- **Repository Analysis:** Summarize files, directories, file extensions, and Python files.
- **Python Syntax Checking:** Detect Python syntax errors using Python's built-in compilation utilities.
- **Automated Unit Tests:** Validate core functionality with the `unittest` framework.
- **Task Planning:** Organize requirements, implementation steps, and acceptance criteria.
- **Code Review Template:** Support consistent review of correctness, readability, and maintainability.
- **Bug Report Template:** Document reproduction steps, expected behavior, and actual results.
- **Workflow Configuration:** Store reusable development workflow settings in JSON.
- **Developer Documentation:** Keep workflow instructions and usage guidance organized.

## Technology Stack

- Python 3
- Git and GitHub
- JSON
- Markdown
- Python standard library (`unittest`, `py_compile`, `pathlib`)

## Project Structure

```text
AI-Coding-Workflow-Toolkit/
├── config/
│   └── workflow_config.json
├── scripts/
│   ├── analyze_repository.py
│   └── check_python.py
├── templates/
│   ├── task_plan.md
│   ├── code_review.md
│   └── bug_report.md
├── tests/
│   ├── test_analyzer.py
│   └── test_checker.py
├── workflows/
│   └── README.md
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible Python 3 version
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/amoltathesoftwareengineer/AI-Coding-Workflow-Toolkit.git
cd AI-Coding-Workflow-Toolkit
```

No third-party packages are required for the core scripts if `requirements.txt` contains only comments.

## Usage

### 1. Analyze a Repository

Run the analyzer against the current directory:

```bash
python scripts/analyze_repository.py .
```

This reports repository statistics and identifies Python files.

### 2. Check Python Syntax

```bash
python scripts/check_python.py .
```

This checks Python files for syntax errors without running the application code.

### 3. Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

The test suite checks repository analysis and Python syntax-checking functionality.

## Safety and Best Practices

- Review code before accepting AI-generated suggestions.
- Never expose credentials, API keys, or confidential repository content to unapproved services.
- Review scripts before running them against important repositories.
- Require confirmation before destructive file operations.
- Run automated tests before merging changes.

## Current Status

The core repository analyzer, Python syntax checker, reusable templates, workflow configuration, and unit tests are implemented.

The current version focuses on local development workflows and does not claim to provide a fully autonomous AI coding agent.

## Future Enhancements

- Continuous integration workflow examples
- Git change summaries and pull request assistance
- Repository health and quality checks
- Optional integrations with configurable AI providers
- Development metrics and reporting

## Author

**Amol Tathe**

- GitHub: https://github.com/amoltathesoftwareengineer
- Repository: https://github.com/amoltathesoftwareengineer/AI-Coding-Workflow-Toolkit

## License

See the `LICENSE` file for the applicable open-source license.
