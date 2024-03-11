#Demploop.py

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100, "문자열, 3.14"]
for item in lst:
    print(item, type(item))


device = {"아이폰": 5, "아이패드": 10}
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)    

    

lst = list(range(10))
print(lst)

print("--- 수열함수 ----")
for i in range(10):
    print(i)

print(list(range(1,11)))
print(list(range(2000,2025)))

print("-------리스트 컴프리핸션(임베딩)------")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

print("----- 필터링 ----")
def getBiggerThan20(i):
    return i>20


lst = [10, 25, 35]
itemL = filter(getBiggerThan20, lst)

for i in itemL:
    print(i)

print("----- 람다함수 ----")
lst = [10, 25, 35]
itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print(i)
    
