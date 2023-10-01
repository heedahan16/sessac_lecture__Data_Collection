# 아래 사이트를 크롤링하여 아래와 같이 각각 글의 id와 title 그리고 글마다 코멘트 내용을 리스트 형식으로 담고 최종 json 파일 형태로 저장하는 코드 작성

import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://crawlingstudy-dd3c9.web.app/05")

res = requests.get("https://jsonplaceholder.typicode.com/photos")

submit = []
for data in json.loads(res.text):
    id = data["id"]
    title = data["title"]
    
    res = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={id}")
    
    result = {
        "id" : id
        , "title" : title
        , "comment" : []
    }

    for comment in json.loads(res.text):
        result["comment"].append(comment["body"].replace("\n", ""))

    submit.append(result)

    print(submit)


with open("practice8.json", "w") as f:
    json.dump(submit, f)

