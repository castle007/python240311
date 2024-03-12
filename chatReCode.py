import re

def check_email(email):
    # 이메일 주소 패턴
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # 이메일 주소 검사
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 데이터
emails = [
    "example@example.com",
    "user123@gmail.com",
    "john.doe@company.co.uk",
    "jane_doe123@yahoo.com",
    "invalid.email@",
    "no_at_symbol.com",
    "missing_domain@.com",
    "special!characters@example.com",
    "space in@email.com",
    "이메일@도메인.com"
]

# 각 이메일 주소를 체크하고 결과 출력
for email in emails:
    if check_email(email):
        print(f"{email} : 적합함")
    else:
        print(f"{email} : 부적합")
