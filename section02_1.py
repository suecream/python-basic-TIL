#section02_1
#파이썬 기초코딩
#print 구문의 이해

#기본출력
print('Hello Python!')
print("hello python")
print("""heLLo Python""")
print('''hellO PYthon''')


print()

#separator 옵션 사용
print('T','E','S','T', sep='')
print('2021','04','30', sep='-')
print('superlove133','google.com', sep='@')

#end 옵션 사용
print('welcome To', end='')
print(' the black parade', end='')
print(' piano notes')
#end 사용 X => 줄바꿈
print('test')

#format 사용 (맵핑개념)
print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('you','me'))
print('{a} are {b}'.format(a='you', b ='me'))

print("%s's favorite number is %d" % ('hojun', 7))  # %s :문자, %d : 정수, %f : 실수 

print("test1: %5d, price: %4.2f" % (1233, 1143.12345123)) # 자릿수 지정
print('test1: {0: 5d}, price: {1: 4.2f}'.format(12314, 123123.21312))
print('test1: {a: 5d}, price: {b: 4.2f}'.format(a=12341,b=1231214.2123))

print("'you'")
print('\'you\'')
print('"you"')
print('''"you"\n\n''')
print("\t\ttest")