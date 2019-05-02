def case1():
    numbers = [1, 3, 5]
    ps = 0
    while ps < len(numbers):
        number = numbers[ps]
        if number % 2 == 0:
            print("Found even num", number)
            break
        ps += 1
    else:  # break checker 반복문을 모두 실행했지만  break을 발견하지 못할 경우 처리.
        print('not found even num')


def case2():
    ns = [2, 4, 6]
    check = True
    position = 0
    while position < len(ns):
        n = ns[position]
        if n % 2:
            check = False
            print("Found even num", n)
            break
        position += 1
    if check:
        print("not found even num")


if __name__ == "__main__":
    case1()
    # case2()
