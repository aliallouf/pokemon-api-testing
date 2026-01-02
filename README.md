# 🐾 PokeAPI Automation Suite

A robust, production-ready API testing framework built with **Python** and **Pytest**. This project demonstrates automated validation of the [PokeAPI](https://pokeapi.co/), focusing on data integrity, error handling, and professional reporting.

---

## 🚀 Features

* **Automated API Testing**: Validates GET requests and JSON responses from a real-world API.
* **Data-Driven Testing**: Uses Pytest Parametrization to test multiple endpoints with a single test function.
* **Smart Assertions**: Checks status codes, data types, and specific nested JSON values.
* **Professional HTML Reports**: Generates visual dashboards for test results including execution time and failure details.
* **CI/CD Ready**: Configured for GitHub Actions to run tests automatically on every push.

---

## 🛠️ Tech Stack

| Tool | Purpose |
| :--- | :--- |
| **Python 3.12+** | Programming Language |
| **Pytest** | Testing Framework |
| **Requests** | API Client / HTTP Library |
| **Pytest-HTML** | Reporting Plugin |

---

## 📋 Prerequisites

Before running the tests, ensure you have Python installed. You can check your version by running:

```bash
python --version
## ⚙️ Installation & Setup
1. Clone the repository:
git clone [https://github.com/YOUR_USERNAME/pokemon-api-testing.git](https://github.com/YOUR_USERNAME/pokemon-api-testing.git)
cd pokemon-api-testing
2. Install dependencies:
pip install -r requirements.txt
## 🧪 Running the Tests
To execute the full suite and generate a self-contained report, run:
pytest --html=report.html --self-contained-html
## 📊 View the Report
After running the tests, open the report.html file in your preferred web browser.

✅ Green: Tests passed (API is behaving as expected).

❌ Red: Tests failed (Potential bug found in the API or data changed).
## 💡 Key Learnings
While building this project, I implemented several industry-standard testing patterns:

Fixtures: Used to manage the base URL and keep the code DRY (Don't Repeat Yourself).

Edge Case Testing: Specifically verifying 404 Not Found responses for non-existent resources.

JSON Schema Validation: Ensuring that required keys are present in the response body.
