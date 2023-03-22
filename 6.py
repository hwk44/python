# 5장
'''
class 클래스이름:
    # 클래스 멤버 변수
    클래스변수 = 값

    # 생성자 메서드
    def __init__(self, 매개변수):
        # 인스턴스 멤버 변수
        self.인스턴스변수 = 매개변수

    # 인스턴스 메서드
    def 메서드이름(self, 매개변수):
        # 메서드 내용
'''
class Rectangle:

    count = 0

    def __init__(self, width, height): # 생성자
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self): # 인스턴스 메소드
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 인스턴스 생성 시 생성자 메서드 호출
rectangle1 = Rectangle(3, 4)
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12

# 인스턴스 생성
rectangle2 = Rectangle(5, 6)

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30

# 인스턴스 변수 값 변경
rectangle1.width = 5
print(rectangle1.width) # 출력 결과: 5

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 20

# 클래스 변수 값을 출력
print(Rectangle.count) # 출력 결과: 2

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle3 = Rectangle(7, 8)
print(Rectangle.count) # 출력 결과: 3

rectangle4 = Rectangle(8, 9)
print(Rectangle.count) # 출력 결과: 4

print(rectangle1.perimeter()) # 출력 결과: 18


# 인스턴스 메서드 자전거 클래스
class Bicycle:
    # 생성자 메서드
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    # 인스턴스 메서드
    def speed_up(self, increment):
        self.speed += increment

    def apply_brake(self, decrement):
        self.speed -= decrement

# Bicycle 클래스를 이용하여 객체 생성
my_bike = Bicycle(6, 0)
print(my_bike.speed)  # 출력 결과: 0

# 인스턴스 메서드 호출
my_bike.speed_up(3)
print(my_bike.speed)  # 출력 결과: 3

my_bike.apply_brake(1)
print(my_bike.speed)  # 출력 결과: 2



#  클래스 메서드
'''인스턴스가 아닌 클래스에 대한 작업을 수행하기 위해 사용되므로,
 객체의 인스턴스 변수에 대한 접근이 불가능합니다. 따라서, 
클래스 메서드는 인스턴스를 통해 호출되는 것이 아니라, 
클래스 이름을 이용하여 직접 호출됩니다'''
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
# 클래스명.메서드명
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2


# 계산기 클래스. 생성자가 없음
class Calculator:
    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2

# Calculator 클래스를 이용하여 객체 생성
my_calculator = Calculator()
print(my_calculator.calculate(2, 3)) # 출력 결과: 5

# 클래스 메서드 호출
Calculator.set_operator('*')
print(my_calculator.calculate(2, 3)) # 출력 결과: 6

'''
    Deposit 클래스를 생성하라.
    이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
    initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
    초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
    
    인스턴스 메소드 profit()은 n년 후 원리금을 반환한다.
    n년 후 원리금은 initial * (1 + interest)n이다. 
    Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 
    원리금을 구하는 프로그램을 작성하라. 단 원리금은 정수로 표시되어야 한다.
'''
class Deposit:

    def __init__(self, initial, interest, n):
        # initial : 원금(원), interest: 이자율 (1% => 0.01)
        self.initial = initial
        self.interest = interest
        self.n = n

    def profit(self):
        return int(self.initial *(1+ self.interest) ** self.n)

deposit1 = Deposit(1000000,0.035,7)
print(deposit1.profit())


# 캡슐화
# 클래스나 모듈 안에 정의된 변수나 함수에 직접 접근할 수 없게 하는 것
# 인스턴스 변수 이름 앞에
# 밑줄 두 개(__)를 붙여서 비공개 인스턴스 변수로 만들어 캡슐화를 구현

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # age 인스턴스 변수를 비공개로 설정 게터와 세터로 접근

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

p = Person("John", 30)
print(p.get_name())  # "John" 출력
p.set_name("Alice")
print(p.get_name())  # "Alice" 출력

# 연습문제
#예제의 Teacher 클래스에서 People 클래스의 __init__()를 호출하지 않고
# 부모 클래스의 age, name 인스턴스 변수를 이용할 수 있는가? 이용할 수 없다면
# 그 이유는? 이용할 수 있게 하려면 프로그램을 어떻게 수정해야 하는가?

class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, ", age :", str(self.__age))

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t = Teacher(20,"길동","죽전초")
t.showSchool()
t.set_name("Lee")
t.showSchool()

'''
다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라
Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
getID() 메소드는 employeeID를 반환하는 메소드이다.
Employee 클래스를 이용하여 Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력하라.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def showInfo(self):
        print("이름 : " , self.name ,  ", 나이 : " , self.age)

class Employee(Person):
    def __init__(self,name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID

    def showInfo(self):
        super().showInfo()
        print("ID : " , self.employeeID)

e = Employee("adam", 29, "E4123")
e.showInfo()


## 다중 상속
'''
파이썬에서는 다중 상속을 통해 클래스 간의 관계를 유연하게 구성할 수 있습니다.
 하지만 다중 상속을 남용하면 코드의 복잡도가 증가하고 유지보수가 어려워질 수 있으므로, 
 적절한 상황에서 사용해야 합니다.
'''
class Parent1:
    def method1(self):
        print("Parent1's method1")

class Parent2:
    def method2(self):
        print("Parent2's method2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.method1()  # Parent1's method1
c.method2()  # Parent2's method2

# 메소드 오버라이딩
class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

# 메서드 오버라이딩을 이용한 다형성 구현
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() # 각 객체에 따라 다른 동작을 수행


#게임 캐릭터 구현 예시
class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with a normal attack.")


class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength

    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")

    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")


class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic

    def attack(self):
        print(f"{self.name} casts a magic missile.")

    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")


c = Character("Bob", 10, 100)
c.attack()  # Bob attacks with a normal attack.

w = Warrior("Conan", 20, 200, 15)
w.attack()  # Conan attacks with a mighty swing.
w.smash()   # Conan smashes the ground with a powerful blow.

m = Mage("Merlin", 15, 150, 30)
m.attack()  # Merlin casts a magic missile.
m.teleport()  # Merlin teleports to a nearby location.


# 클래스 분리가 안되었을때
'''
class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break
game = Game("Alice",120,15, "Goblin", 60, 8)
game.fight()
'''

# 클래스 분리
# player 클래스
class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

# monster 클래스
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

#game 클래스
class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    def create_player(self, name, hp, attack):
        self.player = Player(name, hp, attack)

    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break
game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()


# 추상 클래스
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class Bike(Vehicle):
    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")


vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


''' 
다형성은 같은 이름의 메서드나 함수가 다른 객체에서 다른 동작을 하도록 만드는 기술입니다.
전달된 인자에 따라 함수 또는 연산의 기능이 달라지는 기능
2 + 3  5
'2' + '3'  '23'
'Hello ' + 'World'  'Hello World'
'''

class 동물:
    def 소리내기(self):
        pass

class 개(동물):
    def 소리내기(self):
        print("멍멍!")

class 고양이(동물):
    def 소리내기(self):
        print("야옹!")

def 동물들_소리내기(동물_리스트):
    for 동물_인스턴스 in 동물_리스트:
        동물_인스턴스.소리내기()

개_인스턴스 = 개()
고양이_인스턴스 = 고양이()

동물들 = [개_인스턴스, 고양이_인스턴스]
동물들_소리내기(동물들)

class 동물:
    def 소리내기(self):
        print("동물이 소리를 냅니다.")

class 개(동물):
    def 소리내기(self):
        print("멍멍!")

class 고양이(동물):
    def 소리내기(self):
        print("야옹!")

def 동물소리내기(동물_인스턴스):
    동물_인스턴스.소리내기()

개_인스턴스 = 개()
고양이_인스턴스 = 고양이()

동물소리내기(개_인스턴스)   # 결과: 멍멍!
동물소리내기(고양이_인스턴스) # 결과: 야옹!

'''
문제: 학생 정보를 관리하는 프로그램을 만드세요.
학생(Student) 클래스
인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적(avg_score)
메서드: get_info() - 학생의 정보를 문자열로 반환
'''

class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score

    def get_info(self):
       # return f"이름:{self.name}, 학번 : {self.student_id}, 학년 : {self.year}, " \
        #       f"전공 : {self.major}, 평균 성적 : {self.avg_score}"
        print("이름 : " ,self.name, ", 학번 : " , self.student_id , ", 학년 : ", self.year
              , ", 전공" ,self.major , ", 평균 성적" ,self.avg_score)

s = Student("길동",230001, 2, "바이올린", "A")
# print(s.get_info())

'''
학생들을 관리하는 클래스(StudentManager)
인스턴스 변수: 학생들(student_list)
메서드:
add_student(student): 학생을 리스트에 추가하는 메서드
remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
find_student(student_id): 학번을 이용해 학생을 찾는 메서드
show_all_students(): 모든 학생의 정보를 출력하는 메서드
'''
class StudentManager:
    def __init__(self):
        self.student_list= []

    def add_student(self,student_id):
        self.student_list.append(student_id)

    def remove_student(self,student_id):
        for s in self.student_list:
            if(s.student_id == student_id):
                self.student_list.remove(s)
                return

    def find_student(self,student_id):
        for s in self.student_list:
            flag = 0
            if(s.student_id == student_id):
                flag = 1
                break
        if(flag == 1):
            print("항목에 있습니다.")
        else:
             print("항목에 없습니다.")

    def show_all_students(self):
        for s in self.student_list:
            s.get_info()

sm = StudentManager()
student1 = Student("영희",220002, 3, "호텔경영", "B+")
student2 = Student("기영",210045, 4, "전자공학", "B")
student3 = Student("기봉",230068, 2, "컴퓨터공학", "A+")

sm.add_student(s)
sm.add_student(student1)
sm.add_student(student2)
sm.add_student(student3)

sm.find_student(230068)
sm.show_all_students()
print("-----------------------")

sm.find_student(210045)
sm.remove_student(210033)
student3.name = "기철"
sm.show_all_students()




