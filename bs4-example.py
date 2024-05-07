import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
request = requests.get(link, headers)
site = BeautifulSoup(request.text, "html.parser")

brl_today_value = site.find("div", class_="AP7Wnd").get_text()

print(brl_today_value)
