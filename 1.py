
import keyword
print(keyword.kwlist) # keyword 키워드를 불러옴

print(bool('')) # False

# 10진수
x = 42
print(x)    # 출력: 42

# 2진수
y = 0b101010
print(y)    # 출력: 42

# 8진수
z = 0o52
print(z)    # 출력: 42

# 16진수
w = 0x2a
print(w)    # 출력: 42

# 실수로 바꾸는 float() 함수
print(float(10))
print(float("3.14"))

# 복소수 생성
z1 = 2 + 3j
z2 = complex(4, -2)

# 복소수 연산
z3 = z1 + z2
z4 = z1 * z2
z5 = z1 / z2  # 복소수 나눗셈은 잘 모르겠다.
z6 = z1 ** 2

# 결과 출력
print(z3)   # (6+1j)
print(z4)   # (14+8j)
print(z5)   # (-0.4+0.7j) 
print(z6)   # (-5+12j)

z = 3 + 4j
print(z.real)  # 출력: 3.0
print(z.imag)  # 출력: 4.0


greeting = "Hello"
name = "John"
message = greeting + ", " + name + "!"
print(message) # "Hello, John!" 출력

word = "spam"
repeated = word * 3
print(repeated) # "spamspamspam" 출력

string = "Hello, World!"
position = string.find("World")
print(position) # 7 출력

a = True
b = False

print(a and b)   # 출력: False
print(a or b)    # 출력: True
print(not a)     # 출력: False

num = 10
text = "apple"
print(str(num) + text)

# 타입 변환
num = 10
float_num = float(num)
str_num = str(num)
bool_num = bool(num)
'''
print(num)
print(float_num)
print(str_num)
print(bool_num) # True 가 출력됨
'''
print(type(num))         # <class 'int'>
print(type(float_num))   # <class 'float'>
print(type(str_num))     # <class 'str'>
print(type(bool_num))    # <class 'bool'>

# 리스트
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)
fruits.append('orange')
print(fruits)
fruits.pop()
print(fruits)

# 튜플. 상수랑 비슷. 수정 삭제 추가 불가능 
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[1])

# 딕셔너리
fruits = {"apple": 3, "banana": 2, "cherry": 5}
print(fruits)
print(fruits["banana"])
fruits["orange"] = 4
print(fruits)
print(fruits.keys()) # 키 값 가져오기
print(3 in fruits.values()) # 밸류에 3 이 있는지 확인


'''  구구단 19단까지 출  
for i in range(2,20):
    for each in range(2,20):
        print(i, 'X', each,' = ' , i* each)
'''

# 멤버쉽 연산자 주어진 데이터가 자료형 안에 있는지 확인
# 시퀀스형 자료 (문자열, 리스트, 튜플, 세트) in not in 을 사용

# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력 대소문자 구
print("O" in b)  # False 출력
print("k" not in b)  # True 출력

# 식별 연산자
#두 개의 변수가 동일한 객체를 가리키는지 여부를 확인하는
#연산자입니다. is와 is not 연산자를 제공합니다
# 식별 연산자 사용 예제
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # False 출력
print(a is not b)  # True 출력
print(a is c)  # True 출력
print(b is not c)  # True 출력

# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print("I'm a boy.")  # "I'm a boy." 출력
# 탈출문자 \" , \'
print("He said, \"Hello!\"")  # He said, "Hello!" 출력 
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is %5s, I'm %d years old, and my height is %.1f." % (name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 출력 형식 지정 예제
num = 10
pi = 3.14159265

print("num = %d" % num)  # 출력 결과: "num = 10"
print("pi = %f" % pi)  # 출력 결과: "pi = 3.141593"
print("pi = %.2f" % pi)  # 출력 결과: "pi = 3.14"
print("pi = %10.2f" % pi)  # 출력 결과: "pi =       3.14" 공백 10자리 찍어냄 


''' format() 메소드를 이용한 포매팅 '''
name = "John"
age = 30
height = 175.5

print("My name is {}, I'm {} years old, and my height is {:.1f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 문자열
name = "John"
print("Hello, {}!".format(name))

# 정수
num = 42
print("The answer is {}.".format(num))

# 실수
pi = 3.14159
print("Pi is approximately {:.2f}.".format(pi))

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# 인덱스를 이용한 대입
print("My name is {1} {0} and I am {2} years old.".format(last_name, first_name, age))

# 인덱스를 이용한 포매팅 예제
name = "John"
age = 30
height = 175.5

print("My name is {0}, I'm {1} years old, and my height is {2:.1f}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."


'''f-string을 이용한 포매팅'''
# f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name:0>10}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

name = 'Tom'
age = 20
num_apple = 3
num_orange = 2
num_banana = 1
print(f'My name is {0} and I am {1} years old.'.format(name,age))
print(f'I have {num_apple} apples, {num_orange} oranges, and {num_banana} banana.')

a = 1.23
s = '90%'
b = 10
c= 20
d = b+c
print(f'The result is {a:.3f}')
print(f'Your score is {s}')
print(f'{b} + {c} = {d}')


''' input() 함수를 이용하여 사용자로부터 입력 받기'''

'''
name = input("What is your name? ")
print(f"Hello, {name}!")
'''

# input() 함수를 이용하여 사용자로부터 입력받아 계산하기
'''
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division:.2f}")
'''

# input(), 포매팅, 산술식을 이용하여 계산하기
'''
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

result = f"""
입력한 숫자:
첫 번째 숫자: {num1}
두 번째 숫자: {num2}

산술 연산 결과:
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} * {num2} = {num1 * num2}
{num1} / {num2} = {num1 / num2:.2f}
"""

print(result)

'''


# input()과 산술식만을 이용하여 가장 큰 숫자 출력하기
'''
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

max_num = num1

if max_num < num2:
    max_num = num2

if max_num < num3:
    max_num = num3

print(f"입력한 숫자 중 가장 큰 수는 {max_num}입니다.")
'''

#"사과 쇼핑몰"에서 사과를 구매할 때, 총 가격을 계산하는 프로그램을 작성하세요.
'''
num = int(input("사과의 개수"))
price = int(input("사과 가격"))
tax = float(input("부가세율 (%)"))

price = price *(1 + tax/100)
print(f'부가세를 포함한 사과 {num}개의 소비자 가격은 {(price*num):.0f}입니다.')
'''

#초를 입력하면 분과 초로 표시하는 프로그램. 예를 들어, 200초를 입력하면 3분 20초로 표현하라
'''
time = int(input("시간(초)을 입력하세요."))
m = time // 60
s = time % 60

print(f"{m}분 {s}초")
'''
# 분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램을 만들어라. (예 : 1550분은 1일 1시간 50분)
'''
time = int(input("시간을 입력하세요."))
day = time // 1440
temp = time % 1440
h = temp // 60
m = temp % 60
print(f'{time}분은 {day}일 {h} 시간 {m}분 ')
'''

# 500만원을 년이율 5%로 복리 저금했을 때 5년 후의 원리금의 합계를 출력하는 프로그램
deposit = int(input("금액을 입력하세요(만원)"))
price = deposit
rate = int(input("연 이율을 입력하세요 (%)"))
deposit += deposit*rate/100 # 1년 지났을 때 받는 금액
deposit += deposit*rate/100
deposit += deposit*rate/100
deposit += deposit*rate/100
deposit += deposit*rate/100

print(f"{price}만원을 년이율 {rate}%로 복리 저금 했을 때 5년 후 금액은 {deposit:.2f}만원 입니다.")

# 1부터 n까지의 합은 n(n+1)/2로 주어진다.
# 1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.
add = lambda a : a*(a+1)/2
print(add(100))

#판매자가 딸기와 포도를 판매하고 있다.
#포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
#사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여
#출력하는 프로그램을 작성하고 실행하라.
'''
podo = int(input("포도의 개수를 입력하세요."))
berry = int(input("딸기의 개수를 입력하세요."))

print(f'포도 {podo} 개, 사과 {berry}개의 무게는 {((podo*75 + berry*113.5)/1000):.3f}kg입니다.')
'''



