import time
import requests

from bs4 import BeautifulSoup

def get_menu_data(soup,data):
    if data=="menu name":
        return soup.find("h2").text
    try:
        items = {"price":0,"energy":1,"protein":4,"fat":5,"carbohydrates":6,"salt":7,"scores":8}
        return soup.tbody.find_all("tr")[items[data]].td.text
    except:
        return "-"
def main():
    target_url = "http://gakushoku.coop/list_search.php"
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text, "lxml")
    #get menu links
    menu_links = []
    for a in soup.find_all("a"):
        menu_link = a.get("href")
        if menu_link and "detail" in menu_link and menu_link not in menu_links:
            menu_links.append(menu_link)
    print(len(menu_links))
    #get menu data
    menus = []
    base = "http://gakushoku.coop"
    for i,menu_link in enumerate(menu_links[:10]):
        url = base+menu_link
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        menu_name = get_menu_data(soup,"menu name")
        price = get_menu_data(soup,"price")
        print(menu_name,price)
        time.sleep(1)
if __name__=="__main__":
    main()
"""
参考
https://qiita.com/nbit/items/09b576991794e37d48dc
"""