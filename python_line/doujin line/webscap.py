import requests
from bs4 import BeautifulSoup
import random

list_name = []
list_links = []

web_res = requests.get('https://hentaithai.com/')
soup = BeautifulSoup(web_res.text,"html.parser")

tag_name = soup.find_all("h3",{"class":"font_name"})
for get_name in tag_name :
    get_name = str(get_name).split('<h3 class="font_name">')[1]
    get_name = str(get_name).split('</h3>')[0]
    if((get_name == "รวมโดจินภาพสีล้วน") or (get_name == "เรื่องที่คนชอบอ่านมากที่สุด") or (get_name == "ไม่รู้จะอ่านเรื่องไหนดี สุ่มเลยละกัน")) : continue
    else : list_name.append(get_name)

tag_links = soup.find_all("a",{"class":"col-6 col-sm-4 col-md-3 col-lg-2"})
for links in tag_links :
    if 'href' in links.attrs:
        get_links = (str("https"+links.attrs['href']+"\n"))
        list_links.append(get_links)

list_links.pop(12)
all_mess = []

for ran in range(1, 6):
    x = random.randint(1, len(list_name) - 1)
    all_mess.append(f'{list_name[x]}    {list_links[x]}')
    print(list_name[x])
    print(list_links[x])


