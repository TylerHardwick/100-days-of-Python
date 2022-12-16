from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "linkedin Username"
PASSWORD = "Linkedin Password"

driver_service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service)



#Sign in
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3376998095&f_AL=true&f_E=2&f_WT=2%2C3&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
log_in_button = driver.find_element("link text", "Sign in")
log_in_button.click()
time.sleep(1)
username_field = driver.find_element("id", "username")
username_field.send_keys(USERNAME)
password_field = driver.find_element("id", "password")
password_field.send_keys(PASSWORD)
sign_in_button = driver.find_element("xpath", "/html/body/div/main/div[3]/div[1]/form/div[3]/button")
sign_in_button.click()
# Added sleep due to Captcha on Linked in
time.sleep(10)


def zoom_out():
# Set the focus to the browser rather than the web content
    driver.set_context("chrome")
# Create a var of the window
    win = driver.find_element("tag name", "html")
# Send the key combination
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")
    win.send_keys(Keys.CONTROL + "-")

# Set the focus back to content to re-engage with page elements
    driver.set_context("content")
    time.sleep(1)


zoom_out()
time.sleep(2)

# Save Listing
job_list = driver.find_elements("css selector", ".scaffold-layout__list-container li")
for item in job_list:
    item.click()
    try:
        time.sleep(0.2)
        save_button = driver.find_element("css selector", ".jobs-save-button span")
        if save_button.text == "Save":
            time.sleep(0.2)
            save_button.click()
            time.sleep(0.2)
        else:
            time.sleep(0.4)
            pass
        follow_button = driver.find_element("css selector", ".follow")
        time.sleep(0.2)
        if follow_button.text == "Follow":
            follow_button.click()
            time.sleep(0.2)
        else:
            time.sleep(0.2)
            pass

    except NoSuchElementException:
        pass


