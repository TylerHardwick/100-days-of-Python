from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

TARGET_ACCOUNT = "Target_instagram_handle"
USERNAME = "Instagram Username"
PASSWORD = "Instagram Password"


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        cookies = self.driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookies.click()
        time.sleep(2)
        username_entry = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        username_entry.click()
        username_entry.send_keys(USERNAME)
        password_entry = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
        password_entry.click()
        password_entry.send_keys(PASSWORD)
        password_entry.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(2)
        followers = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        time.sleep(1)

    def follow(self):
        follower_list = self.driver.find_elements("css selector", "._aano button")
        for item in follower_list:
            item.click()
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

