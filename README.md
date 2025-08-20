# Saucedemo Automation Testing

This project contains automation tests for [Saucedemo](https://www.saucedemo.com/) using **Selenium** and **pytest**.
It is created as a QA portfolio project, covering login, add-to-cart,Checkout, and reporting.

---

## Project Structure

├── assets/ # Optional assets (screenshots, test data, etc.)

├── pages/ # Page Object Model (POM) classes for each page

├── tests/ # Test cases implemented with pytest

├── utils/ # Utility functions, config, driver setup, etc.

├── report.html # Test report in HTML format

└── requirements.txt # Python dependencies

---

## Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/Pandellll/saucedemo_automation.git
   cd saucedemo_automation
   ```

2. create a virtual environment & install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   ```

3. Run the tests with pytest
   ```bash
   pytest -v
   ```

---

## Test Report

To generate an HTML report after running the tests:
```bash
pytest --html=report.html
```

---

## Test Coverage

The following flows are covered in this automation suite:
- Login with valid and invalid credentials
- Adding items to the cart
- Checkout process with complete data
- Validation of error message and edge cases

---

## Tools & Technologies

- Python 3.13.3
- Selenium WebDriver
- pytest
- pytest-html (for test reporting)

---

## How to Extend

- Add new test cases under `test/`
- Add new Page Objects under `pages/`
- Add reusable functions under `utils/`
After updates, run the test suite again amd check the updated `report.html`.

--- 

## Notes

- The `assets/` folder can be used for screenshots, locators, or test data.\
- Always update `requirements.txt` when adding new dependencies

---

This repository is intended for learning and QA automation portfolio purposes.
