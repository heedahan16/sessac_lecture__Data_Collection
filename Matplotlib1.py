# 판다스에서 했던 결과를 가지고 1. 나이대별 타이타닉 생존자, 2. 성별 타이타닉 생존자 바그래프를 그리는 코드 작성

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 깨짐 에러 해결
mpl.rcParams["font.family"] = "Malgun Gothic"
mpl.rcParams["axes.unicode_minus"] = False

# 나이대별 타이타닉 생존자 바그래프를 그리는 코드 작성

titanic = pd.read_csv("titanic_train.csv")
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

def Age_range(n):
    if n < 10:
        return "유아"
    elif n > 10 and n < 20:
        return "10대"
    elif n > 20 and n < 30:
        return "20대"
    elif n > 30 and n < 40:
        return "30대"
    elif n > 40 and n < 50:
        return "40대"
    elif n > 50 and n < 60:
        return "50대"
    elif n > 60 and n < 70:
        return "60대"
    else:
        return "노인"
    
titanic["Age_range"] = titanic["Age"].apply(Age_range)
age_survived = titanic.groupby(titanic["Age_range"]).sum()["Survived"]
age_survived = age_survived.reindex(['유아', '10대', '20대', '30대', '40대', '50대', '60대', '노인'])

age_bar = plt.bar(age_survived.index, age_survived.values, color = "g")
plt.title("나이대별 타이타닉 생존자")
plt.xlabel("나이")
plt.ylabel("생존자")
plt.show()

# 성별 타이타닉 생존자 바그래프를 그리는 코드 작성
sex_survived = titanic.groupby(titanic["Sex"]).sum()["Survived"]

sex_bar = plt.bar(sex_survived.index, sex_survived.values, color = "g")
plt.title("성별 타이타닉 생존자")
plt.xlabel("성별")
plt.ylabel("생존자")
plt.show()