# Test Assignment for ACT

## Generating Test Reports in HTML with html-pytest
1. Run the tests and generate a test report. 
The script will set up a virtual environment and install necessary dependencies if needed. 
```bash
./run_tests.sh
```
2. View the test results as an HTML file in the folder `report`

## Generating Test Reports with Allure
1. Install the Allure CLI if it is not already installed.
```bash
brew install allure 
```
2. Run the tests and generate a test report. 
The script will set up a virtual environment and install necessary dependencies if needed.
```bash
./run_tests.sh
```
3. Generate the Allure HTML report.
```bash
allure generate allre-results -o allure-html
```