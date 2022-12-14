from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element("id", "cookie")


def check_upgrades():
    money_scan = driver.find_element("id", "money")
    money = money_scan.text
    if "," in money:
        money = money.replace(",", "")
    store = driver.find_elements("css selector", "#store b")
    store_costs = [int(item.text.split("-")[1].replace(",", "")) for item in store[0:-1]]
    store_items = [item.text.split("-")[0].strip() for item in store[0:-1]]
    for num in range(len(store_items)):
        if int(money) > store_costs[::-1][num]:
            print(f"Buying {store_items[::-1][num]} for a cost of: {store_costs[::-1][num]}")
            buy_item = driver.find_element("id", f"buy{store_items[::-1][num]}")
            buy_item.click()
            global timeout
            timeout = time.time() + 3
            break


timeout_5_min = time.time() + 60*5
timeout = time.time() + 3

continue_clicking = True
while continue_clicking:
    cookie.click()

    # 3 sec timer
    if time.time() > timeout:
        check_upgrades()

    # 5 min timer (ends cookie bot)
    if time.time() > timeout_5_min:
        print("5 minutes passed. Ending test.")
        cps = driver.find_element("id", "cps")
        print(f"You ended with {cps.text}")
        break

driver.quit()