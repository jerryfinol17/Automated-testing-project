# Automated-testing-project
A beginner-friendly test automation project for web apps using Selenium and Pytest. It features simple, maintainable test scripts and GitHub Actions for CI/CD. Explore my Python and QA skills!  
# Automated Web Testing Framework with Selenium and Pytest

A beginner-friendly QA automation project demonstrating end-to-end (E2E) testing for the SauceDemo e-commerce demo app (https://www.saucedemo.com/). This framework uses the Page Object Model (POM) for maintainable tests, covering login scenarios (successful and error cases) and inventory/cart flows. Built with Python, Selenium, and Pytest for modular, scalable testing.

[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.35-green)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/pytest-8.4-orange)](https://pytest.org/)

## Overview
- **Goal**: Automate key user flows like user authentication, adding items to cart, and verifying cart contents.
- **App Under Test**: SauceDemo – a sample e-commerce site for testing login, inventory, and checkout.
- **Current Coverage**: 5 tests (4 login variants + 1 add-to-cart with cart verification).
- **Run Environment**: Firefox headless via WebDriver Manager (no manual driver setup needed).

## Tech Stack
- **Languages/Tools**: Python 3.9+, Selenium WebDriver, Pytest, Pytest-HTML (for reports).
- **Design Pattern**: Page Object Model (POM) for clean separation of page elements and actions.
- **Config**: Credentials managed in a separate config file for security.
- **Browser**: Firefox (headless mode for CI-friendly runs).

## Project Structure
