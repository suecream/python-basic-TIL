# section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# ex1
f = open('./resource/review.txt', 'r')
content = f.read() 
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close() # 이후에 또 사용 시 다시 open 해야함
print('-------------------------------')
print('-------------------------------')

# ex2
with open('./resource/review.txt', 'r') as f: #close 생략 가능
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c)) # with 하위로 인덴트 해야함

print('-------------------------------')
print('-------------------------------')

# ex3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # 양쪽 공백 함수 메소드

print('-------------------------------')
print('-------------------------------')

# ex4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content) # 다 읽고 커서가 마지막에 가있음, 내용 없음.

print('-------------------------------')
print('-------------------------------')

# ex5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line: # line 이 NULL 일때 까지 읽음 한줄 한줄
        print(line, end=" #")
        line  = f.readline()

print('-------------------------------')
print('-------------------------------') 

# ex6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=" $$ ")

print('-------------------------------')
print('-------------------------------') 
print()
# ex7 
score = []
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : {:6.3}".format(sum(score)/len(score)))

# 파일 쓰기

# ex1
with open('./resource/text1.txt','w') as f:
    f.write("niceman!\n")

# ex2
with open('./resource/text1.txt','w') as f:
    f.write("goodman!\n")

# ex3
from random import randint

with open('./resource/text2.txt','w') as f:
    for cnt in range(6): # 0~5
        f.write(str(randint(1, 50)))
        f.write('\n')

# ex4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list=['kim\n','park\n','cho\n']
    f.writelines(list)

# ex5
with open('./resource/text4.txt','w') as f:
    print('test contest1!', file=f)
    print('test contest1!', file=f) 
    # 결과를 콘솔이 아닌 파일로 씀.






















