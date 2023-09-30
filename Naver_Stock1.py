# 품목명과 현재가를 크롤링하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/sise_quant.nhn")
soup = BeautifulSoup(res.text, "html.parser")

for tr in soup.select("table tr"):
    if len(tr.select("td")) > 2:
        number = tr.select("td")[0].text
        item = tr.select("td")[1].text
        price = tr.select("td")[2].text
        
        print(number, item, price)