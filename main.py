from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movies_titles = soup.find_all(name="h3")
movies_text = [movie.getText() for movie in reversed(movies_titles)]

print(movies_text)

with open("movies.txt", "w") as file:
    for movie in movies_text:
        file.write(f"{movie} \n")
