# 데이터 타입

v_str1 = 'niceman' # 문자형
v_bool = True # 부울 
v_str2 = 'goodboy'
v_float = 10.3 # 실수
v_int = 7 # 정수
v_dict = {
    'name' : 'Kim',
    'age' : 25
} 
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {7,8,9}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_list))
print(type(v_dict))
print(type(v_int))
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5 # 0.5
f4 = 10. # 10.0
# + 더하기, - 빼기, * 곱하기, / 나누기, // 나누기(몫), % 나누기(나머지), ** 지수(제곱)


print(i1*i2)
print(big_int1*big_int2)
print(f1**f2)
print(f3 + i2) # 결과값 실수 = 자동 캐스팅 (형변환)

result = f3 + i2
print(result, type(result))

a= 5.
b =4

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수) 

print(int(result2))

print(float(result2))
print(complex(3))
print(int(True)) # 1로 형변환 
print(int(False))
print(int('3')) # 문자 -> 숫자 형변환 
print(complex(False))
print(3%2)

y = 100
y+= 100 # = y=y+100

print(y)

# 수치 연산 함수
# https://docs.python.org/3/1/library/math.html 

print(abs(-7)) # 절대값
n, m =divmod(100, 8) # 몫, 나머지
print(n,m) 

import math

print(math.ceil(5.1)) # 5.1 보다 크면서 가장 작은 정수
print(math.floor(3.4576)) # 3.4576 보다 작으면서 가장 큰 정수



