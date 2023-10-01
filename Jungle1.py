# 디자인정글 메인페이지 데이터 크롤링(제목, 카테고리)하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.jungle.co.kr/")
soup = BeautifulSoup(res.text, "html.parser")

urls = []
for li in soup.select("ul.thumb_list li"):
    if li.select_one("a.thumb_title"):
        urls.append("https://www.jungle.co.kr" + li.select_one("a.thumb_title")["href"])

for url in urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    print(url)

    for div in soup.select("div.container"):

        if div.select_one("h1") != None:
            title = div.select_one("h1").text
        elif div.select_one("h5") != None:
            title = div.select_one("h5").text
        else:
            print("다른 타입 발견: ", url)

    for div in soup.select("div.linemap_area"):
        category = div.text.split("\n")[2]

    print(title)
    print(category)
    print()
    
