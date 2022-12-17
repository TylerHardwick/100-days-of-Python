from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

PROMISED_DOWN = 900
PROMISED_UP = 900
TWITTER_EMAIL = "Email here"
TWITTER_PASS = "Password here!"
TWITTER_USERNAME = "Username here"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.download_result = 0
        self.upload_result = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        cookie_btn = self.driver.find_element("id", "onetrust-accept-btn-handler")
        cookie_btn.click()
        time.sleep(1)
        start = self.driver.find_element("class name", "start-text")
        start.click()
        time.sleep(55)
        self.download_result = float(self.driver.find_element("css selector", ".download-speed").text)
        self.upload_result = float(self.driver.find_element("css selector", ".upload-speed").text)
        print(f"Download Speed: {self.download_result}\n Upload Speed: {self.upload_result}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        username = self.driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        verify_username = self.driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        verify_username.send_keys(TWITTER_USERNAME)
        verify_username.send_keys(Keys.ENTER)
        time.sleep(0.5)
        password = self.driver.find_element("xpath",'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(3.5)
        twitter_search_box = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div')
        twitter_search_box.click()
        time.sleep(0.6)
        twitter_search = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        twitter_search.send_keys(f"Hey ISP, why is my internet speed {self.download_result}mbps down/ {self.upload_result}mbps up when I am paying for {PROMISED_DOWN}mbps down/ {PROMISED_UP}mbps up? ")
        tweet_btn = self.driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.download_result < PROMISED_DOWN or bot.upload_result < PROMISED_UP:
    bot.tweet_at_provider()
