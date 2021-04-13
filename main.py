# Botting Processes: A piece of software that executes commands or performs routine tasks without the users intervention
# Download Selenium driver: https://www.selenium.dev/downloads/ or pip install selenium
# For Windows:
# Chrome Driver (for Chrome): https://www.chromedriver.chromium.org
# Gecko Driver (for Firefox): https://github.com/mozilla/geckodriver/releases

# Access https://www.seleniumeasy.com/test/ to test the code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    # Using ChromeDriver, for Firefox, use webdriver.Firefox()
    # If chromedriver was not added to PATH, it needs to be pointed at inside the () below
    driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    # The "try" part is to close the popup ad that shows up when accessing the website
    # Read here: https://selenium-python.readthedocs.io/waits.html
    try:
        adElement = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="at-cv-lightbox-button-holder"]/a[2]')))
        # adElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="at-cv-lightbox-button-holder"]/a[2]')))
        adNoButton = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-button-holder"]/a[2]')
        adNoButton.click()

    finally:
        messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
        messageField.send_keys('Hello World!')
        showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
        showMessageButton.click()
        additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
        additionField1.send_keys('1')
        additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
        additionField2.send_keys('2')
        getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
        getTotalButton.click()
