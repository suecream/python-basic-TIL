# section08_1
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용 1 (클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("\nex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)


# 사용 2 (클래스 권장x)
from pkg.fibonacci import * # 파일내 모든 모듈 불러오기 (리소스 존나 먹음)

# 사용 3 (클래스 권장o)
from pkg.fibonacci import Fibonacci as fb

fb.fib(600)

print("ex3 : ", fb.fib2(700))
print("ex3 : ", fb().title)


# 사용 4 (함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))
print("ex4 : ", c.div(10, 100))

# 사용 5 (함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

# 사용 6
import pkg.prints as p

p.prt1()
p.prt2()

import builtins # 빌트인 패키지 
print(dir(builtins))
















