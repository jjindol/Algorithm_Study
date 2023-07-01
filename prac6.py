'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper()) # 대문자로 바꿔줌
print(msg) # 원본은 그대로
print(msg.lower()) # 소문자로 바꿔줌

tmp=msg.upper()
print(tmp)
print(tmp.find(" "))
print(tmp.count("T"))

print("------------------")

print(msg[:2]) # 인덱스 번호 2번 전까지의 문자 추출
print(msg[3:7]) # 3번 인덱스부터 6번 인덱스까지
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=" ")
print()

for x in msg:
    print(x, end=" ")
print()

for x in msg:
    if x.isupper(): # 대문자만 출력 
        print(x, end=" ")
print()

for x in msg:
    if x.islower(): # 소문자만 출력
        print(x, end=" ")
print()

tmp="AZaz"
for x in tmp:
    print(ord(x), end=" ") # 문자열에 하나씩 접근
print()

tmp = 66
print(chr(tmp))





















