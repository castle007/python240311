#DemoStr.py

#print(dir(str))

strA = "python is very powerful"
strB = "파이선은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.upper())
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))
print("-".join(lst))

#정규 표현식
import re


result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())
#주석처리
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())
result = re.search("\d{4}", "올해는 2024년")
print(result.group())
result = re.search("\d{5}", "우편번호는 51204년")
print(result.group())
