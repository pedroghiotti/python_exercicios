class Operation:
    def __init__(self, sign, func):
        self.__sign = sign
        self.__func = func

    def get_sign(self):
        return self.__sign
    
    def process(self, *args):
        return self.__func(*args)


add = Operation('+', lambda a, b: a+b)

subtract = Operation('-', lambda a, b: a-b)

multiply = Operation('*', lambda a, b: a*b)

divide = Operation('/', lambda a, b: a/b)