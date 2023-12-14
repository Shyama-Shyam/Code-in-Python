from grocery import Grocery
from rice import Rice


itm1 = Grocery('chips', 20.5, True, 0, False)
itm2 = Grocery('biscuit', 300, True , 10 )

print(itm1.name) 
#.name is property read only attribute without setter method , __name will not work (private attribute)
#after setter method we can udate the name

itm1.name = 'CHIPS'
print(itm1.name)


#ENCAPSULATION : Restrict the direct to some of our attributes by getters and setters

#ABSTRACTION : hide unnecessary details from users who are ctraing objects 
#as user we want to send email , we send_mail mathod
# but we also have connect server method , send , write method which are not used directly by user
#so we want to hide them from the user
itm1.send_mail()
try:
    itm1.__send() #private method
except:
    print('private method')

#INHERITANCE: allows to reuse code through out classes , child class
itm3 = Rice('rice white', 30, True, 5, True, 'white')
itm3.send_mail()

#POLYMORPHISM : (many forms , different scenarios diffrent results from the same function)
# example : len() function handles both list and str
inp = 'shyam' #str
print(len(inp))
inp = ['shyama', 'shyam'] #list
print(len(inp))

#rice child class have disc = 10 , someother child class let say wheat might have disc = 30 so 
#our apply_disount can  handle both rice and wheat (different type of obbject) and produce different result using 
#overrided discount class attribute 