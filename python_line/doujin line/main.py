import requests
import schedule
from bs4 import BeautifulSoup
import time
import random

def job():
    url = 'https://notify-api.line.me/api/notify'
    token = 'Z3nFlOBYdaPDdmLD3FIch5dH35MJywumKXYtjOTLUr5'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {token}'
    }

    list_name = []
    list_links = []

    web_res = requests.get('https://hentaithai.com/')
    soup = BeautifulSoup(web_res.text, "html.parser")

    tag_name = soup.find_all("h3", {"class": "font_name"})
    for get_name in tag_name:
        get_name = str(get_name).split('<h3 class="font_name">')[1]
        get_name = str(get_name).split('</h3>')[0]
        if ((get_name == "รวมโดจินภาพสีล้วน") or (get_name == "เรื่องที่คนชอบอ่านมากที่สุด") or (
                get_name == "ไม่รู้จะอ่านเรื่องไหนดี สุ่มเลยละกัน")):
            continue
        else:
            list_name.append(get_name)

    tag_links = soup.find_all("a", {"class": "col-6 col-sm-4 col-md-3 col-lg-2"})
    for links in tag_links:
        if 'href' in links.attrs:
            get_links = (str(links.attrs['href'] + "\n"))
            list_links.append(get_links)

    list_links.pop(12)
    all_mess = []
    for ran in range(1, 6):
        x = random.randint(1, len(list_name) - 1)
        all_mess.append(f'{list_name[x]}    https:{list_links[x]}')

    message = f"เรื่องที่ 1 : {all_mess[0]} \n" \
              f"เรื่องที่ 2 : {all_mess[1]} \n" \
              f"เรื่องที่ 3 : {all_mess[2]} \n" \
              f"เรื่องที่ 4 : {all_mess[3]} \n" \
              f"เรื่องที่ 5 : {all_mess[4]} \n" \

    res = requests.post(url=url, headers=headers, data={'message': message})

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)