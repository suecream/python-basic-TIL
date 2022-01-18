# section07_1
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수
#     함수
#     함수


# ex1
class UserInfo: # 대문자 시작을 원칙으로 함(단어간 연결시에도)
    # 속성, 메소드   
    def __init__(self, name): # init 메소드
        self.name = name
    def user_info_p(self):
        print("name : ", self.name)

# 네임스페이스
user1 = UserInfo('kim') # 인스턴스 생성
print(user1.name) 
user1.user_info_p() # 인스턴스 메소드
user2 = UserInfo('park')
print(user2.name)
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# ex2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
# self_test.function1()
SelfTest.function1() # 클래스에서 호출 해야함 (여러 인스턴스들이 공유 한다고 생각)
self_test.function2() # 인스턴스 호출 하거나 클래스 호출 시 인자 넣어줌

print(id(self_test))
SelfTest.function2(self_test)


# ex3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 (모두가 공유한다 !!)
    stock_num = 0 # 하나의 변수를 통해 모든 인스턴스가 공유 하는 코딩 가능
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스에서 변수를 찾고 거기에도 없으면 에러

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1 # 인스턴스 삭제 

print(user2.stock_num)
print(user3.stock_num)



