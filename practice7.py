# 분양 중인 아파트 정보를 크롤링하여 아래와 같이 딕셔너리 형태로 정리하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/03")
soup = BeautifulSoup(res.text, "html.parser")

detail = []    
for li in soup.select("ul.sale_list._sale_list li.sale_item div.sale_box"):
    item = li.select_one("div.sale_tit a").text    
    price = li.select("dd")[0].text
    type1 = li.select("dd")[1].text.split("|")[0]
    type2 = li.select("dd")[1].text.split("|")[1]
    number = li.select("dd")[2].text.split("|")[0]
    square = li.select("dd")[2].text.split("|")[1]
    detail.append(dict(이름=item, 분양가=price, 유형=type1, 분양유형=type2, 세대수=number, 평형=square))

print(detail)