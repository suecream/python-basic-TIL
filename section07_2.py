# section07_2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# ex1
# 상속 기본
# 슈퍼클래스(부모), 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 예시) 라면 -> 속성(종류, 회사, 맛, 면 종류, 라면 이름) : 부모

class Car:
    """Parent Class""" # 이렇게 정의 해주는 것을 원칙으로 함
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "your Car Name : %s" % self.car_name

    def show(self):
        print(super().show()) # super method 도 호출 하고 싶으면
        return 'Car info : %s %s %s' % (self.car_name, self.type, self.color)
    

# 일반 사용 방법
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # super
print(model1.type) # super
print(model1.car_name) # sub
print(model1.show()) # super
print(model1.show_model()) # sub
print(model1.__dict__) # super, sub 둘다 참조

# Method Overriding(오버라이딩)
model2 = BenzCar('220d', 'suv', 'blue')
print(model2.show()) # 함수 이름이 같으면 sub에서 참조(개선, 재구현)

# Parent Method Call
model3 = BenzCar("AMG GT R", "coupe", "green")
print(model3.show())

# Inheritance Info (상속 정보)
print(BmwCar.mro())
print(BenzCar.mro()) # 소스 파악할 때 자주 사용하는 메소드

# ex2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass
    
class M(B, A ,Z):
    pass

print(M.mro()) # 너무 복잡한 다중 상속은 코드가 복잡해짐 (주의)
print(A.mro()) 


