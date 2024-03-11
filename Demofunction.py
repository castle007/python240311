#Check git Operation

def SetValue(newValue):
    x = newValue
    print(x)

print(SetValue(5))

def times(a, b):
    return a*b


print(times(3,4))

globals()

#지역변수, 전역변수
x =1
def func(a):
    return a + x

def func2(a):
    x = 5
    return a + x

func(2)
print(func(2))
print(func2(2))

#기본값 세팅
def defaulttimes(a=10, b=20):
    return a*b

print(defaulttimes())
print(defaulttimes(5))
print(defaulttimes(b=6))
print(defaulttimes(5,6))


#튜플리턴
def swap(x, y ):
    return y, x


#호출
print(swap(5,10))



