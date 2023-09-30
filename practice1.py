# HTML 문서 내에 ID가 cook인 태그 내의 내용을 출력하는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/01")
soup = BeautifulSoup(res.text, "html.parser")

# find 사용
print(soup.find(id="cook").text.replace("\n", "").strip())

# select 사용
print(soup.select_one("p#cook").text.replace("\n", "").strip())