def print_args(*args):
    print("positional argument tuple:", *args)


print_args(1, 2, 3, 4)

print("nathan".capitalize())

generator = (i for i in range(10)) # 대기 상태.


def x():
    return 10


def y():
    yield 10 # 대기 상태
print(x())
print(y().__next__())