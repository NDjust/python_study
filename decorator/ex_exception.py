from functools import wraps

def handler():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AssertionError as e:
                return e
            except ZeroDivisionError as e:
                return e
            except SyntaxError as e:
                return e
        return wrapper
    return decorator


@handler()
def _eval(s):
    return eval(s)


print(_eval('102 + 2/0'))