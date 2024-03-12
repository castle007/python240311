#w전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #언어가 모호함 ==> 사용자의 명시성 필요
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
