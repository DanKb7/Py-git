#Пример для 232гр 
class Add:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 

    def Result(self): #сложение в ООП
        return self.a + self.b 
    
class Ret(Add):# Умножение в ООП
    def Prioriti(self):
        return self.a * self.b

a = Add(int(input("Введи переменную А: ")),int(input("Введи переменную А: ")))
print("Ваш результат = ", a.Result())
b = Ret(int(input("Введи переменную Б: ")),int(input("Введи переменную Б: ")))
print("Ваш результат = ", b.Prioriti())

# blet
# blet