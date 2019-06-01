'''
first-class citizen 

1) 변수나 데이터에 할당 할 수 있어야 한다.

2) 객체의 인자로 넘길 수 있어야 한다.

3) 객체를 리턴값으로 리턴 할 수 있어야 한다.

reference = https://whatisthenext.tistory.com/111?category=761276

'''

# 1) 함수를 변수에 할당 가능

def sqaure(x):
    return x * x

# sqaure_f = sqaure  -> square 함수를 변수에 할당.
# sqaure = sqaure(3) -> square의 리턴 값을 변수에 할당.


# 2) 함수를 함수의 인자로 전달 가능.

def sqaure(x):
    return x * x


def my_func(func, arg_list):
    re = []
    for i in arg_list:
        re.append(func(i))
    return re


num_list = [3, 5, 7]
squares = my_func(sqaure, num_list) 

#print(squares) - > [9, 25, 49]

# 만약에 함수를 인자로 전달을 못한다면 중복 코드가 발생.

def sqaure(arg_list):
    re = []
    for i in arg_list:
        re.append(i * i)
    return re

def cub(arg_list):
    re = []
    for i in arg_list:
        re.append(i * i * i)
    return re

# 3) 함수 리턴 가능
# #num -> 인터프리터의 해석 순서.

def log(msg): # 1 , #3
    def log_message(): #4, #10
        print('Log : ', msg) #11
    return log_message #5

log_hi = log("Hello") #2, #6
print(log_hi) #6, #7
log_hi #9
