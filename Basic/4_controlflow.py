# if elif else
x = 10

#1
if x>10 :
    pass

#2
if x>10:
    pass
else:
    pass

#3
if x>10:
    pass
elif x>5:
    pass
else:
    pass

print('loops')
#FOR LOOP

#syntax
iterable = [1,2,3,4]  #can be list , dict, set , tuple
for var in iterable:
    pass

for i in range(8,16,2): #start default = 0 , stop not included , step  default 1
    print(i)


fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green","black"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)

for i in range(10):   
    if i == 3:
        continue
    if i== 7:
        break
    print(i)

count = 0
while (count < 5): 
    count += 1; print("Hello")

i=0
while True:
    print('still in loop')
    i+=1
    if i==5:
        break

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)

# python code to demonstrate working of items()

king = {'Ashoka': 'The Great', 'Chandragupta': 'The Maurya',
		'Modi': 'The Changer'}

# using items to print the dictionary key-value pair
for key, value in king.items():
	print(key, value)


