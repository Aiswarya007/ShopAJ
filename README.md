# ShopAJ

ShopAJ is an e-commerce platform showcasing trending products. This repository contains automated tests for the platform using Python, Selenium, and Behave, following the Page Object Model (POM) design pattern. The project also integrates continuous integration/continuous deployment (CI/CD) pipelines for efficient delivery.

Features
--------
Automated Tests: Tests implemented using Selenium, Behave, and pytest.
Page Object Model (POM): A design pattern to separate the test code from the page-specific code.
CI/CD Integration: Continuous integration and deployment pipelines set up for automated builds and tests.
Allure Reports: Test execution reports are generated using Allure.

Prerequisites
-------------
Before running the project, ensure you have the following installed:
--> Python 3.x
--> Pip (Python package manager)

Installation
-------------
--> Clone the repository:
git clone https://github.com/your-username/ShopAJ.git
cd ShopAJ

--> Create a virtual environment:
python -m venv .venv

--> Activate the virtual environment:
Windows:
.venv\Scripts\activate
Linux/Mac:
source .venv/bin/activate

--> Install dependencies:
pip install -r requirements.txt

Running Tests
-------------
--> To run the automated tests, use the following command:
pytest --alluredir=allure-results

--> To generate the Allure report after tests have been executed:
allure serve allure-results

CI/CD Setup
-----------
The project is integrated with CI/CD pipelines to automate testing and deployment. Ensure your pipeline includes steps to:
--> Install dependencies.
--> Run the tests.
--> Generate Allure reports.

License
-------
This project is licensed under the MIT License.


## Demo Video

[Watch the video](https://drive.google.com/file/d/1WClAwWWexSU0x_rP28_ZC1Gsz921Gkou/view?usp=sharing)

