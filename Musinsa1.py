# 무신사 쇼핑몰의 상의(TOP) 카테고리 첫 페이지의 제품들의 브랜드명, 제품명, 가격을 아래와 같이 크롤링하는 코드 작성

import requests
from bs4 import BeautifulSoup

h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
res = requests.get("https://store.musinsa.com/app/items/lists/001", headers=h)
soup = BeautifulSoup(res.text, "html.parser")

for li in soup.select("ul#searchList li.li_box"):
    brand = li.select_one("p.item_title a").text
    item = li.select_one("p.list_info a").text.replace("\n", "").strip()
    price = li.select_one("p.price").text.split("\n")[-2].strip()

    print("브랜드: ", brand)
    print("제품명: ", item)
    print("가격: ", price)
    print()