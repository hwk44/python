# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# keys 함수를 사용하여 딕셔너리의 키를 리스트로 변환
keys_list = list(fruits.keys())
print(keys_list)  # ['apple', 'banana', 'orange']

# values 함수를 사용하여 딕셔너리의 값을 리스트로 변환
values_list = list(fruits.values())
print(values_list)  # [3, 2, 1]

# items 함수를 사용하여 딕셔너리의 (키, 값) 쌍을 리스트로 변환
items_list = list(fruits.items())
print(items_list)  # [('apple', 3), ('banana', 2), ('orange', 1)]


# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# get 함수를 사용하여 딕셔너리에서 특정 키에 해당하는 값을 가져옴
print(fruits.get('apple'))  # 3
print(fruits.get('grape'))  # None

# setdefault 함수를 사용하여 딕셔너리에 새로운 (키, 값) 쌍 추가
fruits.setdefault('grape', 5)
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 5}

# pop 함수를 사용하여 딕셔너리에서 특정 키의 (키, 값) 쌍 제거하고 값을 반환
grape_count = fruits.pop('grape')
print(grape_count)  # 5
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1}

# update 함수를 사용하여 딕셔너리에 다른 딕셔너리의 (키, 값) 쌍 추가 또는 업데이트
new_fruits = {'pear': 2, 'apple': 5}
fruits.update(new_fruits)
print(fruits)  # {'apple': 5, 'banana': 2, 'orange': 1, 'pear': 2}


'''
다음 딕셔너리에 대해 물음에 답하라.
days = {'January':31, 'February':28, 'March':31,
'April':30,'May':31, 'June':30, 'July':31,
'August':31,'September':30, 'October':31, 'November':30, 'December':31}
사용자가 월을 입력하면 해당 월에 일수를 출력하라
알파벳 순서로 모든 월을 출력하라
일수가 31인 월을 모두 출력하라
월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
'''

days = {'January':31, 'February':28, 'March':31,
'April':30,'May':31, 'June':30, 'July':31,
'August':31,'September':30, 'October':31, 'November':30, 'December':31}

# 사용자가 월을 입력하면 해당 월에 일수를 출력하라
'''
s = input("월을 입력하세요")
print(days.get(s.title()))
'''

print(days['April'])
# 알파벳 순서로 모든 월을 출력하라
print(sorted(days.keys()))

# 일수가 31인 월을 모두 출력하라

for i in days:
    if(days.get(i) == 31):
        print(i)
# print(days.values())
# print(days.keys())

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
days_item = days.items()

days_item = [(day, month) for (month, day) in days_item]
# print(days_item)
print(sorted(days_item)) # 튜플로?

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
'''
s = input("월을 세자리만 입력하세요.")
# s= s.title
# print(days[s.title()])
for x in days:
    if x[0:3] == s.title():
        print(days[x])   
'''     

'''
다음 딕셔너리에 대해 물음에 답하라.
'''
d=[{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}
    ]

# 전화번호가 8로 끝나는 사용자 이름을 출력하라
for i in d:
    if i['phone'][-1] == '8':
        print(i['name']) 
# 이메일이 없는 사용자 이름을 출력하라
for i in d:
    if i['email'] == '':
        print (i['name'])

# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라.
# 이름이 없으면 '이름이 없습니다'라는
# 메시지를 출력하라
'''
s = input("name to search : ")

flag = 1

for i in d:
    if i['name'] == s.title():
        print(i['name'], " : ", i['email'])
        flag = 0
if flag == 1:
    print("이름이 없습니다.")
'''    

''' set
set은 중복을 허용하지 않는 집합을 나타내는 자료형입니다. 
set은 {}를 사용하여 생성할 수 있지만, 중괄호 {}는 딕셔너리와도 비슷하기 때문에
set() 생성자를 사용하는 것이 좋습니다.

set은 리스트, 튜플 등의 이터러블 객체를 받아들입니다.
set은 생성할 때 자동으로 중복된 원소를 제거합니다.

set은 순서가 없기 때문에 인덱싱을 지원하지 않습니다. 
하지만 in 연산자를 이용하여 특정 원소가 set에 포함되어 있는지를 확인할 수 있습니다.
또한, 수학에서 집합 연산에 사용하는 교집합, 합집합, 차집합 등의 연산도 가능합니다.

'''

my_set = {1, 2, 3, 3, 4, 5, 5}
print(my_set) # {1, 2, 3, 4, 5}

my_set = set([1, 2, 3, 3, 4, 5, 5])
print(my_set) # {1, 2, 3, 4, 5}

mset = set()
mset.add(1)
mset.add(2)
mset.add(3)
mset.add(3)
mset.add(4)
mset.add(5)
print(mset) # {1, 2, 3, 4, 5}

# set 생성
my_set = {1, 2, 3}

# 개수 확인
print(len(my_set))  # 출력: 3

# 요소 추가
my_set.add(4)# set 생성
my_set = {1, 2, 3}

# 개수 확인
print(len(my_set))  # 출력: 3

# 요소 추가
my_set.add(4)
print(my_set)  # 출력: {1, 2, 3, 4}

# 여러 요소 추가
my_set.update([5, 6, 7])
print(my_set)  # 출력: {1, 2, 3, 4, 5, 6, 7}

# 요소 제거 (remove)
my_set.remove(3)
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}

# 요소 제거 (discard)
my_set.discard(10)  # 요소가 없어도 오류 발생하지 않음
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}



'''
집합 연산
합집합(Union) 연산: set1 | set2 또는 set1.union(set2)
교집합(Intersection) 연산: set1 & set2 또는 set1.intersection(set2)
차집합(Difference) 연산: set1 - set2 또는 set1.difference(set2)
대칭차집합(Symmetric Difference) 연산: set1 ^ set2 또는 set1.symmetric_difference(set2)
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1 | set2)       # {1, 2, 3, 4, 5}

# 교집합
print(set1.intersection(set2))  # {3}
print(set1 & set2)              # {3}

# 차집합
print(set1.difference(set2))  # {1, 2}
print(set1 - set2)            # {1, 2}

# 대칭차집합
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
print(set1 ^ set2)                      # {1, 2, 4, 5}

# == 연산자 예시
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {4, 5, 6}
print(set1 == set2) # True
print(set1 == set3) # False

# >, >= 연산자 예시
set4 = {1, 2, 3, 4}
set5 = {1, 2, 3}
print(set4 > set5)  # True
print(set4 >= set5) # True
print(set5 > set4)  # False
print(set5 >= set4) # False


#clear() : set의 모든 요소를 제거합니다.

my_set = {1, 2, 3}
my_set.clear()
print(my_set) # 출력: set()

# pop() : set에서 요소를 제거하고 반환합니다. 
# set이 비어 있을 경우 KeyError 예외를 발생시킵니다.

my_set = {1, 2, 3}
popped = my_set.pop()
print(popped) # 출력: 1
print(my_set) # 출력: {2, 3}


'''1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램'''
myset = set([]) # myset = {} 로 생성하게 되면 myset 은 딕셔너리가 되어서 오류남
import random
# print(random.randint(1,45))

while len(myset) < 6:
        myset.add(random.randint(1,45))
print(myset)

fruits = ['apple', 'banana', 'cherry', 'date']

# 길이 기준으로 정렬
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)
# 출력 결과: ['date', 'apple', 'banana', 'cherry']


# 학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.

scores = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

print("Average grades : ")
# print(scores.items())

for name, score in scores.items():
    print("{} : {:.0f}".format(name ,sum(score)/len(score)))

for name, score in scores.items():
    print (name, end=" : ")
    avg = 0
    for i in score:
        avg += i
    avg /= 3
    print("{:.0f}".format(avg))
    
'''
숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 
남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
'''
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set1 = set(list1)
print(sum(set1))

set1.clear()
'''
주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
'''
text = "Hello, world!"

dic1 = {}
for char in text:
    if char not in dic1:
        dic1[char] = 1
    else:
        dic1[char] += 1
print(dic1)

'''
두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를
반환하는 프로그램을 작성하시오.

리스트A: 임의의 길이와 요소를 가진 리스트
리스트B: 임의의 길이와 요소를 가진 리스트
'''
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

# 공통된 요소인 2와 4를 모두 포함한 리스트를 반환한다.
# 결과값
# [2, 4]
print(list(set(list1) & set(list2)))              # {3}


'''
함수의 정의와 호출 방법
함수를 정의한 이후에는 함수를 호출하여 사용할 수 있습니다. 
함수를 호출할 때는 함수 이름 뒤에 인자를 괄호 안에 지정하여 호출합니다. 
함수가 호출되면 인자를 전달하고, 함수 내부에서 지정한 처리가 수행됩니다. 
함수는 실행 결과를 반환하는데, 반환되는 값은 return 키워드를 사용하여 지정합니다.
'''
# 함수 정의
def add_numbers(a, b):
    result = a + b
    return result

# 함수 호출
result = add_numbers(3, 5)
print(result)   # 출력 결과: 8

#1~n까지의 합을 계산하는 함수
def sumof10():
    result = 0
    for i in range(1, 11):
        result += i
    return result
print(sumof10())

# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와
# 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 이들 함수를
# 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 
# 첫 자리까지 구하라.

def cir_area(r):
    import math
    return  math.pi*r*r
print("{:.1f}".format(cir_area(3.5)))

def cir_cirm(r):
    import math
    return math.pi*2*r
print("{:.1f}".format(cir_cirm(3.5)))

#den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
#12 -> [1, 2, 3, 4, 6, 12]
def den(n):
    cd = []
    for i in range(1,n+1):
        if n%i == 0:
            cd.append(i)
    return cd
print(den(40))


# 위치 인자와 키워드 인자 사용 예시
def print_info(name, age, gender):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")

# 위치 인자를 사용하여 함수 호출
print_info("Alice", 25, "Female")

# 키워드 인자를 사용하여 함수 호출
print_info(age=30, name="Bob", gender="Male")



# 가변 인자와 기본값 인자 사용 예시
def print_numbers(*args, sep=", "):
    print(sep.join(map(str, args)))

# 가변 인자를 사용하여 함수 호출
print_numbers(1, 2, 3)               # 출력 결과: 1, 2, 3
print_numbers(1, 2, 3, sep="-")      # 출력 결과: 1-2-3

# 기본값 인자를 사용하여 함수 호출
def say_hello(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

say_hello("Alice")                  # 출력 결과: Hello, Alice!
say_hello("Bob", "Hi")              # 출력 결과: Hi, Bob!


# 인자의 순서와 조합 사용 예시
def print_numbers(a, b, *args, c=10, d=20):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
print_numbers(1, 2, 3, 4, 5, c=30, d=40)
# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5)

x = 'global'

def my_function():
    global x # 전역 변수를 함수에 가져와 쓰겠다는 선언
    x = 'local' # 전역 변수가 바뀜
    print(x)
my_function()
print(x)

# 기존 함수 정의 방법
def add(a, b):
    return a + b

# 람다 함수 정의 방법
lambda_add = lambda a, b: a + b

# 함수 호출
result1 = add(3, 4)             # 7
result2 = lambda_add(3, 4)      # 7


# 함수의 인자로 전달된 예시
students = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
]

# 점수(score)를 기준으로 학생 리스트 정렬
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
print(sorted_students)
# 출력 결과: [{'name': 'Bob', 'score': 90}, {'name': 'Alice', 'score': 80}, {'name': 'Charlie', 'score': 70}]


"""
1.두 개의 매개변수 n, m을 전달받아 n x m개의 * 상자를 출력하는 프로그램을 함수로 작성
예: 2, 4  **** 
          ****

2. 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
예: 123  1+2+3 = 6

3. 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
4. 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
5. 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
"""
'''
def _1(n, m):
    for i in range(1, n+1):
        for i in range(1, m+1):
            print("*", end="")
        print("")  
    return
_1(4,5)

def _2():
    s = []
    num = str(input("숫자를 입력하세요."))
    for i in num:
        s.append[i]      
    
_2()
'''
def get_operator(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '/':
        return lambda a, b: a / b



'''
내부함수를 이용한 계산기
'''
def calculator():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    return add, subtract, multiply, divide # 튜플로 반환

add, subtract, multiply, divide = calculator() # 튜플

print(add(10, 20))  # 출력결과: 30
print(subtract(10, 20))  # 출력결과: -10
print(multiply(10, 20))  # 출력결과: 200
print(divide(10, 20))  # 출력결과: 0.5


# 내부 함수는 코드의 재사용성을 높일 수 있다
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)  # 제곱 함수를 구현
cube = power(3)  # 세제곱 함수를 구현

print(square(3))  # 출력결과: 9
print(cube(3))  # 출력결과: 27



# 함수의 반환값으로 람다 함수 사용
add_func = get_operator('+')
result1 = add_func(3, 4)  # 7
print(result1)

multiply_func = get_operator('*')
result2 = multiply_func(3, 4)  # 12
print(result2)

def sum_numbers(*args):
    result = 0
    for arg in args:
        result += arg
    return result

# 가변 인자를 사용하여 함수 호출
result1 = sum_numbers(1, 2, 3, 4, 5)   # 15
result2 = sum_numbers(1, 2, 3)         # 6
result3 = sum_numbers(1, 2)            # 3


# 함수 내 변수 참조 순서
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)






