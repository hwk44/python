'''
7장 예외처리 내용
'''

# ValueError: 잘못된 값이 사용될 때 발생
# num = int("not_a_number")
from astroid import ExceptHandler

# TypeError: 잘못된 타입의 객체가 사용될 때 발생
# result = "string" + 1

# IndexError: 인덱스 범위를 벗어난 경우 발생
#numbers = [1, 2, 3]
#out_of_range = numbers[3]

# KeyError: 사전에서 존재하지 않는 키를 참조할 때 발생
#my_dict = {"a": 1, "b": 2}
#value = my_dict["c"]

# FileNotFoundError: 존재하지 않는 파일을 열려고 시도할 때 발생
#with open("non_existing_file.txt", "r") as file:
 #   content = file.read()


try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# try:
#     # 예외가 발생할 수 있는 코드를 실행합니다.
#     file = open("non_existent_file.txt", "r")
#     result = 5 / 0
#     int("not_a_number")
# except FileNotFoundError as error:
#     print(f"An error occurred: {error}")
# except ZeroDivisionError as error:
#     print(f"An error occurred: {error}")
# except ValueError as error:
#     print(f"An error occurred: {error}")


data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}
'''
때 try-except문을 이용하여 다음과 같이 동작하는 프로그램을 작성하라.
사용자로부터 문자열을 입력 받는다
문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다
문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.
'''

try:
    s = str(input("문자열을 입력하세요."))
    value = data[s]
    print(value)
except Exception as e:
        print(f'an error occurred : {e}')

while True:
    try:
        user_input = input("enter a dat of the week")
        val = data.get(str.title(user_input))
        if val != None:
            print(val)
        else:
            print("항목이 없습니다.")
            break
    except :
        pass
