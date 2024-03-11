


#형식변환
a = (1,2,3)
b = list(a)
b.append(4)
print(b)

#딕셔너리
fruits = {"apple": "red", "banana" : "yellow"}
print(fruits)
print(fruits["apple"])

#입력
fruits["kiwi"] = "green"

#삭제
del fruits["apple"]
print(fruits)

for item in fruits.items():
    print(item)


