'''
reference - https://whatisthenext.tistory.com/113?category=761276
what is Decorator?
-> 하나의 함수를 취해서 또 다른 함수를 반환하는 함수.

언제 데코레이터를 쓰는가?

1) 로그를 남길 때
2) 유저의 로그인 상태를 확인하여 로그인 페이지로 redirect 할때.
3) 프로그램 성능을 위한 테스트

추가 참고 사이트 - http://www.hanbit.co.kr/media/channel/view.html?cms_code=CMS5689111564
'''

# ex1
# #num -> 인터프리터 순서.

def decorator_f(original_f): #1, #4
    def wrapper_f(): #5, #8
        return original_f() #9
    return wrapper_f #6


def dp(): #2, #10
    print("intall dp function") #11

decorated_dp = decorator_f(dp) #3
decorated_dp #7


# ex2

def decorator_f(original_f):
    def wrapper_f():
        print("{} 함수가 호출되기 전입니다.".format(original_function.__name__))
        return original_f()
    return wrapper_f

def dp_1():
    print("dp_1 함수 실행")

def dp_2():
    print("dp_2 함수 실행")

# display_1 = decorator_function(dp_1) 
# display_2 = decorator_function(dp_2) 
 
dp_1() # 변수에 함수형 리턴값 할당 없이 바로 함수 호출이 가능하다. 
dp_2() # 변수에 함수형 리턴값 할당 없이 바로 함수 호출이 가능하다. 
 


 # 인자가 전달되는 함수는 어떻게 테코레이팅 해야 할까?

def decorator_f(original_f):
    def wrapper_f(*args, **kwargs):
        print("{} 함수가 호출되기 전입니다.".format(original_f.__name__))
        return original_f(*args, **kwargs)
    return wrapper_f

