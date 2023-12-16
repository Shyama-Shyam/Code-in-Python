x  = [1,2,3]
print(type(x))
# <class 'list'> x is object of class list but still we can use the syntax x[1] how do we make these syntaxes
print(x[1]) #2

#made possible by dunders/magicmethods / Data Model methods

class dog:
    def __init__(self, x):
        self.x = x
    def __repr__(self): #this magic method gives a str representation when we print the object
        return f"{self.x}"
    def __mul__(self,other):
        if type(other) is not int:
            raise Exception('argument should be int')
        else:
            return self.x * other
    def __call__(self, n):
        print(f"we get a number {n}")
    
d = dog('grok')
print(d) #reper method
print(d*4)  #mul method
d(6)