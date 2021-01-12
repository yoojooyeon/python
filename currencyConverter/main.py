import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

code_url = "https://www.iban.com/currency-codes"
currency_url = "https://transferwise.com/gb/currency-converter/"

print("Welcome to CurrencyConvert PRO 2000: \n")
result = requests.get(code_url)
soup = BeautifulSoup(result.text, 'html.parser')

countries = []

for row in soup.findAll('table')[0].tbody.findAll('tr'):
  first_col = row.findAll('td')[0].text
  third_col = row.findAll('td')[2].text
  if third_col != "":
    country = {
      'name': first_col.capitalize(),
      'code': third_col
    }
    countries.append(country)
 

def first_taker():
  global first_input
  first_input = input("\nWhere are you from? Choose a country by number.\n\n#: ")
  try: 
    first_input = int(first_input)
    if first_input > len(countries):
      print("Choose a number from the list.")
      first_taker()
    else:
      country = countries[first_input]
      print(f"{country['name']}")
      return
  except:
    print("That wasn't a number.")
    first_taker()


  
def second_taker():
  global second_input 
  second_input = input("\nNow choose another country.\n\n#: ")
  try:
    second_input = int(second_input)
    if second_input > len(countries):
      print("Choose a number from the list.")
      second_taker()
    else:
      country = countries[second_input]
      print(f"{country['name']}")
      return
  except:
    print("That wasn't a number.")
    second_taker()



def third_taker():
  try:
    third = input(f"\nHow many {first_country['code']} do you want to convert to {second_country['code']}?\n")
    third = int(third)
    return third
  except:
    print("That wasn't a number.")
    return third_taker() 

  
  

for idx, key in enumerate(countries):
  print(f"#{idx} {key['name']}")
   
first_taker()
second_taker()

first_country = countries[first_input]
second_country = countries[second_input]
  
amount = third_taker()

r = requests.get(f"{currency_url}{first_country['code']}-to-{second_country['code']}-rate?amount={amount}")
soup = BeautifulSoup(r.text, "html.parser")
rate = soup.find("span", {"class": "text-success"}).text
rate = float(rate)
rated = rate*amount


if rated:
  from_amt = format_currency(amount, first_country['code'], locale="ko_KR")
  to_amt = format_currency(rated, second_country['code'], locale="ko_KR")
  print(f"{from_amt} is {to_amt}")
