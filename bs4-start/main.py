from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_home_page = response.text
soup = BeautifulSoup(yc_home_page, "html.parser")
article_tag = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for article in article_tag:
    text = article.getText()
    article_text.append(text)
    link = article.find("a").get("href")
    article_link.append(link)


print(article_text)
print(article_link)


article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvote)

max_value = max(article_upvote)
largest_number = article_upvote.index(max_value)
print(largest_number)
print(article_text[largest_number])
print(article_link[largest_number])
























# with open("website.html") as file:
#     content = file.read()
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.prettify())
# print(soup.a)