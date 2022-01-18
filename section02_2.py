# section02_2
# 파이썬 기초코딩 
# 몸풀기 코딩실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('my name is Goodboy!')

# 변수선언
myname = 'badboy'

# 조건문
if myname == "Goodboy":
    print('ok') # indent (들여쓰기)

# 반복문

for i in range(1,10):
    for j in range(1,10):
        print('%d*%d = '% (i,j), i*j)

# 변수선언

이름 = '좋은사람'
print(이름)

# 함수선언

def 인사():
    print('안녕하세요 반갑습니다.')

인사()

def greeting():
    print('hello')

greeting()

# 클래스 
class Cookie:
    pass

# 객체생성
cookie = Cookie()

print(id(Cookie))
print(dir(cookie))
print(cookie.__class__)