# SwagLabs Automation Framework (Python + Playwright + BDD + Allure)

This repository contains an **end-to-end automation testing framework** for [SwagLabs](https://www.saucedemo.com/)  
built using **Python**, **Playwright**, **Pytest-BDD**, and **Allure Reports**.

---

##  Project Structure
com.saucedemo.playwright.python/
│
├── Pages/ # Page Object Models (LoginPage, ProductsPage, CheckoutPage, etc.)
│ ├── init.py
│ ├── base_page.py
│ ├── login_page.py
│ ├── products_page.py
│ ├── checkout_page.py
│ └── order_complete_page.py
│
├── steps/ # Step definitions for BDD tests
│ ├── test_login_steps.py
│ └── test_order_steps.py
│
├── features/ # Gherkin BDD feature files
│ ├── login.feature
│ └── order.feature
│
├── conftest.py # Fixtures (browser, screenshot handling, allure attachments)
├── pytest.ini # Pytest configuration
├── requirements.txt # Python dependencies
└── README.md # This documentation

markdown
Copy
Edit

---

## Prerequisites

Before running the tests, make sure you have:

1. **Python 3.10+** installed  

2. **Node.js** (required for Playwright browsers)  

3. **Java 8+** (required for Allure Reports)  

4. **Allure Commandline** installed:
   ```bash
   npm install -g allure-commandline --save-dev
##Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/com.saucedemo.playwright.python.git
cd com.saucedemo.playwright.python
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install Playwright browsers:

bash
Copy
Edit
playwright install
▶ Running Tests
1️⃣ Run in Headed Mode with Allure Report
bash
Copy
Edit
pytest --headed --alluredir=reports
2️⃣ Run in Headless Mode
bash
Copy
Edit
pytest --alluredir=reports
📊 Viewing Allure Reports
After running tests, serve the Allure report:

bash
Copy
Edit
allure serve reports
This will:

Generate the HTML report

Open it in your default browser

Show test details, steps, and screenshots/videos for failed tests

#Screenshots & Videos
Local Storage
Screenshots of failed tests are stored in:

Copy
Edit
screenshots/
Example:

bash
Copy
Edit
screenshots/test_successful_login_with_valid_credentials.png
In Allure Reports
Open a failed test in the Allure report

Scroll to Attachments

You’ll see:

Screenshot → Click to view PNG

Video → Click to watch MP4 of the run

# Example BDD Scenario
features/login.feature

gherkin
Copy
Edit
Feature: Login to SwagLabs

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I login with valid credentials
    Then I should see the products page
Framework Highlights
✅ Playwright → Modern browser automation

✅ Pytest-BDD → Readable Gherkin syntax

✅ Page Object Model (POM) → Maintainable test code

✅ Allure Reporting → Rich HTML reports with screenshots/videos

✅ Headed & Headless modes supported
