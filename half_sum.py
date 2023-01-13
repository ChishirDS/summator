from mainLF import LF

class HalfSum(LF):
    
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        
    def half_sum(self):
        
        obj = LF(self.a, self.b)
        P = obj.logick_and()

        firstStep = obj.logick_or()

        obj2 = LF(P)
        notP = obj2.logick_not()
        
        obj3 = LF(notP, firstStep)
        S = obj3.logick_and()
        
        return S, P
        

# f = HalfSum(0, 1)
# print(f.half_sum())
