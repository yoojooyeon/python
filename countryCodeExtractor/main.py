import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:")
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')

countries = []

for row in soup.findAll('table')[0].tbody.findAll('tr'):
  first_col = row.findAll('td')[0].text
  third_col = row.findAll('td')[2].text
  if third_col != "":
    country = {
      'first_col': first_col.capitalize(),
      'third_col': third_col
    }
    countries.append(country)
 

def number_taker():
  output = input("#: ")
  
  try:
    output = int(output)
    if output > len(countries):
      print("Choose a number from the list.")
      number_taker()
    else:
      country = countries[output]
      print(f"You chose {country['first_col']}")
      print(f"The currency code is {country['third_col']}")
      return
  except:
    print("That wasn't a number.")
    number_taker()


for idx, key in enumerate(countries):
  print(f"#{idx} {key['first_col']}")
   

number_taker()
