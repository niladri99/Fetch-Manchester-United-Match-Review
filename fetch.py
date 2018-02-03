
import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.manutd.com/en/Fixtures-And-Results/Match-Reports.aspx")
soup = BeautifulSoup(page.content, 'html.parser')

links = []

for div in soup.findAll('div', {'class': 'story'}):
	links.append(div.findAll('a'))

testtag = links[0][0]

nowstring = str(testtag)

postlink = nowstring.split("\"")
# print(postlink[1]) # this is the actual URL

article_link = postlink[1];

base_manu_url = "http://www.manutd.com"

article_page = requests.get(base_manu_url + article_link)
manu_soup = BeautifulSoup(article_page.content, 'html.parser')

# print(manu_soup.prettify()) # print the HTML of the article page

stories = ''

article = manu_soup.find('div', {'class': 'newsstory'}).findAll('p')
for eachp in article:
	stories += '\n' + ''.join(eachp.findAll(text=True))

print(stories)