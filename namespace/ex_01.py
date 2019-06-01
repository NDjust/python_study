dog_name = 'Shiva'


def change_dog():
    '''this dog_name is change_dog func local variable'''
    dog_name = "poodle"
    return dog_name


def global_dog():
    '''call global variable dog_name'''
    global dog_name
    # dog_name = "poodle"
    return dog_name


def global_change_dog():
    '''call global variable dog_name and change variable value'''
    global dog_name
    dog_name = "poodle"
    return dog_name


if __name__ == "__main__":
    print(dog_name is change_dog())  # global, local
    print(id(dog_name), id(change_dog()))  # global, local
    print(dog_name is global_dog())  # global, global
    print(id(dog_name), id(global_dog()))  # global, global
    print(dog_name is global_change_dog())  # global, global change value
