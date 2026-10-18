
# Developer Workflow Guides

This directory documents repeatable workflows for everyday software development.

## 1. Start a Development Task

1. Open `templates/task_plan.md`.
2. Define the objective and technical requirements.
3. Identify the files that may need changes.
4. Break the work into small implementation steps.
5. Define how the changes will be tested.
6. Track completion using the checklist.

## 2. Review Code Before Merging

1. Inspect the code changes and understand their purpose.
2. Open `templates/code_review.md`.
3. Check correctness, readability, security, and performance.
4. Run the relevant automated tests.
5. Run the Python syntax checker:

   ```bash
   python scripts/check_python.py .
   ```

6. Record review findings and required changes.
7. Approve the changes only when the applicable checks pass.

## 3. Report and Investigate a Bug

1. Open `templates/bug_report.md`.
2. Describe the problem and the expected behavior.
3. Provide reproducible steps.
4. Include relevant error messages after removing secrets.
5. Investigate the likely root cause.
6. Implement a fix and add regression tests.
7. Verify the fix before closing the issue.

## 4. Inspect a Repository

Run:

```bash
python scripts/analyze_repository.py .
```

The analyzer reports:
- Total file count
- Directory count
- Python file count
- File extension statistics
- Python file paths

## 5. Validate Python Syntax

Run:

```bash
python scripts/check_python.py .
```

Review the output and correct any syntax errors before proceeding.

## 6. Run Automated Tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

Review all test results. A passing test suite helps validate expected behavior but does not guarantee the absence of every defect.

## Recommended Practice

- Make small, focused changes.
- Review generated or AI-assisted code before accepting it.
- Never commit passwords, API keys, or access tokens.
- Run relevant tests before merging changes.
- Document important technical decisions.
