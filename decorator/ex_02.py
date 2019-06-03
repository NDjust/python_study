# 정상수행시 : try -> else -> finally
# 에러발생시 : try -> except -> finally

from functools import wraps

# use closure
def handler():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
                # 리턴은 함수 실행시 한번만 되니 try에서 return되면 아래가 무시.
                # 하지만 finally 는 함수 호출시 생성 되어지니 func가 실행이 되어도 출력이 된다?
            except ZeroDivisionError as e:
                return e
            except SyntaxError as e:
                return e
            except ValueError as e:
                return e
            else:
                return 'no error'
            finally:
                return 'end'
            # return, exit()등과 같이 프로그램이나 함수가 종료되기 전에 finally는 항상 실행된다.
        return wrapper
    return decorator

class Calculator:
    
    def __init__(self):
        self._current = 0

    def add(self, value):
        self._current += value
    
    def sub(self, value):
        self._current -= value

    def mul(self, value):
        self._current *= value
    
    @handler()
    def div(self, value):
        self._current /= value
        return self._current

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, new_value):
        self._current = new_value
        
#simple try exception




if __name__  == "__main__":
    c1 = Calculator()
    c1.add(10)
    print(c1.current)
    print(c1.div(2))
    print(c1.current)