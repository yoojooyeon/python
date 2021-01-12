import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

r = requests.get(alba_url)
soup = BeautifulSoup(r.text, "html.parser")

companies = []

company = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li")[:-1]

global name
global link

for x in company:
  items = x.find_all("span")
  name = items[1].text
  name = name.replace("/", "_")
  link = x.find("a")["href"]

  if name and link:
    company = {
      'company': name,
      'link': link
    }
    companies.append(company)

  csv_lists = []

  nav_r = requests.get(f"{link}")
  nav_soup = BeautifulSoup(nav_r.text, "html.parser")

  navigate = nav_soup.find("div", {"id": "NormalInfo"}).find("tbody").find_all("tr")[:-1]

  for x in navigate:
    tds = x.find_all("td")
    try:
      place = tds[0].text
      title = tds[1].find("span", {"class":"company"}).text
      times = tds[2].find("span").text

      pay = tds[3].find_all("span")
      pay1 = pay[0].text
      pay2 = pay[1].text
      pays = pay1 + pay2
      dates = tds[4].text
      
      csv_list = {'place': place, 'title':title, 'time': times, 'pay': pays, 'date': dates}
      csv_lists.append(csv_list)
      
      files = open(f"{name}.csv", mode="w")
      writers = csv.writer(files)
      writers.writerow(["place", "title", "time", "pay", "date"])

      for x in csv_lists:
        writers.writerow(list(x.values()))

    except IndexError:
      continue
    
