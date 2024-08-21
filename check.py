# pip install zenrows
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup


client = ZenRowsClient("817f0e70aaf5c3c70de65cb9c46f9f830c7c07f8")
url = 'https://www.cnesst.gouv.qc.ca/en'
params = {"js_render":"true"}
article_file = open('article.txt','w')

response = client.get(url, params=params)

# print(response.text)

html_soup = BeautifulSoup(response.text, 'lxml')

basicBody = html_soup.find('div', class_="basic__body")
print("basicBody")
# print(basicBody)
# print(basicBody.find("p").text)

#  # creating a list of all common heading tags
# heading_tags = ["h1", "h2", "h3"]
# tags_list = []
# tags_text = ''
# for tags in html_soup.find_all(heading_tags):
#     print("HERE IS THE TESTXXYYXYX")
#     tags_text = tags.text.strip()
#     print(tags_text)
#     tags_list = tags_list.append(tags_text)

# print(tags_list)
# article_file.write(tags_list)

# article = html_soup.find('div', attrs={'class': 'basic__body'}).find_all('p')
# article_text = ''
# articles = []
# for element in article:
#     article_text = article_text + '\n' + ''.join(element.findAll(text = True))
# articles.append(article_text)
# article_file.write(articles)

# article_file.close()