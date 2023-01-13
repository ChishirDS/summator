class LF:
    
    values =  [0, 1]

    def check_values(self, *args: int) -> bool:   
        
        for value in args:
            if value not in self.values:
                print('value error')
                return False
            else:
                return True
    
    
    def __init__(self, a: int, b=0) -> None:
        
        try:
            if self.check_values(a, b):
                self.a = a
                self.b = b
            else:
                print('Некорректно указаны значения')
        except:
            print('Значения должны быть либо 1 либо 0')
    
    
    def logick_and(self) -> int:
        
        if self.a == 1 and self.b == 1:
            return 1
        else:
            return 0
            
            
    def logick_or(self) -> int:
        
        if (self.a == 0) and (self.b == 0):
            return 0
        else: 
            return 1
    
    
    def logick_not(self) -> int:
        return 1 if self.a == 0 else 0




# f = LF(1, 1)
# print('Логическое И:')
# print(f.logick_and())
# print('\n\n\nЛогическое ИЛИ:')
# print(f.logick_or())

# f1 = LF(1)
# print('\n\n\nЛогическоеЛогическое НЕ:')
# print(f1.logick_not())