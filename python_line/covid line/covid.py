import requests

url_get = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
covid = url_get.json()[0]

new_case = covid["new_case_excludeabroad"]
total_case = covid["total_case_excludeabroad"]
total_recovered = covid["total_recovered"]
case_new_diff = covid["case_new_diff"]

i = total_case
print('{:,}'.format(i))