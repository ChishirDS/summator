from single_digit_sum import SingleDigitSum


class MultiDigitSum(SingleDigitSum):
    
    values = '01'
    
    def validate(self, a: str, b: str) -> bool:
  
        for i in a:
            if i not in self.values:
                return False

        for i in b:
            if i not in self.values:
                return False
        
        if len(a) != len(b):
            return False
        
        return True
        
    
    def __init__(self, a: str, b: str) -> None:
        
        if  self.validate(a, b):
            self.a = a
            self.b = b
        else:
            raise ValueError('The value must be written in binary notation in string representation. Only 0 and 1 are allowed')
        
    
    def parsing(self):
        
        amount_register = []
        list_a = list(map(lambda i: int(i), [i for i in self.a]))
        list_b = list(map(lambda i: int(i), [i for i in self.b]))
        list_a.reverse()
        list_b.reverse()
        p = 0
        
        for digit in zip(list_a, list_b):
            
            obj = SingleDigitSum(*digit, p)
            s, p = obj.single_digit_sum()[0], obj.single_digit_sum()[1]
            amount_register.append(s)
            
        amount_register.append(p)
        amount_register.reverse()
        
        return amount_register

