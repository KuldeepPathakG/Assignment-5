class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self,num1,num2):
        add1=num2+num1
        return add1
    def subtract(self,num1,num2):
        sub1=num2-num1
        return sub1
    def multiply(self,num1,num2):
        mul1=num2*num1
        return mul1
    def divide(self,num1,num2):
        div1=num2/num1
        return div1
    
obj1=Calculator(10,94)
print(obj1.add(10,94))
print(obj1.subtract(10,94))
print(obj1.multiply(10,94))
print(obj1.divide(10,94))