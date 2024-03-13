# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트오브베스트 주소 
        data = f'https://www.todayhumor.co.kr/board/list.php?kind=total&table=total&page={n}'
        print(data)

        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        #<td class='subject'
        # <a href="/board/view.php?table=lovestory&amp;no=95112&amp;s_no=15474815&amp;kind=total&amp;page=2" target="_top">금수저 흙수저</a>

        for item in list:
                try:
                        #문자열
                        title = item.find("a").text
                        #주소
                        # addr = item.find("a")["href"]
                        # print(title)
                        # print(addr)
                        if (re.search('한국', title)):
                                print(title.strip())

                except:
                        pass
        
