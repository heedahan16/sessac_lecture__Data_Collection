# 더 보기 눌러서 나오는 추가데이터도 모두 크롤링(제목, 카테고리)하는 코드 작성

import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://www.jungle.co.kr/")

magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

page = 0

while True:

    print("page: ", page)

    url = f"https://www.jungle.co.kr/recent.json?magazineOffset={magazineOffset}&contestOffset={contestOffset}&exhibitOffset={exhibitOffset}&galleryOffset={galleryOffset}"
    res = requests.get(url)
    data = json.loads(res.text)

    magazineOffset = data["magazineOffset"]
    contestOffset = data["contestOffset"]
    exhibitOffset = data["exhibitOffset"]
    galleryOffset = data["galleryOffset"]

    for datum in data["moreList"]:
        title = datum["title"]
        category = datum["targetCode"]

        print(title)
        print(category)
        print()

    page += 1