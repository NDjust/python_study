import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == "__main__":
    demo(bisect_fn)
    print([grade(score) for score in [33, 22, 100, 82, 72, 65]])