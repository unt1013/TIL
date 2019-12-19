import requests
import time

from bs4 import BeautifulSoup

url = "https://www.naver.com"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')

data = soup.select("#PM_ID_ct .ah_k")
out = True
index = 0
while(out):
    time.sleep(1)
    print(data[index].text)
    index = index + 1
    break