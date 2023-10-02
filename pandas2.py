# 1. 아래와 같은 데이터프레임(점수는 1~100까지 랜덤값)을 만들고 2. 반별 합계와 평균을 추가하고 3. 인덱스 명을 추가하고 학년별 합계를 구하는 코드 작성

import pandas as pd
import numpy as np

print("step1")
df = pd.DataFrame(np.random.randint(1, 100, size=(15, 3)), index=[["1학년", "1학년", "1학년", "1학년", "1학년", "2학년", "2학년", "2학년", "2학년", "2학년", "3학년", "3학년", "3학년", "3학년", "3학년"], ["1반", "2반", "3반", "4반", "5반", "1반", "2반", "3반", "4반", "5반", "1반", "2반", "3반", "4반", "5반"]], columns=["국어", "영어", "과학"])
print(df)
print()

print("step2")
df["총점"] = df["국어"] + df["영어"] + df["과학"] 
df["평균"] = df["총점"] / 3
print(df)
print()

print("step3")
df.index.names=["학년", ""]
print(df.groupby("학년").sum())
