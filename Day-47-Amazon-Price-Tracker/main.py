from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


headers= {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
}

amazon_link = "https://www.amazon.co.uk/Nintendo-Switch-OLED-Model-White/dp/B098TVDYZ3/ref=sr_1_2?keywords=nintendo+switch&qid=1670866463&sprefix=nin%2Caps%2C82&sr=8-2"

response = requests.get(amazon_link, headers=headers)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "lxml")
price = soup.find("span", id="priceblock_ourprice")
current_price = float(price.getText().strip("£"))
product = soup.find("span", id="productTitle")
product_name = product.getText()

my_email = "email@gmail.com"
my_password = "emailpass"

if current_price <= 285:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="toemail@gmail.com",
                            msg=f"Subject: Amazon Low Price Alert! \n\n Hey Tyler, {product_name} is currently £{current_price}! Buy now!\n {amazon_link}".encode("utf-8"))

        print("Msg sent")
