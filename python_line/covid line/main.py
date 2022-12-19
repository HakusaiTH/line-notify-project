import requests
import schedule
from datetime import datetime

def job():
    url = 'https://notify-api.line.me/api/notify'
    token = 'Z3nFlOBYdaPDdmLD3FIch5dH35MJywumKXYtjOTLUr5'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {token}'
    }

    url_get = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
    covid = url_get.json()[0]

    new_case = '{:,}'.format(covid["new_case_excludeabroad"])
    total_case = '{:,}'.format(covid["total_case_excludeabroad"])
    total_recovered = '{:,}'.format(covid["total_recovered"])
    case_new_diff = '{:,}'.format(covid["case_new_diff"])
    current_dateTime = str(datetime.now())
    get_time = current_dateTime.split()

    message = 'test line notify'

    message = f"\nจํานวนผู้ป่วย covid-19 ประจำวันที่ {get_time[0]}\n" \
              f"จํานวนผู้ป่วยรายใหม่    {new_case} ราย\n" \
              f"จํานวนผู้ป่วยสะสม   {total_case} ราย\n" \
              f"จํานวนผู้ป่วยรักษาหายสะสม   {total_recovered} ราย\n" \
              f"จํานวนการเพิ่มขึ้น/ลดลง ของผู้ป่วย  {case_new_diff} ราย\n" \

    res = requests.post(url=url, headers=headers, data={'message': message})

schedule.every().day.at('07:40').do(job)
while True:
   schedule.run_pending()
