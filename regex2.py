# 정상적인 이메일만 추출하는 코드 작성

import re

email = """jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr"""

for email in re.finditer("[a-zA-Z]*\@[a-zA-Z]*\.[a-zA-Z]*\.?[a-zA-Z]*", email):
    print(email.group())

