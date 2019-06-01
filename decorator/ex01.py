from functools import wraps


def document_it(func):
    @wraps(func)
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print('Positional arguments:', args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return new_function


def square_it(func):
    @wraps(func)
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


def without_wraps_square(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


@square_it
@document_it
def add_ints(a, b):
    '''두수의 합을 리턴'''
    return a + b


@without_wraps_square
def sub_ints(a, b):
    '''두수의 차를 리턴'''
    return a - b


if __name__ == "__main__":
    print(add_ints(1, 2))
    '''
    출력 
    Running function: add_ints
    Positional arguments: (1, 2)
    Keyword arguments: {}
    Result: 3
    3
    '''
    print(add_ints.__name__)  # use wraps
    # 출력 add_ints
    print(add_ints.__doc__)
    # 출력 두수의 합을 리턴
    print(sub_ints.__name__)  # not use wraps
    # 출력 new_function
    print(sub_ints.__doc__)
    # 출력 None
