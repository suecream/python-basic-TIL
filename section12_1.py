#section12_1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now) # 현재 시간


nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print("nowDatetime : ",nowDatetime)


# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite.sqlite_version : ', sqlite3.sqlite_version)

# DB생성 & Auto Commit (Rollback)
conn = sqlite3.connect('C:/pybasic/resource/database.db', isolation_level = None)

# Cursor
c = conn.cursor()
print('Cursor Type : ',type(c))


# 테이블 생성 (Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
username text, email text, phone text, website text, regdate text)")

# 데이터 삽입

# c.execute("INSERT INTO users VALUES(1, 'kim', 'superlove133@gmail.com', \
# '010-5749-9926', 'kim.com', ?)", (nowDatetime,))

# c.execute("INSERT INTO users(id, username, email, phone, website, regdate)\
# VALUES(?,?,?,?,?,?)", (2, 'park', 'khj990213@naver.com','031-397-9926',\
# 'park.com',nowDatetime))

# Many 삽입(튜플, 리스트)
userlist = (
    (3, 'lee', 'lee@naver.com', '010-1234-2353','lee.com',nowDatetime),
    (4, 'cho','cho@naver.com','010-2134-2664','cho.com',nowDatetime),
    (5, 'yoon', 'yoon@google.com', '010-6623-4121','google.com', nowDatetime),
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate)\
# VALUES(?,?,?,?,?,?)", userlist)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")

# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)
# 지우고 지운값을 반환


# COMMIT : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit()

# Rollback
# conn.rollback()

# 접속 해제
conn.close()









