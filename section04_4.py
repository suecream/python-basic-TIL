# section04_4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> NongoDB
# 선언
a = {'name':'kim', 'phone':'010-7777-7777', 'birth': 990213}
# 값은 중복될 수 있으나 Key는 중복불가
b = {0:'hello python', 1:'hello coding'}
c = {'arr':[1,2,3,4,5]}

print(type(a))

# 출력 (Key 조회)
print(a['name'])
print(a.get('name'))
print(a.get('address')) # 이 방식 추천
print(c['arr'][1:2]) # 슬라이싱 처리 가능

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1,3,4] # 리스트
a['rank2'] = (1,2,3,) # 튜플
print(a)

# keys, values, items(한 쌍)
print(a.keys())
print(list(a.keys())) # 리스트로 형변환 해야함 

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items(),'\n\n\n\n\n\n\n')
print(list(a.items()))
print(1 in b)
print('name2' in a)

# 집합(Sets)(순서x, 중복x)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,6])

print(type(a))
print(c) # 중복 허용x

t = tuple(b)
print(t)
l = list(b)
print(l)

print('\n\n\n\n\n')

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7,8,10,15])

s3.add(18)
s3.add(7)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))


