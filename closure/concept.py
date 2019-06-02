-'''
clousure 는 일반 함수와 다르게, 
자신의 영역 밖에서 호출된 함수의 변수값과 
레퍼런스를 복사, 저장, 접근을 가능하게 한다.

closure에서 내부 함수는
루프나 코드 중복을 피하기 위해 또 다른 함수 내에 
어떤 복잡한 작업을 한 번 이상 수행할 때 유용하게 사용한다.

Closure 쓰는 이유
-> 기존에 만들어진 함수나 모듈 등을 수정하지 않고 wrapper 
함수를 이용해서 자기 입맛에 맞게 조정할 수 있다는 것이다.

'''

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

print(outer_function(3, 5))


def say_words(msg):
    def say_sentence():
        return "안녕? 이걸 출력해줘! : {}".format(msg)
    return say_sentence
 
a = say_words("출출하다")
print("a는 무엇일까? : ", a)
print("a의 타입은 무엇일까? : ", type(a))
print("a가 함수라는 걸 알았다. 괄호를 붙여보자. ====> ", a())

''' 
출력결과
a는 무엇일까? :  <function say_words.<locals>.say_sentence at 0x7fc2c039c0d0>
a의 타입은 무엇일까? :  <class 'function'>
a가 함수라는 걸 알았다. 괄호를 붙여보자. ====>  안녕? 이걸 출력해줘! : 출출하다

-> closure는 다른 함수에 의해 동적으로 생성되고, 
바깥 함수로부터 생성된 변수값을 알고 있는 변수이다.

'''
