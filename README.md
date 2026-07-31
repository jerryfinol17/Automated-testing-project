# 🧪 Selenium Automation Framework

### Clean End-to-End Automation with Selenium, Python & Allure Reporting

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)

---

## About the Project

This repository showcases how I build structured, maintainable automation frameworks using **Selenium**, **Python**, and the **Page Object Model (POM)**.

While my recent work primarily focuses on Playwright, this project represents the engineering foundations that continue to influence how I design automation today.

Built around a complete e-commerce workflow, the framework demonstrates clean architecture, reusable components, centralized configuration, cross-browser execution, and professional reporting with **Allure**.

The application itself is simply the case study.

**The engineering principles are the real project.**

---

## Why I Built It

Every automation engineer has a framework that teaches them the importance of maintainability.

For me, this was one of those projects.

Rather than simply automating user interactions, I wanted to understand how automation frameworks should be organized so they remain readable, reusable, and easy to extend over time.

Many of the architectural decisions I still use today were first explored here.

---

## Highlights

- Production-ready Page Object Model architecture
- Reusable `BasePage` implementation
- Centralized configuration and locators
- Cross-browser execution
- Data-driven testing
- Automatic screenshots on failure
- Allure Reporting
- GitHub Actions CI/CD
- Scheduled workflow execution
- Scalable folder organization

---

## What This Framework Covers

The automation validates complete business workflows including:

- Authentication
- Product browsing
- Shopping cart
- Checkout
- Order confirmation
- Positive scenarios
- Negative scenarios
- Cross-browser validation

Rather than validating isolated pages, the framework reproduces realistic customer journeys while maintaining a clean and organized automation architecture.

---

## Repository Structure

```text
.
├── .github/
├── config/
├── pages/
├── test/
├── screenshots/
├── allure-results/
├── requirements.txt
└── conftest.py
```

A detailed explanation of the framework architecture, design decisions, reporting strategy, and engineering principles is available in **ARCHITECTURE.md**.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/jerryfinol17/selenium-automation-framework.git

cd selenium-automation-framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete test suite:

```bash
pytest -q
```

Generate and open the Allure report:

```bash
allure serve allure-results
```

---

## Continuous Validation

Quality shouldn't only be verified when new code is written.

This repository includes **GitHub Actions** workflows that automatically execute the framework on pushes and scheduled runs to ensure it remains healthy as dependencies and the surrounding ecosystem continue evolving.

Software changes.

Browsers change.

Automation should evolve with them.

---

## Why This Repository Matters

This repository demonstrates more than Selenium knowledge.

It reflects how I approach automation engineering:

- Clean architecture over quick scripts
- Maintainability over complexity
- Readable code over clever code
- Reusable components
- Reliable automation
- Actionable reporting

Although I now build most new frameworks with Playwright, the engineering principles explored here remain exactly the same.

Tools evolve.

Good engineering principles don't.

---

## Technical Documentation

This repository includes a dedicated engineering document covering the framework in depth.

Topics include:

- Architecture decisions
- Page Object Model implementation
- Design patterns
- Reporting strategy
- CI/CD pipeline
- Cross-browser execution
- Lessons learned

📖 **Read the full documentation:** `ARCHITECTURE.md`

---

## Looking for a Custom Automation Framework?

I help startups and software teams build reliable automation solutions through:

- Playwright (Python & TypeScript)
- Selenium
- REST API Testing
- CI/CD Integration
- Automation Framework Design
- Analytical Testing
- UX-Oriented QA Reviews




---
## Let's Connect

<p align="center">

<a href="mailto:jerrytest124@gmail.com">📧 Email</a> •
<a href="https://linkedin.com/in/jerry-finol">💼 LinkedIn</a> •
<a href="https://jerryfinol17.github.io/JerryFinolQA/">🌐 Portfolio</a>

<br><br>

<a href="https://x.com/JerryFinolQA">𝕏 X</a> •
<a href="https://www.reddit.com/user/Jerry_Finol17/">👽 Reddit</a> •
<a href="https://www.instagram.com/jerryfinolqa/">📷 Instagram</a>
<a href="https://www.facebook.com/JerryFinolQA">📘 Facebook</a>
---


> **Understand first. Test second. Explain always.**



