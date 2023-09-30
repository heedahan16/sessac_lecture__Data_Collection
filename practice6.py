# 사이트 내에 인기 검색 종목과 주요 해외 지수를 각각 상한가인 종목만 크롤링하여 종목명과 주가 지수를 아래와 같이 리스트로 정리하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/03")
soup = BeautifulSoup(res.text, "html.parser")

popular = []
for li in soup.select("ul.lst_pop li"):
    item = li.select_one("a").text
    price = li.select_one("span").text

    direction = li.select_one("img")["alt"]
    if direction == "상승":
        direction = "상한"
    if direction == "상한":
        popular.append([item, price])

major = []
for li in soup.select("ul.lst_major li"):
    item = li.select_one("a").text
    price = li.select_one("span").text

    direction = li.select_one("img")["alt"]
    if direction == "상한":
        major.append([item, price])
    
print(popular)
print()
print(major)
        
