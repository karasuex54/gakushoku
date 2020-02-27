"""
参考
https://qiita.com/nbit/items/09b576991794e37d48dc
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

url = "http://gakushoku.coop/list_search.php"
soup = BeautifulSoup(urlopen(url),"lxml")

menu_links = []
for a in soup.find_all("a"):
    menu_link = a.get("href")
    if menu_link and ("detail" in menu_link) and (menu_link not in menu_links):
        menu_links.append(menu_link)

time.sleep(1)

base = "http://gakushoku.coop/"
for i,menu_link in enumerate(menu_links):
    url = base+menu_link
    soup = BeautifulSoup(urlopen(url),"lxml")
    print(soup)
    break