import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open("proxy_list.txt", "r") as f:
    proxyes = f.read().split("\n")
    for p in proxyes:
        q.put(p)


def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http":proxy, 
                                                                 "https:":proxy})
        except:
            continue

        if res.status_code == 200:
            print(proxy)


for _ in range(40):
    threading.Thread(target=check_proxies).start()