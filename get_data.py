import time
import requests
import re
import json

from bs4 import BeautifulSoup

def get_menu_data(soup,data):
    if data=="menu_name":
        res = soup.find("h2").text
        return delete_eng_name(res)
    try:
        items = {"price":0,"energy":1,"protein":4,"fat":5,"carbohydrates":6,"salt":7,"scores":8}
        res = soup.tbody.find_all("tr")[items[data]].td.text
        if items[data]==0 or items[data]==4 or items[data]==5 or items[data]==6 or items[data]==7:
            res = res[:len(res)-1]
        if items[data]==1:
            res = res[:len(res)-4]
        if items[data]==8:
            res = delete_eng_name(res)
            res = re.split("["+chr(65306)+chr(12288)+chr(32)+"]",res)[1::3]
        return res
    except:
        return "-"

def delete_eng_name(menu_name):
    N = len(menu_name)
    n = N
    for i in range(N):
        if ord(menu_name[i])==65288 and 40<=ord(menu_name[i+1])<=122:
            n = i
            break
    return menu_name[:n]

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
    #get menu data
    menus = []
    base = "http://gakushoku.coop"
    D = {}
    for i,menu_link in enumerate(menu_links):
        url = base+menu_link
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        menu_name = get_menu_data(soup,"menu_name")
        price = get_menu_data(soup,"price")
        energy = get_menu_data(soup,"energy")
        protein = get_menu_data(soup,"protein")
        fat = get_menu_data(soup,"fat")
        carbohydrates = get_menu_data(soup,"carbohydrates")
        salt = get_menu_data(soup,"salt")
        scores = get_menu_data(soup,"scores")

        d = {}
        d["menu_name"] = menu_name
        d["price"] = float(price)
        d["energy"] = float(energy)
        d["protein"] = float(protein)
        d["fat"] = float(fat)
        d["carbohydrates"] = float(carbohydrates)
        d["salt"] = float(salt)
        d["red"] = float(scores[0])
        d["green"] = float(scores[1])
        d["yellow"] = float(scores[2])
        print(len(menu_links)-i,d)
        D[i] = d
        time.sleep(2)
    with open("./menus.json","w") as f:
        json.dump(D,f,ensure_ascii=False,indent=4)
if __name__=="__main__":
    main()
"""
参考
https://qiita.com/nbit/items/09b576991794e37d48dc
"""