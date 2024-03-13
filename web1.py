#web1.py

#윀크롤링을 위한 선안
from bs4 import BeautifulSoup

#페이지 로딩
page = open("test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
#문서의 <p> 전체 검색
# print(soup.find_all("p"))
#문서의 <a> 전체 검색
# print(soup.find_all("a"))
# print(soup.find("p"))
#조건이 있는 경우 : <p class = 'outer-text'>컨텐츠</p>
# print(soup.find_all("p", class_="outer-text"))
#attrs 를 사용
# print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그의 내무 문자열만 가져오기 : .text 속성
# for tag in soup.find_all("p"):
#     title = tag.text.strip() #strip() : 공백문자 삭제
#     title = title.replace("\n","")
#     print(title)

#<p id = 'first'>
print(soup.find(id="first"))

#id 와 class : # = id, . = class

#구조를 이용 : > 는 테그의 관계 표시 ==> 부모 > 자식


#