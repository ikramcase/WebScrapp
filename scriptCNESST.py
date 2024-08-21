# pip install zenrows
from zenrows import ZenRowsClient
from lxml import html

client = ZenRowsClient("745dc5dcb71e78da952053e1746b71e0e7c2c39b")
website_url = "https://www.cnesst.gouv.qc.ca/en"
params = {"js_render":"true"}

response = client.get(website_url, params=params)

# print(response.text)
webpage = html.fromstring(response.content)

href_list = webpage.xpath('//a/@href')

# print(*href_list, sep='\n')

# open a text file for URLs
url_file = open('url_data.txt','w')

print('++++++===FROM HERE==++++++')
for i in range(len(href_list)):
    url = href_list[i]
    if url.startswith('/en'):
        # print(url)
        web_url = "https://www.cnesst.gouv.qc.ca"+url
        print(web_url)
        url_file.write(web_url)
        response = client.get(web_url, params=params)
        webpage = html.fromstring(response.content)
        href_list_new = webpage.xpath('//a/@href')
        # print(href_list_new, sep='\n')
        for i in range(len(href_list_new)):
            url = href_list_new[i]
            if url.startswith('/en'):
                # print(url)
                web_url = "https://www.cnesst.gouv.qc.ca"+url
                print(web_url)
                url_file.write(web_url+'\n')
url_file.close()

# for unique urls, use the following command
# cat url_data.txt | sort | uniq > output.txt
