# kr_daily.csv 파일을 읽어 1. 확진자, 2. 사망자 그래프 두 개를 한 화면에 그리는 코드 작성

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.family"] = "Malgun Gothic"
mpl.rcParams["axes.unicode_minus"] = False

covid = pd.read_csv("kr_daily.csv")

# 확진자 그래프 
covid["date"] = pd.to_datetime(covid["date"].astype("str"))
plt.subplot(121)
plt.plot(covid["date"][-15:].values, covid["confirmed"][-15:].values, color="r", linestyle = "dashed")
list_date = []
for i in covid["date"][-15:]:
    list_date.append(str(i).split(" ")[0])

plt.title("확진자")
plt.xticks(list_date, rotation=45)

# 사망자 그래프
plt.subplot(122)
plt.bar(covid["date"][-15:].values, covid["death"][-15:].values, color="r")
plt.title("사망자")
plt.xticks(list_date, rotation=45)
plt.show()