# 1. 결측치 처리(age - 평균값, Cabin - N, Embarked - N 적용)하고, 2. 성별(Sex) 생존자 합을 구하고, 3. 클래스(Pclass)별 생존자 합을 구하고, 4. 나이(Age)를 활용하여 유아, 10대, 20대, 30대, 40대, 50대, 60대, 노인의 생존자 합을 구하는 코드 작성

import pandas as pd

# 결측치 처리(age - 평균값, Cabin - N, Embarked - N 적용) 코드 작성
print("step1")

titanic = pd.read_csv("titanic_train.csv")

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
titanic["Cabin"] = titanic["Cabin"].fillna("N")
titanic["Embarked"] = titanic["Embarked"].fillna("N")

print(titanic)
print()

# 성별(Sex) 생존자 합 구하는 코드 작성
print("step2")

print(titanic.groupby(titanic["Sex"]).sum()["Survived"])
print()

# 클래스(Pclass)별 생존자 합 구하는 코드 작성
print("step3")

print(titanic.groupby(titanic["Pclass"]).sum()["Survived"])
print()

# 나이(Age)를 활용하여 유아, 10대, 20대, 30대, 40대, 50대, 60대, 노인의 생존자 합을 구하는 코드 작성
print("step4")

def Age_range(n):
    if n < 10:
        return "유아"
    elif (n > 10) and (n < 20):
        return "10대"
    elif (n > 20) and (n < 30):
        return "20대"
    elif (n > 30) and (n < 40):
        return "30대"
    elif (n > 40) and (n < 50):
        return "40대"
    elif (n > 50) and (n < 60):
        return "50대"
    elif (n > 60) and (n < 70):
        return "60대"
    else:
        return "노인"
    
titanic["Age_range"] = titanic["Age"].apply(Age_range)
print(titanic.groupby(titanic["Age_range"]).sum()["Survived"])
