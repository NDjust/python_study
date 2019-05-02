def write(books):
    def reading(book):
        return f"i am reading {book}"

    return reading(books)


def write1(books):
    '''closure'''

    def reading():
        return f"i am reading {books}"

    return reading


if __name__ == "__main__":
    a = write1("when")  # <function write1.<locals>.reading at 0x000001BEFC489AE8>
    b = write1("how")  # <function write1.<locals>.reading at 0x000001BEFC489AE8>
    print(a())  # i am reading when
    print(b())  # i am reading how
