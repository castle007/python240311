#DemoForm2.py
#DemoForm2.ui(화면저장) + DemoForm2.py(로직저장)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup
#시간함수
import time
#날짜
from datetime import datetime


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
    f.close()
    return filename

#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#폼 클래스 정의 = QMainWindow
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
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
        f.close()
        self.label.setText("당근마켓 크롤링")        
    def secondClick(self):
        crawl_and_save()
        self.label.setText("두번째 버튼 클릭~~")    
    def thirdClick(self):
        crawl_and_save()
        self.label.setText("세번째 버튼 클릭!~~")        

#직접 모듈 실행 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()



