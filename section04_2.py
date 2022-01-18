# section04_2
# 문자열, 문자열 연산, 슬라이싱

str1 = "i am boy."
str2 = 'niceman'
str3 = ""
str4 = str('sd')
print(len(str1),len(str2),len(str3),len(str4)) # LENGTH

escape_str1 = 'Do you have a \"big collection\"'
print(escape_str1)

escape_str2 = "tab \tTab\t"
print(escape_str2)

# Raw string
raw_s1 = r'C:\programs\Test\Bin'
print(raw_s1)
raw_s2 = r'\\a\\a'
print(raw_s2)

# 멀티라인
multi = \
""" 
문자열 
멀티라인 
테스트
"""

print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = 'abc'
str_o3 = "def"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 + str_o3)

print('a' in str_o2)
print('f' in str_o2)

# 문자열 형변환
print(str(77))
print(str(10.4)+'asd')

# 문자열 함수

# a = 'Niceman'
# b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice','good'))
# print(list(reversed(b))) ctrl + ? 전체 주석


a = 'Niceman'
b = 'orange' 

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)])
print(a[:])
print(b[0:4])

print(b[0:4:2])
print(b[1:-2])
print(b[::-1])

