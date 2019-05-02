short_list = [1, 2, 3]

while True:
    value = input('position [q to quit]? ')
    if value == 'q':
        break

    try:
        position = int(value)
        print(short_list[position])
    except IndexError as e:
        print('Bad index: ', position)
    except Exception as e:
        print('Something else broke: ', e)


# class UppercaseException(Exception):
#     print("have upper case")
#
#
# words = ['eenie', 'meenie', "MO"]
# for w in words:
#     if w.isupper():
#         raise UppercaseException(w)


class OopsException(Exception):
    pass


try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
