
import requests
from bs4 import BeautifulSoup

URL = 'https://www.binance.com/de/fee/trading'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='rc-table-container')
print(results.prettify())
