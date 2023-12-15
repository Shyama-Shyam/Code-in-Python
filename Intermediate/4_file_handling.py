# f = open(filename, mode)
'''
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
'''
path = 'Intermediate\\readfile.txt'

file = open(path, 'r') # or can use, with open(path, 'r') as file:

#1 print each line
for each in file:
    print (each)

file.seek(0) #move pointer to the start
#read all the file at once
print (file.read())
file.close()

#store evrey line in a list
with open(path, 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

with open('Intermediate\\writefile.txt', "w") as f: 
    f.write("hello hello")

