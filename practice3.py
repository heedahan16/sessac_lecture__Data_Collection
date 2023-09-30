# HTML 문서 내에 모든 A 태그에 링크된 페이지에 있는 내용을 읽어 출력하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/01")
soup = BeautifulSoup(res.text, "html.parser")

# find 사용
for a in soup.find_all("a"):
    res = requests.get("https://crawlingstudy-dd3c9.web.app/01/" + a["href"])
    soup = BeautifulSoup(res.text, "html.parser")

    print(soup.find("p").text.replace("\n", "").strip())


# select 사용
for a in soup.select("a"):
    res = requests.get("https://crawlingstudy-dd3c9.web.app/01/" + a["href"])
    soup = BeautifulSoup(res.text, "html.parser")

    print(soup.select_one("p").text.replace("\n", "").strip())