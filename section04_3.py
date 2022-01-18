# section04_3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서 o, 중복 o, 수정 o, 삭제 o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print('\n\n\n\n\n')

# 리스트 함수
y =[5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7) # 2번 인덱스에 7을 넣겠다.
print(y)
y.remove(2) # 숫자2를 찾아 지움 (del은 2번 인덱스를 지움)
print(y)
y.pop()
print(y)
ex = [88, 77]
y.extend(ex)
# y.append(ex)
print(y) # extend 와 append 의 차이

# 삭제 함수 : del, remove, pop

# 튜플 (순서 o, 중복 o, 수정 x, 삭제 x)
# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a','b','c'))
# del c[2] , 불가능
print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print('\n\n\n\n\n')

# 튜플 함수
z =(5,2,3,1,4)
print(z)
print(3 in z)
print(z.index(3)) # 찾고자 하는 값의 인덱스 번호 출력
print(z.count(1)) # 찾고자 하는 값의 갯수 출력




