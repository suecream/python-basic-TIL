# section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter)
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# ex1
def hello(world):
    print("hello", world)

hello('python!')
hello(123)  # 함수 사용 위치 보다 선언부가 위에 있어야 함


# ex2
def hello_re(world):
    v = "hello" + str(world)
    return v
# 함수 호출부로 결과값을 리턴
str = hello_re("python!!")
print(str)

# ex3 (다중리턴)
def function_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1, y2, y3

a, b, c = function_mul(100)
print(a, b, c)

# ex4(데이터 타입 반환)
def function_mu2(x): # x에 문자열이 들어올 수 없다.
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3] # 리스트로 리턴 받음

lt= function_mu2(100)
print(lt, type(lt))

print('\n\n\n\n')

# ex4
# *args, *kwargs (가변 인자)

def args_func(*args): 
  #  print(args)
   # for t in args:
    #    print(t)
    for i,v in enumerate(args): # 인덱스 생성 함수
        print(i, v)
    

args_func('kim')
args_func('kim','park')
args_func('kim','park','lee')

# kwargs
# *이면 튜플로 받고 **이면 딕셔너리로 받음
def kwargs_func(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)   

kwargs_func(name1='kim', name2='park',name3='lee')

# 전체 혼합
def example_mul(arg1, arg2,*args,**kwargs):
    print(arg1,arg2,args,kwargs)

example_mul(10,20)
example_mul(10,20,'park','kim', age1=24, age2=13)

# ex5
# 중첩 함수(클로저)
# (심화) 데코레이터
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in function')
    func_in_func(num + 10000)

nested_func(10000)
# ex6
# 힌트
def function_mu2(x : int) -> list: # 예외를 발생시키지 않고 코드상 설명
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3]
print(function_mu2(5))

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 너무 람다식만 쓰면 가독성 저하

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num*10

var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

# 람다식 함수 (축약식), 함수를 매개변수로 넘길 때 좋음(리소스 절약)

lambda_mul_10 = lambda num: num*10

print('>>>',lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y *func(10))

func_final(10,10,lambda_mul_10)

print(func_final(10,10, lambda x : x*1000)) # 람다식 즉시 작성