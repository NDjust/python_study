'''
by using property and setter class member value encapsulation.

'''
class calculator():
    max_digits = 20
    def __init__(self, battery, cur_result, digit_system):
        self._battery = battery
        self._cur_result = cur_result
        self._prev_result = []
        self._prev_calc = None
        self._digit_system = digit_system
    
    def add(self, value):
        self._prev_result += [self._cur_result]
        self._cur_result += value
        self._prev_calc = "add"

    def sub(self, value):
        self._prev_result += [self._cur_result]
        self._cur_result -= value
        self._prev_calc = "sub"

    @property 
    def cur_result(self): # prevent direct access to class member value
        return self._cur_result

    @cur_result.setter # cur_result value can change 
    def cur_result(self, value):
        self._cur_result = value


if __name__ == "__main__":
    c1 = calculator(100, 0, 10)
    c1.add(3)
    c1.sub(2)
    print(c1.cur_result)
    c1.cur_result = 3 # can change memeber value like variable.
    print(c1.cur_result)
