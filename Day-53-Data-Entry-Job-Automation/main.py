from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
FORM = "https://forms.gle/8RJNNFwFi63GSff1A"


class ZillowScrape:
    def __init__(self):
        headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
        }
        zillow_page = requests.get(ZILLOW_URL, headers=headers).text
        self.soup = BeautifulSoup(zillow_page, "lxml")

    def get_link_list(self):
        link_scrape = self.soup.select(".property-card-data .property-card-link")
        link_list = []
        for link in link_scrape:
            if "https" in link["href"]:
                link = link["href"]
            else:
                link = f"https://www.zillow.com{link['href']}"
            link_list.append(link)
        return link_list

    def get_price_list(self):
        price_scrape = self.soup.select("span[data-test=property-card-price]")
        price_list = []
        for item in price_scrape:
            if "+" in item.text:
                item = item.text.split("+")[0]
            elif "/" in item.text:
                item = item.text.split("/")[0]
            price_list.append(item)
        return price_list

    def get_address_list(self):
        address_scrape = self.soup.select(".property-card-link address")
        address_list = [address.text.replace("|", ",").strip() for address in address_scrape]
        return address_list


class FormBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    def fill_form(self, address, price, link):
        self.driver.get(FORM)
        time.sleep(3)
        for num in range(len(address)):
            time.sleep(2)
            address_input = self.driver.find_element(
                "xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(address[num])

            price_input = self.driver.find_element(
                "xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(price[num])

            link_input = self.driver.find_element(
                "xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(link[num])
            time.sleep(0.5)
            submit = self.driver.find_element(
                "xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()
            time.sleep(2)
            resubmit = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            resubmit.click()



zillow_bot = ZillowScrape()
address_list = zillow_bot.get_address_list()
price_list = zillow_bot.get_price_list()
link_list = zillow_bot.get_link_list()

form_bot = FormBot()
form_bot.fill_form(address_list, price_list, link_list)












