def ex4_1():
    guess_me = 7
    if guess_me > 7:
        print("too high")
    elif guess_me == 7:
        print("just right")
    else:
        print("too low")


def ex4_2():
    guess_me = 7
    start = 8

    while True:
        if guess_me > start:
            print("too row")
        elif guess_me == start:
            print("fount it")
            break
        else:
            print("oops")
            break
        start += 1


def ex4_3():
    for i in [3, 2, 1, 0]:
        print(i)


def ex4_4():
    print([i for i in range(10) if i % 2 == 0 and i > 0])


def ex4_5():
    square = {i: i * i for i in range(10)}
    print(square)


def ex4_6():
    set_com = {i for i in range(10) if i > 0 and i % 2 != 0}
    print(set_com)


def ex4_7():
    for i in (i for i in range(10)):
        print("Got {}".format(i))


def ex4_8():
    def good():
        return ["Harry", "Ron", "Hermione"]

    return good


def ex4_9():
    def get_odds():
        for i in range(1, 10):
            if i % 2 != 0:
                yield i

    for count, x in enumerate(get_odds(), 1):
        if count == 3:
            print(x)


def ex4_10():
    def test(func):
        def new_func(*args, **kwargs):
            print("start")
            result = func(*args, **kwargs)
            print("end")
            return result

        return new_func

    @test
    def add(a, b):
        print(a + b)

    add(1, 2)


def ex4_11():
    class OopsException(Exception):
        pass

    try:
        raise OopsException('oops')
    except OopsException as e:
        print("Caught an", e)


def ex4_12():
    titles = ["Creature of Habit", "Crewel Fate"]
    plots = ["A nun turns into a mon ster", "A haunted yarn shop"]
    movies = dict(zip(titles, plots))
    # movie = {}
    # for k, v in zip(titles, plots):
    #     movie[k] = v
    print(movies)


ex4_12()
