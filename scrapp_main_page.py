from zenrows import ZenRowsClient
from bs4 import BeautifulSoup


client = ZenRowsClient("817f0e70aaf5c3c70de65cb9c46f9f830c7c07f8")
url = "https://www.cnesst.gouv.qc.ca/en/prevention-and-safety/organizing-prevention"
params = {"js_render":"true","antibot":"true"}

response = client.get(url, params=params)

print(response.text)
cc = BeautifulSoup(response.content)

# title of the page
title = cc.title.text
print(title)

