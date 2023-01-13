from mainLF import LF
from half_sum import HalfSum

class SingleDigitSum(HalfSum):
    def __init__(self, a: int, b: int, p=0) -> None:
        self.a = a
        self.b = b
        self.p = p
        
    def single_digit_sum(self):
        
        hs1_obj = HalfSum(self.b, self.p)
        firs_step = hs1_obj.half_sum()
        
        hs2_obj = HalfSum(self.a, firs_step[0])
        second_step = hs2_obj.half_sum()  
        
        hs3_obj = LF(second_step[1], firs_step[1])
        third_step = hs3_obj.logick_or()
        
        #print(f'first half sum {firs_step} .  sesond half sum {second_step}. logick or = P {third_step}')
        return second_step[0], third_step
        
        
        
# f = SingleDigitSum(1,0,0)
# print(f.single_digit_sum())