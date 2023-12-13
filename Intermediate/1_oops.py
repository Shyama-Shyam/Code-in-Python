class Grocery:

    #class attributes same for all the objects unless intialized in instance
    discount = 20
    items = [] #To storce all the object instances of the class

    #constructor method called everytime we create instance , used to intialize instance attributes (defined for each object)
    def __init__(self, name: str, price: float, eatable: bool, quantity: float, in_stock = True):

        #check the formats of attributes
        assert price>=0 and quantity>=0, f"arguments should be grater than 0"
        assert type(eatable)== bool

        #instance attributes
        self.quantity = quantity
        self.name = name
        self.price = price
        self.eatable = eatable
        self.in_stock = in_stock

        #actions
        Grocery.items.append(self)
    
    @classmethod #class method to change class instance take class as argument
    def instantiate_from_csv(cls , path):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            obj = Grocery(
                name = str(item.get('name'))[1:-1],
                price = float(item.get('price')),
                eatable = bool(item.get('eatable')),
                quantity = float(item.get('quantity')),
                in_stock = bool(item.get('in_stock'))
            )
            Grocery.items.append(obj)

    @staticmethod #do something that is not unique per instance , Typically used for utility functions that do not depend on class or instance state.
    def is_integer(num):
        if isinstance(num , int):
            return True
        else:
            return False

    #instance method to modify instance attributes
    def apply_discount(self):
        self.price =  round(self.price*(1-(self.discount/100)),2)

    #magic method that will reperesent the objects in console with (strings)(just like code of creating instance)  
    #instad of like <__main__.Grocery object at 0x00000215AC8C8350>
    def __repr__(self) -> str: 
        return f"Grocery('{self.name}', {self.price}, {self.eatable}, {self.quantity})"
        
#create object instances from the database (csv) using class method
import csv
Grocery.instantiate_from_csv("F:\shreeradha\Code-in-Python\Intermediate\items.csv")

#create instance of the class
itm1 = Grocery('chips', 20.5, True, 0, False)
itm2 = Grocery('biscuit', 300, True , 10 )

#print(Grocery.items) #all the instances till now

print(type(itm1).__name__) #name of the class

#print(Grocery.__dict__) #all methods and class attributes

print(itm1.__dict__) #all the attributes of the object as dictionary

print(Grocery.is_integer(4.0)) #static method


# INHERITANCE

