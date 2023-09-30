# 사이트 내에 인기 검색 종목과 주요 해외 지수를 각각 크롤링하여 종목명과 상한, 하한 여부를 아래와 같이 리스트로 정리하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/03")
soup = BeautifulSoup(res.text, "html.parser")

popular = []
for li in soup.select("ul#popularItemList li"):

    item = li.select_one("a").text

    direction = li.select_one("img")["alt"]
    if direction == "상승":
        direction = "상한"
    elif direction == "하락":
        direction = "하한"
    
    popular.append([item, direction])

major = []
for li in soup.select("ul.lst_major li"):
    item = li.select_one("a").text

    direction = li.select_one("img")["alt"]
    if direction == "하락":
        direction = "하한"

    major.append([item, direction])


print(popular)
print()
print(major)
