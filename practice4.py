# 사이트 내에 인기검생 종목과 주요 해외 지수를 각각 크롤링하여 종목명과 주가 지수를 아래와 같은 리스트로 정리하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/03")
soup = BeautifulSoup(res.text, "html.parser")

popular = []
for li in soup.select("ul#popularItemList li"):
    item = li.select_one("a").text
    price = li.select_one("span").text
    popular.append([item, price])

major = []
for li in soup.select("ul.lst_major li"):
    item = li.select_one("a").text
    price = li.select_one("span").text
    major.append([item, price])

print(popular)
print()
print(major)