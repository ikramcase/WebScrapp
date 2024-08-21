# pip install zenrows
from zenrows import ZenRowsClient
from lxml import html
from bs4 import BeautifulSoup
import time


failed_file = open('failed_urls02.txt','w')

with open("valid_proxies.txt", "r") as j:
    proxies = j.read().split("\n")

counter =0
# web_url = "https://www.cnesst.gouv.qc.ca/en"
with open('failed_urls.txt') as f:
    lines = f.readlines()
    # print(lines)
    for i in range(len(lines)):
        print(lines[i])
        print()
        try:
            client = ZenRowsClient("57b2207183912c3f4b36480b3a25764b8c656171")
            params = {"js_render":"true"}
            url = lines[i].strip()
            print(url)
            time.sleep(10)
            print("PROXY :: ", proxies[counter])
            response = client.get(url, params=params)
            # print(response.text)
            bs = BeautifulSoup(response.content, 'lxml')

            # # title of the page
            title = bs.title.text
            print(title)
            time.sleep(10)

            main_text = bs.body.main.text
            main_text = main_text.strip()
            # print(main_text)
            time.sleep(10)
            article_file = open('page_text/'+title+'.txt','w')
            article_file.write(main_text)
            article_file.close()
            time.sleep(10)
        except:
            print("failed retrying next")
            failed_file.write(url+'\n')

        finally:
            counter = counter+1
            
failed_file.close()

# cc.find_all('h1')
# cc.find_all('h2')
# cc.find_all('a')
# cc.find_all('p')

# get all textof the page
# text = cc.get_text()
# text = text.strip()



