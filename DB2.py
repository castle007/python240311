#DB2.py

import sqlite3

#연결 인스턴스
#con = sqlite3.connect(":memory:")
con = sqlite3.connect(r"c:\work\sample.db")
#커서 인스턴스(실제 구문)
cur = con.cursor()
#테이블 구조생성
cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook (name text, phoneNum text);")

#1건 데이터 입력
cur.execute("INSERT INTO PhoneBook VALUES ('홍길동', '010-2121');")
#입력 파라메터 처리
name = "박문수"
phoneNum = "010-3131"
cur.execute("INSERT INTO PhoneBook VALUES (?,?);", (name, phoneNum))
#여러건 입력
datalist = (("tom","010-4141"),("jhon","010-5151"))
cur.executemany("INSERT INTO PhoneBook VALUES (?,?);",datalist)


#검색
cur.execute("SELECT * FROM PhoneBook;")
# for row in cur:
#     print(row)
print(cur.fetchone())
print(cur.fetchmany(2))

con.commit()