

#Проверка корректности значений
def check_values(*args: int) -> bool:
    
    values =  [0, 1]
    
    for value in args:
        if value not in values:
            print('value error')
            return False
        else:
            return True


#Логическое И
def logick_and(a: int, b: int) -> int:
    if check_values(a, b):
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
        
#Логическое ИЛИ
def logick_or(a: int, b: int) -> int:
    if check_values(a, b):
        if (a == 0) and (b == 0):
            return 0
        else: 
            return 1


#Логическое НЕ
def logick_not(a: int) -> int:
    if check_values(a):
        return 1 if a == 0 else 0
