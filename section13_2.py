# section13_2

import random
import time
# 사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime

# DB 생성 & Auto Commit
# 본인 DB 경로
conn = sqlite3.connect('C:/pybasic/resource/records.db', isolation_level=None)
# Cursor 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")


words = []

n = 1
cor_cnt = 0

with open("./resource/word.txt",'r') as f:
    for c in f:
        words.append(c.strip())

# print(words) 

input("Ready? Press Enter Key!")

start = time.time()


while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)

    x = input()

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        # 정답소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 기록 DB 삽입

cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",(cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


print("게임시간 : ",et,"초","정답 갯수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass



























