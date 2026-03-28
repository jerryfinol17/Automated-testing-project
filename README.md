# Selenium + Python + POM Framework
**Production-Ready E2E Automation Framework with Allure | SauceDemo**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![Allure](https://img.shields.io/badge/Allure-FF0000?style=for-the-badge&logo=allure&logoColor=white)](https://allure.report)
[![GitHub Actions](https://github.com/jerryfinol17/selenium-python-saucedemo-pom-framework/actions/workflows/main.yml/badge.svg)](https://github.com/jerryfinol17/selenium-python-saucedemo-pom-framework/actions)
[![Coverage](https://img.shields.io/badge/Coverage-76.5%25-yellow?style=for-the-badge)](https://github.com/jerryfinol17/selenium-python-saucedemo-pom-framework)

A clean, maintainable **End-to-End automation framework** built with **Selenium + Python + Page Object Model (POM)** and **Allure Reporting**.

Designed with production standards in mind: reusable components, centralized configuration, beautiful reporting, and CI/CD ready.

---

### ✨ Key Features

- **Page Object Model** with reusable `BasePage` class
- Centralized locators and configuration
- Cross-browser testing (Firefox + Edge)
- **Allure Reporting** with automatic screenshots on failure
- Data-driven tests (positive + negative scenarios)
- CI/CD pipeline with GitHub Actions

---

### 🏗️ Project Structure

```bash
selenium-python-saucedemo-pom-framework/
├── pages/           # Page Objects (BasePage, LoginPage, InventoryPage...)
├── test/            # Test suites
├── config/          # Locators and configuration
├── screenshots/     # Automatic failure screenshots
├── allure-results/  # Allure raw data
├── .github/workflows/ # CI/CD pipeline
├── requirements.txt
└── conftest.py
```

### 🚀 Quick Start
```bash
git clone https://github.com/jerryfinol17/selenium-python-saucedemo-pom-framework.git
cd selenium-python-saucedemo-pom-framework

# Virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Run tests
pytest -q

# Generate and open Allure report
allure serve allure-results
```

### Run Tests:
```bash
pytest test/ -v                               # Full suite
pytest --alluredir=allure-results -v          # With Allure
allure serve allure-results/                  # Open interactive report
```

###  Reporting 
**Allure Report**: Rich interactive dashboards with steps, timelines and screenshots
**Screenshots**: Automatically captured on test failure
**Coverage**: 76.5%

### Why This Framework?
This repository showcases my ability to build structured and maintainable Selenium frameworks using modern practices (POM, Allure reporting, and clean architecture).It complements my **Playwright** frameworks (Python & TypeScript) and demonstrates versatility across the two most used automation tools.

###   Services I Offer:
**QA Automation Enginee**r specialized in building production-ready frameworks.
Available services:Playwright frameworks (Python & TypeScript)
Selenium + Python frameworks
Migration from Selenium to Playwright
CI/CD integration + Allure reporting

Looking for a custom automation framework for your project?
Contact me → **jerrytareas17@gmail.com (mailto:jerrytareas17@gmail.com)**

Star  the repository if you find it useful!

Made with  for the QA Automation community.



