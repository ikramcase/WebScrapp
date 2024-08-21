# pip install zenrows
from zenrows import ZenRowsClient
from lxml import html
from bs4 import BeautifulSoup


client = ZenRowsClient("817f0e70aaf5c3c70de65cb9c46f9f830c7c07f8")
params = {"js_render":"true"}
article_file = open('article.txt','w')

with open('output.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i])
        website_url = lines[i]
        print(website_url)
      
        response = client.get(website_url, params=params)

        print("here is the client response from zenrows : ",response)
        webpage = html.fromstring(response.content)
        html_soup = BeautifulSoup(response.text, 'lxml')
        # print(html_soup)
        
        # creating a list of all common heading tags
        heading_tags = ["h1", "h2", "h3"]
        tags_list = []
        tags_text = ''
        for tags in html_soup.find_all(heading_tags):
            tags_text = tags_list.append(tags.name + ' -> ' + tags.text.strip())
            tags_list.append('\n')
        article_file.write(tags_text)

        article = html_soup.find('div', attrs={'class': 'basic__body'}).findAll('p')
        article_text = ''
        articles = []
        for element in article:
            article_text = article_text + '\n' + ''.join(element.findAll(text = True))
        articles.append(article_text)
        article_file.write(articles)

article_file.close()
f.close()