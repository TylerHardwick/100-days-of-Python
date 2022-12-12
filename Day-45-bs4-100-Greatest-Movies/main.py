from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_page = response.text
soup = BeautifulSoup(empire_page, "html.parser")

film_title = soup.find_all("h3", class_="title")




film_list = [film.getText() for film in film_title]
film_list.reverse()

with open("film_list.txt", "w", encoding="utf-8") as file:
    for film in film_list:
        file.writelines(f"{film}\n")
