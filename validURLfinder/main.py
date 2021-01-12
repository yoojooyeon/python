import requests
import os


def close():
    print("Do you want to start over? y/n ")
    ans = str(input()).lower()
    if ans == "y":
      os.system('clear')
      down_finder()
    elif ans == "n":
      print("k. bye!")
      return
    else:
      print("That's not a valid answer")
      close()


def down_finder():
  os.system('clear')
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  
  ans = str(input()).lower().split(",")

  for x in ans:
    x = x.strip()
    com = x.find(".")

    if com == -1:
      print(f"{x} is not a valid url")
    else:
      if "http://" not in x and "https://" not in x:
        x = f"http://{x}"
      try:
        request = requests.get(x)
        if request.status_code == 200:
          print(f"{x} is up!")
        else:
          print(f"{x} is down!")
      except:
        print(f"{x} is down!")
  close()    


down_finder()

