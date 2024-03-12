#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#저식 클래스
class Student(Person):
    #재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기(재정의)    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, 학과:{2}, 학번: {3})".format(self.name, self.phoneNumber, self.subject, self.studentID))



p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "240312")
print(p.__dict__)
print(s.__dict__)
p.printInfo()
s.printInfo()


