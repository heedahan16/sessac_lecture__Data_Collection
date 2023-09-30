# 아래 URL의 뉴시스 매체의 어제 일자 모든 기사를 아래와 같이 제목과 본문을 분류하여 크롤링하는 코드 작성

import requests
from bs4 import BeautifulSoup
import re

h = {
    "Cookie":"JSESSIONID=EF09BF1FEBF8E2D45F83138C89C8A5E1; NNB=EBHCWBDFIDSGI; isShownNewLnb=Y; nx_ssl=2"
    , "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
res = requests.get("https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=003", headers=h)
soup = BeautifulSoup(res.text, "html.parser")

oid = "003"
date = "20230930"

url = f"https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid={oid}&date={date}"
res = requests.get(url, headers=h)
soup = BeautifulSoup(res.text, "html.parser")

links = []
for li in soup.select("ul li"):
    if li.select_one("a") != None:
        if li.select_one("a")["class"] == ['nclicks(cnt_flashart)']:
            links.append(li.select_one("a")["href"])

for link in links:
    res = requests.get(link, headers=h)
    soup = BeautifulSoup(res.text, "html.parser")

    if soup.select_one("h2#title_area") != None:
        title = soup.select_one("h2#title_area").text
        for data in re.finditer("\=.*", str(re.sub("\<br\/\>|\<span.*\>.*|\<strong.*\>.*\<\/strong\>|[0-9]{4}\.[0-9]{2}\.[0-9]{2}\.|[a-zA-Z]*\@[a-zA-Z]*\.com|공감언론.*|.*\<\/em\>|\<[^\>]*\>", "",str(soup.select_one("div#newsct_article article"))))):
            content = data.group().split(" = ")[-1]
    else:
        title = soup.select_one("h4.title").text  
        content = re.sub("\<br\/\>|\<span.*\>.*\<\/span\>|\<strong.*\>.*\<\/strong\>|\<p.*\>.*\<\/p.*\>|\<[^\>]*\>.*", "", str(soup.select_one("div#newsEndContents"))).replace("\n", "").strip() 

    print(title)
    print()
    print(content)
    print()
    print()
