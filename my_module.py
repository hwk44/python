def greet(name):
    print(f"Hello, {name}!")



def subtract(a, b):
    return a - b

if __name__ == '__main__':

    def add(a, b):
        return a + b
    print(add(3, 5))
    print(subtract(10, 7))

'''
이 모듈을 다른 모듈에서 import해서 사용할 경우 
if __name__ == '__main__': 이하의 코드는 실행되지 않습니다.
 하지만 이 모듈을 스크립트로 직접 실행할 때는 
 if __name__ == '__main__': 이하의 코드가 실행됩니다.
'''