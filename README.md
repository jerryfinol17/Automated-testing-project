Automated Web Testing Framework with Selenium and PytestA beginner-friendly QA automation project demonstrating end-to-end (E2E) testing for the SauceDemo e-commerce demo app (https://www.saucedemo.com/). This framework uses the Page Object Model (POM) for maintainable tests, covering login scenarios (successful and error cases), inventory management (add/sort), cart operations (add/remove/verify), and full checkout flows. Built with Python, Selenium, and Pytest for modular, scalable testing. Includes data-driven tests, cross-browser support (Firefox/Chrome), and advanced reporting.

[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.35-green)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/pytest-8.4-orange)](https://pytest.org/)

## Overview
Goal: Automate key user flows like authentication, product sorting/adding to cart, item management, and complete checkout processes.
App Under Test: SauceDemo – a sample e-commerce site for testing login, inventory, cart, and checkout.
Current Coverage: 12+ tests (4 login variants, 4 inventory flows, 4 cart/E2E checkouts) with data-driven parametrization and ~90% pass rate.
Run Environment: Firefox/Chrome (headless for CI; non-headless for local debugging) via WebDriver Manager (no manual driver setup needed).
Scalability: Easy to extend with more browsers, APIs, or mobile emulation.


## Tech Stack
Languages/Tools: Python 3.9+, Selenium WebDriver, Pytest, WebDriver Manager.
Reporting: Pytest-HTML (basic logs) + Allure (interactive dashboards with steps, timelines, and screenshots).
Design Pattern: Page Object Model (POM) for clean separation of locators, actions, and config.
CI/CD: GitHub Actions for automated runs on push/PR, with report artifacts.
Other: Data-driven testing via @pytest.mark.parametrize, explicit waits for stability.

automated-testing-project/
├── config/
│   ├── config_for_login_page.py     # Test credentials (standard_user, locked_out, invalid, empty)
│   ├── config_for_inventory_page.py # Product locators and details (add/remove selectors)
│   └── config_for_cart_page.py      # Cart product mappings (display names, actions)
├── pages/
│   ├── login_page.py                # Login actions (open, enter creds, error handling, logout)
│   ├── inventory_page.py            # Inventory actions (add single/multi, sort by price, badge count, go to cart)
│   ├── cart_page.py                 # Cart verification (get items, remove, badge, start checkout)
│   └── checkout_page.py             # Checkout steps (fill info, continue, complete)
├── tests/
│   ├── test_login.py                # Login tests (success, errors)
│   ├── test_inventory.py            # Inventory tests (add, multi-add, sort, prices)
│   └── test_cart.py                 # Cart and E2E tests (verify, remove, checkout)
├── reports/                         # Generated HTML reports (run pytest to create)
├── allure-results/                  # Raw Allure data (auto-generated)
├── allure-report/                   # Generated Allure HTML dashboard
├── docs/                            # Screenshots and docs (e.g., report_screenshot.png)
├── requirements.txt                 # Dependencies (selenium, pytest, allure-pytest, etc.)
├── .github/workflows/ci.yml         # GitHub Actions for CI/CD
└── README.md                        # You're reading it!
Quick StartClone the Repo:

git clone https://github.com/your-username/automated-testing-project.git
cd automated-testing-project

Install Dependencies:

pip install -r requirements.txt

Run Tests:All tests: pytest tests/ -v
With HTML report: pytest tests/ --html=reports/report.html --self-contained-html -v
With Allure: pytest tests/ --alluredir=allure-results -v then allure serve allure-results
Specific test: pytest tests/test_cart.py::test_full_e2e_checkout -v
Cross-browser (if marked): pytest -m cross_browser -v

View Reports:HTML: Open reports/report.html in your browser for logs and pass/fail summaries.
HTML Report Example
Allure: Run allure serve allure-results for an interactive dashboard (timelines, steps, attachments). Example screenshot:
Allure Dashboard
Tests CoveredLogin (test_login.py): Successful login, locked-out user, invalid credentials, empty username (4 tests).
Inventory (test_inventory.py): Add single product to cart, multi-add products, sort by price (lo-hi/hi-lo), validate prices (4 tests).
Cart & E2E (test_cart.py): Verify cart items/badge, remove single/all items, start checkout, full E2E checkout (parametrized with user data) (4+ tests).

All tests include asserts for URLs, elements, text, and edge cases. Data-driven for efficiency (e.g., multiple products/usernames).

CI/CD IntegrationGitHub Actions runs tests on every push/PR to main.
Artifacts: Download allure-report or html-report from Actions tab for post-run analysis.
Badges update automatically for build status.

Contributing & Next StepsFork, PRs welcome! Add more tests (e.g., responsive checks) or browsers.
For production: Integrate coverage (pytest-cov) or parallel runs (pytest-xdist).
Questions? Open an issue.

![html report.png](docs/html%20report.png)
![Screenshot 2025-09-29 145456.png](docs/Screenshot%202025-09-29%20145456.png)
Built by Jerry Finol | Last Updated: September 29, 2025

