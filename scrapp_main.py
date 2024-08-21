# pip install zenrows
from zenrows import ZenRowsClient
from lxml import html
from bs4 import BeautifulSoup
import time

# web_url = "https://www.cnesst.gouv.qc.ca/en"

with open('out.txt') as f:
    lines = f.readlines()
    # print(lines)
    for i in range(len(lines)):
        print(lines[i])
        print()
        client = ZenRowsClient("817f0e70aaf5c3c70de65cb9c46f9f830c7c07f8")
        params = {"js_render":"true"}
        url = lines[i].strip()
        print(url)
        time.sleep(10)
        response = client.get(url, params=params)
        # print(response.text)
        bs = BeautifulSoup(response.content, 'lxml')

        # # title of the page
        title = bs.title.text
        print(title)
        time.sleep(10)

        main_text = bs.body.main.text
        main_text = main_text.strip()
        print(main_text)
        time.sleep(10)
        
        
        article_file = open('page_text/'+title+'.txt','w')
        article_file.write(main_text)
        article_file.close()
        time.sleep(10)


# cc.find_all('h1')
# cc.find_all('h2')
# cc.find_all('a')
# cc.find_all('p')

# get all textof the page
# text = cc.get_text()
# text = text.strip()



