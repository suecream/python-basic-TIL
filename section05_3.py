# 1
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for a in q1:
    if a == "가을":
        print(q1[a])
        break
    else:
        continue
# 2 
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "메론"}
for a, b in q2.items():
    if b == "사과":
        print('사과 포함')
        break
else:
    print('사과 없음')
# 3 
score = 90
if score > 80:
    print('A학점')
elif score > 60:
    print('B학점')
elif score > 40:
    print('C학점')
elif score > 20:
    print('D학점')
else:
    print("넌 F야")
# 4
a = 12
b = 6
c = 18
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
# 5
num = '1188415'
if num[0] == '1' or num[0] == '3':
    print('남성입니다.')
elif num[0] == '2' or num[0] == '4':
    print('여성입니다.')
else:
    print('주민번호 뒷자리를 다시 입력해주세요.')

# 6
q3 = ["갑", "을", "병", "정"]
for s in q3:
    if s != "정":
        print(s)
    else:
        continue

q7 = [x for x in q3 if x != '정']
print(q7)
# 7
for s in range(1,101):
    if int(s) % 2 == 1:
        print(s,end=' ')
    else:
        continue 

q8 = [x for x in range(1,101) if x % 2 !=0]
print(q8)
print('\n')
# 8
q4 = ["nice", "study", "python", "anaconda", "!"]
for s in q4:
    if int(len(s)) >= 5:
        print(s)
    else:
        continue
# 9
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for s in q5:
    if s.isupper():
        continue
    else:
        print(s,end=' ')
print('\n')
# 10
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for s in q6:
    if s.isupper():
        print(s.lower())
    else:
        print(s.upper())


# 리스트 컴프리헨션 (파이썬의 특성)
numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

numbers2 = [x for x in range(1,101)]
print(numbers2)
