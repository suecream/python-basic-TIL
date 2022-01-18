# section12_2
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/pybasic/resource/database.db')

# Cursor 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치 변경 확인
# 1개로 로우 선택
# print("One -> \n", c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
# print("ALL -> \n", c.fetchall())
# print("ALL -> \n", c.fetchall()) # 커서의 위치가 중요하다

print()

# 순회1
rows = c.fetchall()

print(type(rows))

# for row in rows:
#    print('retrieve1 > ', row)

# 순회2 (더 많이 쓰임)
# for row in c.fetchall():
#     print('retrieve2 > ', row))

# 순회3 (가독성이 좀 떨어짐)
# for row in c.execute('SELECT * FROM users ORDER BY id desc')

print()

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?',param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 데이터 없음

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:Id',{'Id':5}) # 딕셔너리
print('param3', c.fetchone())
print('param3', c.fetchall()) 

# WHERE retrieve4
prarm4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", prarm4) # IN 은 합집합
print('param4', c.fetchall())

# WHERE retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')"% (3,4))
print('param5', c.fetchall())

# WHERE retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1": 2,"id2" : 5})
print('param6', c.fetchall())


# Dump 출력
with conn:
    with open('C:/pybasic/resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump print Complete')
# f.close(), conn.close()













