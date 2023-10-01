# 로켓펀치 채용 페이지 총 10페이지 크롤링(회사명, 회사 설명, 채용정보(회사별 여러 개))하는 코드 작성

import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://www.rocketpunch.com/jobs")
soup = BeautifulSoup(res.text, "html.parser")

for page in range(1, 11):

    print("page: ", page)

    res = requests.get(f"https://www.rocketpunch.com/api/jobs/template?page={page}")
    soup = BeautifulSoup(json.loads(res.text)["data"]["template"], "html.parser")

    employments = []

    companies = []
    for content in soup.select("div.content"):
        url = "https://www.rocketpunch.com" + content.select_one("div.company-name a")["href"]
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        name = soup.select_one("div#company-name").text
        description = soup.select_one("h3.description").text.replace("\n", "")

        for company in soup.select("section#company-jobs"):
            companies.append(company)
    
    details = []
    for company in companies:
        for item in company.select("div.ui.segment.items"):
            detail = item.select_one("div.ui.job-title.header").text.replace("\n", "")
            details.append(detail)
        
    employment = {
        "name":name
        , "description":description
        , "detail":details
    }

    employments.append(employment)

    print(employments)
        


