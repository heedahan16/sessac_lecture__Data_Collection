# HTML 문서 내에 TABLE 내에 th와 td에 있는 값들을 크롤링 해 아래와 같은 딕셔너리 형태를 만드는 코드 작성

import requests
from bs4 import BeautifulSoup

res = requests.get("https://crawlingstudy-dd3c9.web.app/01")
soup = BeautifulSoup(res.text, "html.parser")

# find 사용

ths = []
for th in soup.find("table").find_all("th"):
    ths.append(th.text)

result = []
for tr in soup.find("table").find("tbody").find_all("tr"):
    name = tr.find_all("td")[0].text
    age = tr.find_all("td")[1].text
    result.append(dict(zip(ths, [name, age])))

print(result)


# select 사용

ths = []
for th in soup.select("table th"):
    ths.append(th.text)

result = []
for tr in soup.select("table tbody tr"):
    name = tr.select("td")[0].text
    age = tr.select("td")[1].text
    result.append(dict(zip(ths, [name, age])))

print(result)