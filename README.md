# 🛍️ E-Commerce Website Automation

This project demonstrates web automation of an e-commerce website using Python, Pytest and Selenium webdriver. 
The script simulates user interactions such as launching a browser, navigating to a site, and performing basic validations.
It includes structured test cases, configuration via fixtures, and reusable test components — focused on login functionality and scalable automation practices.

## 📁 Project Structure

```

Test\_automation/
├── tests/
│   ├── BaseTest.py             
│   └── conftest.py
│   ├── test_Register.py
│   ├── test_login.py
│   ├── test_Search.py                
├── pages/    # Page-level locators and methods                      
│   └── Account.py
│   └── Account_Success_Page.py   
│   └── BasePage.py
│   └── HomePage.py   
│   └── LoginPage.py
│   └── RegisterPage.py
│   └── Searchpage.py              
├──Utilities
│   └── ReadConfigurations.py
├── Configuration
│   └──config.ini

## 🔧 Tools & Technologies Used

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver**
- **PyCharm** (IDE)
- **Page Object Model (POM)** 

🔍 What the Script Does
Launches the Chrome browser
Opens a demo e-commerce website (https://tutorialsninja.com/demo/)
Performs interactions like:
Navigating to homepage
Searching products / accessing elements
Verifying page titles or URLs (depending on your code)
Validation of user login
validation of user registration fields
Verification on available products
Closes the browser

📌 This project helps understand the basics of Selenium WebDriver, element locators, and browser automation using Python.

## ✅ Features Implemented

* ✅ Login test case with valid and invalid credentials
* ✅ Pytest fixtures for browser setup and teardown
* ✅ Code reusability through function modularization
* ✅ Scalable test structure ready for extension
* ✅ Generating test results with allure reports
---
📌 Future Enhancements

* Add test data using external files (CSV/JSON)
* Cart and checkout test cases
* Integration with Jenkins for CI
* Cross-browser testing

## 👩‍💻 Author

**Vrinda MB**
💼 QA Engineer
