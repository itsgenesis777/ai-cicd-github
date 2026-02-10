<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Your First GitHub Actions AI workflow

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-cicd-github)

**Author:** that_genesis  
**Email:** john.gen.pamintuan@gmail.com

---

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_d2f6s4y1)

---

## Introducing Today's Project!

In this project, I'm going to build CI/CD Pipeline. CI/CD which stands for continuous integration and continuous delivery/deployment, aims to streamline and accelerate the software development lifecycle. GitHub Actions helps me automate the workflow—so every time I push code, it can automatically run checks (like linting and tests), build the app, and deploy it with less manual work.

### Key tools and concepts

The key tools I used in this project include Python, pytest for automated testing, virtual environments (venv) for dependency isolation, and GitHub Actions for continuous integration. The key concepts I learned include writing and running automated tests, setting up a CI pipeline that runs on every push, detecting bugs early through CI, packaging code, and using CI artifacts to store and share build outputs.

### Challenges and wins

This project took me approximately an hour to complete. The most challenging part was setting up the CI workflow and understanding how virtual environments and GitHub Actions work together, but working through it helped me better understand automated testing and CI pipelines.

### Why I did this project

I did this project today to learn how automated testing and continuous integration work in practice. It helped me understand how tests, CI pipelines, and artifacts fit together to catch bugs early and automate repetitive tasks. The project met my goals, and another skill I want to learn next is how to extend CI pipelines to include deployments and more advanced checks like linting and code coverage.

---

## Setting Up the Python Environment

In this step, I'm setting up my repository by forking and cloning the starter repository. This is important because I will be using placeholder code from this repository.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_m5v9b3x7)

### Activating the virtual environment

I activated my virtual environment by running the command .\venv\Scripts\Activate in PowerShell after creating it with python -m venv venv. When the terminal shows (venv) at the beginning of the prompt, it means the virtual environment is active and any Python packages installed or commands run will apply only to that project, not to the system-wide Python installation.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_p2w8n4r6)

### Exploring the project structure

The project includes app.py with core utility functions, a tests/ folder for test files, requirements.txt for dependencies, pyproject.toml for project configuration, and a .github/ folder for CI workflows.

---

## Writing and Testing a Python Function

In this step, I am writing a Python function with proper type hints and creating automated tests using pytest. I then run the tests locally to make sure the function works as expected. Writing tests is important because it helps catch bugs early, ensures the code behaves correctly, and makes future changes safer and easier to maintain.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_q8j4m1h6)

### Creating the multiply function

I wrote the multiply function by defining a Python function that takes two integers as parameters, a and b, and returns their product. I added type hints (int) to clearly specify the expected input and output types. Inside the function, I simply multiply the two values using the * operator and return the result. I also included a short docstring to describe what the function does.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_a6s2v5t8)

### Running and verifying tests

I verified my tests by activating the virtual environment and running pytest -v in the terminal. The output showed that all test cases passed without any errors, which confirmed that the functions behaved as expected.

---

## Building a CI Pipeline with GitHub Actions

In this step, I am creating a GitHub Actions workflow that automatically runs my tests every time I push code to the repository. I then intentionally break a test to confirm that the pipeline detects the failure, and fix it afterward to make sure the pipeline passes again. This shows how CI helps catch errors early and ensures code changes are tested automatically.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_g1k5n9r3)

### Configuring the workflow

I set up the CI workflow with GitHub Actions to automatically run tests on every push and pull request. The workflow installs Python, installs dependencies, and runs pytest to verify that the code works correctly.

### Testing the pipeline

CI caught the bug when I intentionally broke a test and pushed the change to the repository. The GitHub Actions workflow automatically ran the test suite and the pipeline failed because the test assertion did not pass. I fixed the issue by correcting the test logic and pushing the update, after which the pipeline passed successfully. This shows that CI helps automatically detect errors early and prevents broken code from being merged.

---

## Packaging Code with CI Artifacts

I am adding a build step to my CI pipeline that packages my Python code into an installable artifact. The pipeline will then upload this package so it can be downloaded and shared with the team. This makes it easier to distribute and reuse the code in a consistent way.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_n3m7k1w9)

### Adding build and upload steps

I added a build step to package the code and an artifact upload step to store the package so it can be downloaded later.Artifacts are useful because they allow the packaged code to be downloaded and shared without rebuilding it each time.

![Image](http://learn.nextwork.org/lively_azure_vibrant_badger/uploads/ai-cicd-github_s6p9c4v1)

### Downloading the packaged artifact

I learned that CI artifacts are files created by the CI pipeline that can be saved and downloaded after a workflow run. I was able to download my packaged Python code directly from GitHub Actions, which means my CI pipeline now not only runs tests but also produces a reusable build output that can be shared or used later without rebuilding it.

---

---
