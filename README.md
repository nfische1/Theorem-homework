# Theorem-homework
Set up
===
```
Make sure python is installed on your machine 
```
```
For MacOS

```
1 Install Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2 Install pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
and then run
```
python get-pip.py
```

3 Install pytest
```
pip install -U pytest --ignore-installed
```
4 Install Webdriver Manager (for frontend testing)
```
pip install webdriver manager
```
5 Install chromedriver
```
brew install chromedriver
```
6 Add chromedriver to path 
```aidl
PATH=/bin:/usr/local/bin:${PATH}
```
7 Install all other requirements
```
pip install -r requirements.txt
```

```
For Windows

```

2 Install pip
Here is a complete link for troubleshooting https://phoenixnap.com/kb/install-pip-windows

in a terminal, run
```
python get-pip.py
```
3 Install pytest. 
Link is below for troubleshooting https://docs.pytest.org/en/stable/getting-started.html
```
pip install -U pytest --ignore-installed
```
4 Install Webdriver Manager (for frontend testing)
```
pip install webdriver manager
```
5 Install chromedriver
http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-windows-install/

6 Add chromedriver to path
```aidl
PATH=/bin:/usr/local/bin:${PATH}
```
7 Install all other requirements
```
pip install -r requirements.txt
```

8 You will need to install:
* Chrome or Firefox for Web UI

8 Make sure Library folder permissions are set to Read & Write for everyone on the machine, and that you've applied the permissions to all enclosed items.
This is for the xml reports. If you do not have these permissions, you will get an error like this:
```
OSError: [Errno 30] Read-only file system: '/test-reports'
```
Running Tests
===
Test Runs
---
Running ALL Tests:
```
pytest -q  tests -s
```
Running ONE SINGLE Test:
```
pytest -q  tests/login/test_login.py -s
```
Running All Tests in a directory:
```
pytest -q  tests/login -s
```

Running Backend tests with XML and Logging Output
---
Run with pytest with additional arguments for xml report:

```
--junitxml=<path to test-reports folder>/name_of_file_junit.xml
```
Example:

```
--junitxml=../test-reports/dev_run_junit.xml
```

Enable the logging:

```
log_cli=true
```
Frontend tests are recorded through the screenshot functionality
===

IntelliJ Setup
===
1 Go to IntelliJ IDEA main menu > Preferences > Plugins/. Install Python Community Edition

2 Go to File > Project Structure > Platform Settings > SDKs and click the + and add Python SDK. 

3 In Project Structure, select Project Settings > Project and define the Project SDK to Python

4 In Project Structure, select Project Settings > Modules and define the Interpreter as Python.

Save and restart if necessary.

REPORTS
```
---------------------------------------LESSONS LEARNED ---------------------------------------------------------------------
```
MAIN OBJECTIVE 
```
I would have tweaked the main objective of this project to prioritize a single end to end test.
This would effectively demonstrate the functionality of the website. Most importantly, it would verify that a product could be checked out. 
```

TAKEAWAYS
```
This project helped me learn that I need to focus on simplifying my testing process. 
Simply knowing how to make tests is not enough if you have a client with a deadline, or a budget constraint. 
If I were to do this test all over, I would focus on the main tests themselves, instead of trying to setup an entire infastructure in 8 hours. 

```
EXPANDING 

```
Steps I would take if I were to continue testing this website.
 1. I would modify my initial testing plan to prioritize the checkout process.
 2. I would create value by provide both backend and frontend tests to cover end to end functionality. 
 3. I would do database checks to verify data is being stored correctly for the products. 
```
