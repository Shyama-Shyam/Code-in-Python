import csv

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
        self.__name = name #adding 2 underscores make it private attribute , can not print obj.__name
        self.price = price
        self.eatable = eatable
        self.in_stock = in_stock

        #actions
        Grocery.items.append(self)

    @property #read only attribute
    def name(self):
        return self.__name
    
    @name.setter #name is property function that we want to set a new value , us setter
    def name(self, value):
        if len(value)<10:
            self.__name = value
        else:
            print('that name is too long')
    
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.eatable}, {self.quantity})"
    
    #method to show abstraction
    def send_mail(self):
        self.__connect_server()
        self.__write()
        self.__send()
    
    #private method for abstraction user cannot do obj.__send()
    def __connect_server(self):
        pass
    def __write(self):
        pass
    def __send(self):
        pass
