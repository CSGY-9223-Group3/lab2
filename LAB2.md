# Lab Two: Build

**Submission Deadline:** 21st October 9am EST

## Objective

In this lab, each group will set up a continuous integration (CI) pipeline with security best practices. This will include automating the build process, tests, integrating security checks, and establishing artifact provenance for secure builds.

---

## Part One: Setting up the CI Pipeline

### 1. Set Up Automated Builds with GitHub Actions

- **Task:** Use GitHub Actions to automate your build process. This should include running tests and security checks on every commit.
- **Reference:** [GitHub Actions Documentation](https://docs.github.com/en/actions)

### 2. Use Bazel for Building Docker Containers *(Optional)*

- **Task:** Use Bazel to build the final container image.
- **References:**
  - [Bazel Documentation](https://bazel.build/)
  - [Using Bazel to Build Container Images](https://docs.bazel.build/versions/main/tutorial/container.html)

### 3. Set Up Tests as Part of the CI Pipeline

- **Task:** Implement unit tests and integration tests for your code. Tests should have good coverage.
- **Requirements:**
  - Test cases must run automatically for every merge.
  - *(Optional)* Use Test Containers for integration tests.
- **Reference:** [Writing Tests in Python (Flask Testing)](https://flask.palletsprojects.com/en/2.0.x/testing/)

### 4. Security Team Task: GitHub Actions Security Hardening

- **Task:** The security team should review the security configuration of GitHub Actions and ensure that best practices are followed.
- **References:**
  - [GitHub Docs on Securing CI Pipelines](https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions)
  - [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)

### 5. Security Team Task: Set Up SAST, DAST, and Secret Scanning

- **Task:** Install and configure tools for Static Application Security Testing (SAST), Dynamic Application Security Testing (DAST), and secret scanning within the CI pipeline.
- **Tools to Use:**
  - **CodeQL for SAST:** [CodeQL Documentation](https://codeql.github.com/docs/)
  - **Trufflehog for Secret Scanning:** [TruffleHog GitHub Repo](https://github.com/trufflesecurity/trufflehog)
  - **DAST (Fuzzing) *(Optional):*** Implement DAST and/or fuzzing for your web app using OSS tools like ZAP or Atheris.
- **Objective:** The aim is to detect application vulnerabilities automatically.

### 6. Security Team Task: Artifact Attestation for Build Provenance

- **Task:** Use artifact attestations to establish the provenance of your builds using tools like in-toto. Implement only the first two points from the reference link.
- **Reference:** [GitHub Docs on Provenance and Build Security](https://docs.github.com/en/code-security/supply-chain-security/understanding-the-software-supply-chain/attesting-to-a-build)

---

## Part Two: Breaking the CI Pipeline Security

Once the lab tasks are completed, both teams will attempt to "break" their own CI pipeline by introducing vulnerabilities or issues that could disrupt the build, security, or integrity of the project. Some methods to explore include:

### 1. Commit Secrets to the Repository

- **Objective:** "Accidentally" commit sensitive information such as API keys or passwords and observe if the CI pipeline detects and raises an alert.

### 2. Manipulate CI Configuration Files

- **Objective:** Alter the CI configuration file to disable security checks or tests in such a way that the CI does not fail, but key security steps are skipped.

### 3. Bypass Linting/Formatting/SAST Checks

- **Objective:**
  - Disable or bypass linting, code formatting, or SAST checks by commenting them out or removing config files.
  - Check whether poorly formatted or problematic code can still be merged.

### 4. Exploit CI Pipeline Weaknesses

- **Objective:** Attempt to identify and exploit any weaknesses in the implementation of the CI pipeline.
- **Methods:**
  - Pretend to be a third party who sends a malicious PR:
    - Could be a feature implementation that hides a backdoor.
    - Could be a bug "fix" that does the slightly wrong thing.
    - Could be updating (but actually adding/replacing) dependencies.
- **Goal:** See what damage it can do.

**Note:** In addition to manual code review, the security hardening efforts implemented by the team should automatically block any exploit attempts that pass undetected through the code review process. Use the references provided below to defend against more advanced attacks and ensure the security of your pipeline.

---

## Submission

Complete all the tasks and submit a link to a Google Doc containing the write-up on Brightspace by **Monday (21st Oct) 9am EST**.

### Write-Up Requirements

#### Part One:

- **Summary:** A brief summary of each lab task completed.
- **Team Contribution:** Indicate which group member(s) worked on each task.

#### Part Two:

- **Exploit Summary:** A summary of the exploit attempts made on your CI pipeline.
- **Defense Mechanisms:** Briefly describe the attacks prevented on your own repository.
- **Fixes Implemented:** Describe the fixes that you implemented if any attack was successful.

---

## Additional References

- [Preventing Pwn Requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
- [Handling Untrusted Input in GitHub Actions](https://securitylab.github.com/resources/github-actions-untrusted-input/)
- [GitHub Actions Building Blocks](https://securitylab.github.com/resources/github-actions-building-blocks/)
- [GitHub Docs on Securing CI Pipelines](https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions)
- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)

---