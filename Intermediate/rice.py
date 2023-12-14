from grocery import Grocery

class Rice(Grocery):

    discount  = 10 #overrides the class attribute now all rice will have discount = 10 in calculations ex in apply discount method 

    def __init__(self, name: str, price: float, eatable: bool, quantity: float, in_stock = True, rice_color = 'not defined'):
        #call super to access all attributes and methods
        super().__init__(
            name , price, eatable,  quantity, in_stock
        )
        assert rice_color=='not defined' or rice_color=='white' or rice_color=='brown'
        self.rice_color = rice_color