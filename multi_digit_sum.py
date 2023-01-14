from single_digit_sum import SingleDigitSum
from mainLF import LF


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
        
    
    def parser(self):
        list_a = list(map(lambda i: int(i), [i for i in self.a]))
        list_b = list(map(lambda i: int(i), [i for i in self.b]))
        list_a.reverse()
        list_b.reverse()
        
        return list_a, list_b
    
    
    def get_sum(self):
        
        amount_register = []
        # вызываем метод преобразовывающзий входный значения для работы
        values = self.parser()
        
        p = 0
        # перебираем числ в двух входных списках одновременно
        for digit in zip(values[0], values[1]):
            # передаем по одному в сумматор, с учетом распаковки и регистра переноса
            obj = SingleDigitSum(*digit, p)
            s, p = obj.single_digit_sum()[0], obj.single_digit_sum()[1]
            # добавляем выходные значения в регистр сдвига суммы
            amount_register.append(s)
        # забираем регистр переноса как старший разряд
        amount_register.append(p)
        # разворачиваем список
        amount_register.reverse()
        
        return amount_register


    def get_subtracting(self):     
        # вызываем метод преобразовывающзий входный значения для работы
        values = self.parser()
        
        #разворачиваем вычитаемое для корректной работы
        values[1].reverse()
        
        reverse_code = []
        # проходим в цикле по всем числам вычитаемого обрабатывая их логическим НЕ
        # получаем обратный код
        for i in values[1]:
      
            obj = LF(i)
            
            reverse_item = obj.logick_not()
            
            reverse_code.append(reverse_item)
            
        # генерируем список из нулей по длинне обратного кода -1  
        additional_code = [0 for i in range(len(reverse_code)-1)]
        #дабавляем к нему единицу и получаем единицу в двоичной системе с учетом количества бит уменьшаемого
        additional_code.append(1)
        
        # приводим все элементы списков к строковым для дальнейшей передачи в метод суммирования
        additional_code = list(map(lambda i: str(i), additional_code))
        reverse_code = list(map(lambda i: str(i), reverse_code))
        new_value0 = list(map(lambda i: str(i), values[0]))

    
        new_value0.reverse()
        
        # склеиваем уменьшаемое и вычитаемое в строки для передачи в метод суммирования
        one = ''.join(additional_code)
        two = ''.join(reverse_code)
        
        # передаем их в метод суммирования
        obj2 = MultiDigitSum(one, two)
        new_value1 = obj2.get_sum()
        # срезаем игнорируемый бит
        new_value1 = new_value1[1:len(new_value1)]
        
        new_value2 = list(map(lambda i: str(i), new_value1))
        # склеиваем двочное число с доп. кодом в строку для передачи в метод суммирования
        res_newV2 = ''.join(new_value2)
        
        #передаем
        obj3 = MultiDigitSum(new_value0, res_newV2)
        
        result = obj3.get_sum()
        
        # возвращаем результат отсекая игнорируемый бит
        return result[1:len(result)]
        
        
        
            
        


f = MultiDigitSum('101010', '101010')
print(f.get_subtracting())