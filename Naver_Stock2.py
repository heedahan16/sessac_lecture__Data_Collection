# 전일 대비 상승한 항목만 품목명, 현재가, 전일비를 크롤링하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/sise_quant.nhn")
soup = BeautifulSoup(res.text, "html.parser")

for tr in soup.select("table tr"):
    if len(tr.select("td")) > 2:
        if tr.select("td")[3].select_one("img") != None:
            if "up" in tr.select("td")[3].select_one("img")["src"]:
                number = tr.select("td")[0].text
                item = tr.select("td")[1].text
                price = tr.select("td")[2].text
                previous = tr.select("td")[3].text.replace("\n", "").strip()

                print(number, item, price, previous)