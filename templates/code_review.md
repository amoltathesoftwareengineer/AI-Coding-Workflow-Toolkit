
# Code Review Checklist

Use this checklist before merging code into the main branch.

## 1. Correctness

- [ ] The implementation meets the requirements.
- [ ] The code handles expected inputs correctly.
- [ ] Edge cases are considered.
- [ ] Errors and exceptions are handled appropriately.
- [ ] No unintended behavior has been introduced.

## 2. Code Quality

- [ ] Variable and function names are meaningful.
- [ ] Functions have a clear responsibility.
- [ ] Duplicate code is minimized.
- [ ] The code is readable and maintainable.
- [ ] Unnecessary complexity has been avoided.

## 3. Security

- [ ] No passwords, API keys, or tokens are committed.
- [ ] User inputs are validated where appropriate.
- [ ] Sensitive information is not exposed in logs.
- [ ] File operations are handled safely.
- [ ] Dependencies are reviewed for known risks.

## 4. Testing

- [ ] Relevant automated tests have been added or updated.
- [ ] Existing tests pass.
- [ ] Failure scenarios have been considered.
- [ ] Important boundary conditions are tested.

## 5. Performance

- [ ] Unnecessary repeated operations are avoided.
- [ ] Resource usage is reasonable.
- [ ] Potential performance bottlenecks are considered.

## 6. Documentation

- [ ] Public functions have useful documentation.
- [ ] README or relevant documentation is updated.
- [ ] Configuration changes are explained.
- [ ] Breaking changes are documented.

## 7. Review Summary

**Reviewer:** 

**Reviewed Commit / Pull Request:** 

**Decision:**
- [ ] Approved
- [ ] Changes requested
- [ ] Further investigation required

**Review Comments:**

Add findings, risks, and recommended improvements here.
