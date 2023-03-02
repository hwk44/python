# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
'''
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")
'''

# 사용자로부터 성적을 입력받아, 학점 부여하기
'''
score = int(input("성적을 입력하세요: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")
'''


### 한 문장의 if-else 문

num = 10
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)

## 성적을 입력받아 학점을 출력하는 프로그램
'''
score = int(input("성적을 입력하세요: "))
grade = "A"
if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)
'''

# 변수 a와 b 중 값이 큰 변수를 출력하는 프로그램
a = 10
b = 20
result = a if a > b else b
print(result)

#세 개의 수 중 가장 작은 수를 출력하는 프로그램

a = 10
b = 20
c = 5
min_value = a if a < b and a < c else (b if b < c else c)
print("가장 작은 수는", min_value, "입니다.")

#입력한 문자열의 길이를 출력하는 프로그램
'''
string = input("문자열을 입력하세요: ")
length = len(string) if string else 0
print("문자열의 길이는", length, "입니다.")
'''

'''사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아,
각 과목의 평균 점수와 총 평균 점수를 계산한 후,
학점을 출력하는 프로그램을 작성하세요.
평균 점수는 소수점 둘째자리까지 출력합니다.
총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
총 평균 점수가 90점 이상인 경우 "A",
80점 이상인 경우 "B", 70점 이상인 경우 "C",
60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.
'''
'''
kor = int(input("국어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
          
sum = kor + math + eng
avg = float((sum)/3)
print(sum)
print(avg)
avg_total = (kor*0.4 + eng*0.4 + math*0.2)

grade = ""
if
'''

# 중첩 if문은 if문 내부에 다시 if문을 사용하여 구현

'''if 조건식1:
    # 조건식1이 참(True)일 때 실행되는 코드
    if 조건식2:
        # 조건식1과 조건식2가 모두 참일 때 실행되는 코드
    else:
        # 조건식1은 참이고, 조건식2는 거짓(False)일 때 실행되는 코드
else:
    # 조건식1이 거짓일 때 실행되는 코드
'''

# 사용자로부터 입력받은 두 개의 수 중에서 큰 수를 찾아 출력하는 프로그램
'''
num1 = float(input("첫 번째 수를 입력하세요: "))
num2 = float(input("두 번째 수를 입력하세요: "))

if num1 > num2:
    print("큰 수는", num1, "입니다.")
else:
    if num1 == num2:
        print("두 수는 같습니다.")
    else:
        print("큰 수는", num2, "입니다.")
'''

score = 75

if score >= 90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    if score >= 85:
        grade = "B+"
    else:
        grade = "B"
elif score >= 70:
    if score >= 75:
        grade = "C+"
    else:
        grade = "C"
elif score >= 60:
    if score >= 65:
        grade = "D+"
    else:
        grade = "D"
else:
    grade = "F"

print("등급:", grade)

'''사용자로부터 cm 단위의 길이를 입력 받는다. 입력 값이 음수이면
"잘못 입력하였습니다"라는 메시지를 출력하고 양수이면
길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 1인치 = 2.54cm
'''
'''
length = int(input("길이를 입력하세요."))

if length < 0:
    print("잘못 입력하였습니다.")
else:
    print(f"{float(length/2.54):.2f} Inch")
'''

'''
사용자로부터 이수한 학점을 입력 받는다.
학점이 40학점 미만이면 "1학년입니다"를 출력하고,
40이상 80미만이면 "2학년입니다"를 출력한다.
학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.
'''
'''
sum_ = int(input("이수한 학점을 입력하세요."))

if sum_ < 40:
    print("1학년입니다.")
elif sum_< 80:
    print("2학년입니다.")
else:
    print("졸업반입니다.")
'''   
    
'''
사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다
이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
'''
'''
hour = int(input("Enter hour"))
s = int(input("am (1) or pm (2)?"))
time = int(input("How many hours ahead?"))

if s == 1:
    s = 0
elif s == 2:
    s=12

newtime = (hour + s + time)%24

if newtime >24:
    newtime %= 24

if newtime > 12:
    newtime = str(f"{newtime%12}  pm")
else:
    newtime = str(f"{newtime}  am")
print("newhour : " , newtime)
'''
'''
sum = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    sum += num
print("입력한 값들의 합: ", sum)

'''
'''
max_value = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    if num > max_value:
        max_value = num
print("가장 큰 값: ", max_value)
'''

'''
num = int(input("10진수를 입력하세요: "))
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("입력한 수의 2진수 표현: ", binary)
'''


''' for 문'''
# 리스트의 원소를 순차적으로 출력하는 예제
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
#리스트에 저장된 모든 수의 합을 구하는 코드
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)

#튜플의 원소를 순차적으로 출력하는 예제
colors = ("red", "green", "blue")

for color in colors:
    print(color)

#문자열의 각 문자를 순차적으로 출력하는 예제
text = "Python"
for char in text:
    print(char)



# 1-10 출력
for i in range(1, 11):
    print(i)
print("-----------------------------")
# 1- 10 짝수만 출력
for i in range(2, 11, 2):
    print(i)
print("-----------------------------")
# 10 - 1 거꾸로 출력 
for i in range(10, 0, -1):
    print(i)
print("-----------------------------")

# range 내장함수 리스트와 비슷한 range 객체 반환
# range(start, stop, step)

# 0에서 4까지의 정수 시퀀스 생성
'''
for i in range(5):
    print(i)
print("-----------------------------")

# 2에서 8까지 2씩 증가하는 정수 시퀀스 생성
for i in range(2, 9, 2):
    print(i)
print("-----------------------------")

# 10에서 1까지 1씩 감소하는 정수 시퀀스 생성
for i in range(10, 0, -1):
    print(i)
print("-----------------------------")
'''

# 별문자 모양 그리기
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="") # end="" java에서 System.out.print() 랑 같음
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
'''

# 3의 배수와 5의 배수의 합 구하기
'''
사용자로부터 양의 정수 n을 입력받아, 1부터 n까지의 자연수 중에서
3의 배수와 5의 배수의 합을 구하고, 이를 출력하는 프로그램을 작성하세요.
사용자로부터 입력받는 정수 n은 1 이상의 양의 정수입니다.
자연수 1부터 n까지의 숫자 중에서 3의 배수 또는 5의 배수인 숫자들의 합을 구합니다.
결과값은 정수형으로 출력합니다.
'''

'''
num = int(input("n = ? "))
if num < 0:
    print("자연수를 입력하세요.")
    num = int(input("n = ? "))
sum = 0

for i in range(1, num+1, 1):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(sum)
'''

'''
사용자로부터 5개의 정수형 숫자를 입력받아,
입력받은 숫자들 중에서 최댓값과 최솟값을 찾고,
이를 출력하는 프로그램을 작성하세요.
입력받은 숫자는 1 이상 100 이하의 자연수입니다.
입력받은 숫자 중 중복된 숫자가 있을 수 있습니다.
'''
'''
n1 = int(input("첫번째 정수를 입력하세요."))
min = n1
max = n1
n2 = int(input("두번째 정수를 입력하세요."))
if n2 < min:
    min = n2
if n2 > max:
    max = n2
n3 = int(input("세번째 정수를 입력하세요."))
if n3 < min:
    min = n3
if n3 > max:
    max = n3
n4 = int(input("네번째 정수를 입력하세요."))
if n4 < min:
    min = n4
if n4 > max:
    max = n4
n5 = int(input("다섯번째 정수를 입력하세요."))
if n5 < min:
    min = n5
if n5 > max:
    max = n5
'''
'''
min_num = 100
max_num = 0
for i in range(5):
    num = int(input(f"[최댓값과 최솟값 찾기]\n\n{i+1}번째 숫자를 입력하세요."))

    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
output = f"\n[결과]\n입력받은 숫자들: {[max_num, min_num]}\n최댓값:{max_num}\n최솟값:{min_num}"
print(output)
'''

'''
sum = 0
while (sum < 100):
    num = int(input("숫자를 입력하세요. : "))
    sum += num;
    if sum >100:
        break
    print("[숫자의 합이 100보다 작을 때까지 입력받기]")

print(f"입력받은 숫자들의 합 : {sum}")
'''

# 피보나치 수열의 n번째 항을 출력하는 프로그램
'''
n1 = 1
n2 = 1

n = int(input(f"몇번째 항을 출력할까요? (1 이상의 양의 정수) : "))

for i in range(2, n):
    if n ==1 or n ==2:
        num = 1
        break
    else:
        num = n1 + n2
        n1= n2
        n2 = num
print(f"피보나치 수열의 {n}번째 항은 {num}입니다.")

for i in range(1, 11):
    if i % 3 == 0:
        print(i)
    else:
        continue
    print("이 부분은 실행되지 않습니다.")  # continue문으로 이동했기 때문에 실행되지 않음
print("반복문이 종료되었습니다.")
'''

# 입력한 문자열에서 모음(a, e, i, o, u)을 제거하는 프로그램
'''
vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")

output_str = ""
for char in input_str:
    if char in vowels:
        pass
        print("패스")
       # continue
       # print("컨티뉴")
    else:
        output_str += char

    

print("Modified string:", output_str)
'''

'''
1~100 사이의 임의의 수가 선택되고 사용자가 숫자를 입력하면 입력한 숫자와 비교하여
"Up", "Down" 또는 "Correct!"를 출력합니다. 맞출 때까지 계속 입력할 수 있습니다.
'''

import random

# 1부터 100 사이의 임의의 수를 선택합니다
secret_number = random.randint(1, 100)
'''
while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로반복문을 종료합니다
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_numbers = random.sample(numbers, 3)
print(random_numbers)
# 출력 예시: [9, 1, 8]


# 도시와 날씨 리스트 정의
cities = ['서울', '부산', '인천', '대구', '광주', '대전']
weathers = ['맑음', '흐림', '비', '눈', '우박']

# 도시와 날씨를 무작위로 선택하여 출력
city = random.choice(cities)
weather = random.choice(weathers)
print(f'{city}의 날씨는 {weather}입니다.')

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print(f"주사위 1: {dice1}, 주사위2 : {dice2}, 합 : {dice_sum}")
    if dice_sum == 7:
        print("이겼습니다.")
        break
    else:
        print("다시 던집니다.")
        
        
'''
플레이어가 처음에 $50을 가지고 있다.
동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다.
맞추면 $9을 따고 틀리면 $10을 잃는다.
플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
동전을 던져서 나오는 수는 다음 문장을 이용하라.
'''

'''
deposit = 50

while (deposit > 0 and deposit < 100):
    coin = random.randint(1,2) # 1 또는 2 임의로 발생
    try_coin = int(input("동전을 맞춥니다. 앞면 (1) 뒷면 (2) : "))
    
    if coin == try_coin:
        deposit += 9
        print(f"맞췄습니다. 현재 금액 = {deposit}")
    else:
        deposit -= 10
        print(f"틀렸습니다. 현재 금액 = {deposit}")
'''

'''
두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
예를 들어 (16, 24)의 최대 공약수는 8이다.
두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을 작성하라.

큰 수를 작은 수로 나눈 나머지를 구하라 remainder
큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
작은 수가 0이 될 때까지 이 과정을 반목하라. 마지막 큰 수가 최대 공약수이다.
'''

'''
num1 = int(input("첫번째 숫자를 입력하세요. "))
num2 = int(input("두번째 숫자를 입력하세요. "))

# 두 수 정렬
if num1 > num2:
    pass
elif num2> num1:
    temp = num1
    num1 = num2
    num2 = temp

while True:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder
    if num2 == 0:
        break

print(f"최대공약수는 {num1} 입니다.")
'''

for i in range(1,10):
    if i%3 == 0:
        pass
    else:
        print(f'{i}는 3의 배수가 아닙니다.')
























