# QA Automation coding exercise

### Summary
This is a little Python Selenium project for an execise using the following tools:
* Python 3.11.3
* PyTest 7.4.0
* Selenium 4.10.0
* Allure-pytest 2.13.2

### How to use it
* Clone the repository:
    ```sh
    git clone https://github.com/nashoshinoda/qa-automation-coding-exercise-ignacio.git
    ```
* Install required modules using this command line:
    ```sh
    pip install -r requirements.txt
    ```
* Install developed modules with this command line:
    ```sh
    pip install -e .
    ```
* Run command **pytest** to execute the available test case.
* Run command **allure serve reports/html** to generate the HTML report once the test execution finished:
    ```sh
    allure serve reports/html
    Generating report to temp directory...
    Report successfully generated to C:\Users\IVELDE~1\AppData\Local\Temp\16445734970921447855\allure-report
    Starting web server...
    2021-06-19 14:06:09.114:INFO::main: Logging initialized @1697ms to org.eclipse.jetty.util.log.StdErrLog
    Server started at <http://ip:port/>. Press <Ctrl+C> to exit
    ```
    A new browser window will be automatically opened showing the results of the tests.

### Things to note:
* The idea of implement pytest markers but not suggested it to run the only test case is because I'm thinking in a future when more test cases will be included.
* The code was formatted using Black following the PEP 8 style guide for Python Code.
* Files messages and web_elements were designed to be used as constant variables and can keep increasing depending the needs of the app.