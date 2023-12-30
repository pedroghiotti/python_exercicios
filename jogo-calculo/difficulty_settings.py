from random import choice
from operations import (
    add, 
    subtract, 
    multiply, 
    divide
)

class DifficultySetting:
    def __init__(self, operations, domain):
        self.__operations = operations
        self.__domain = domain
    
    def get_question(self):

        a = choice(self.__domain)
        b = choice(self.__domain)
        
        op = choice(self.__operations)
        
        if(op is divide):
            b = choice(self.__domain[1:])

        return (f'{a} {op.get_sign()} {b} = ', op.process(a, b))


difficulty_settings = {
    '1': DifficultySetting((add, subtract), range(1, 11)),
    '2': DifficultySetting((add, subtract, multiply, divide), range(11)),
    '3': DifficultySetting((add, subtract, multiply, divide), range(101))
}
