#web2.py

#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup
#시간함수
import time
#날짜
from datetime import datetime

import os

def crawl_and_save():
    url = "https://www.daangn.com/fleamarket/"
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")
    
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    filename = f"dangun_{current_time}.txt"
    
    with open(filename, "wt", encoding="utf-8") as f:
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            addrElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.replace("\n","").strip()
            price = priceElem.text.replace("\n","").strip()
            addr = addrElem.text.replace("\n","").strip()
            print(f"{title} / {price} / {addr}")
            f.write(f"{title} / {price} / {addr}\n")
    
    return filename

# 1분마다 실행
while True:
    new_file = crawl_and_save()
    time.sleep(60)
    
    # 이전 파일이 존재하는지 확인
    if 'prev_file' in locals():
        # 이전 파일이 존재하는 경우 비교
        if os.path.exists(prev_file):
            # 파일 비교
            with open(prev_file, 'rt', encoding='utf-8') as f1, open(new_file, 'rt', encoding='utf-8') as f2:
                if f1.read() != f2.read():
                    print("\n내용 변경 발생\n")
                    # 변경된 경우 이전 파일 삭제
                    os.remove(prev_file)
                else:
                    # 변경되지 않은 경우 이전 파일 삭제
                    print("\n변경 내용 없음\n")
                    os.remove(new_file)
        else:
            print("이전 파일이 존재하지 않습니다.")
    
    # 현재 파일을 이전 파일로 설정
    prev_file = new_file


# <div class="card-desc">
#       <h2 class="card-title">양말 화정동983-1.오전 10시. 한시간만판매함</h2>
#       <div class="card-price ">
#         10,000원
#       </div>
#       <div class="card-region-name">
#         경기도 고양시 덕양구 성사1동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 55
#           </span>
#         ∙
#         <span>
#             채팅 85
#           </span>
#       </div>
#     </div>
