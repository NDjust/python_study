def getmin(a, b, c):
    if a <= b and a <= c:
        print(a)
    elif b <= a and b <= c:
        print(b)
    else:
        print(c)


def filtername(name):
    if len(name) > 3:
        return name[:3]
    elif len(name) < 3:
        return name + " " * (3 - len(name))
    return name


def filternames(names):
    re = []
    for n in names:
        if len(n) != 3:
            re += [filtername(n)]
    return re
ret = filtername('홍')
ns = ["다리우스", "하니", "홍나단", "홍"]
print(filternames(ns))


def printsort2(x):
    for i in range(len(x) - 1):
        for j in range(1 + i, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    for a in x:
        print(a, end=" ")


x = [3, 1, 2, 10, 6]

printsort2(x)

def print_hell(inp):
    if "안녕" in inp:
        print("Hello")


inp = input('입력: ')
print_hell(inp)