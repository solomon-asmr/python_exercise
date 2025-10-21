import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
movie_titles = [movies.getText() for movies in soup.find_all(name="h3", class_="title")]
movie_titles.reverse()
# print(soup)
# print(movie_titles)
print(movie_titles)

with open('movies.txt', 'w', encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(movie + '\n')
