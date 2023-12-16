# context managers
'''
object that is used to manage resources, such as opening and closing files, 
acquiring and releasing locks, and more. Context managers are typically employed with 
the with statement, providing a convenient and clean way to handle resource management.
'''
# Using a file as a context manager
with open('Intermediate//readfile.txt', 'r') as file:
    content = file.read()
    # Do something with the file content

# File is automatically closed when the 'with' block is exited
    
    
class MyContextManager:
    def __init__(self, path , mode):
        self.path = path
        self.mode = mode
        self.file = None

    def read(self):
        if self.file is None:
            raise ValueError("File not open. Use inside a 'with' statement.")
        return self.file.read()
  

    def __enter__(self):
        print("Entering the context")
        self.file = open(self.path, self.mode)
        return self
        # This value is assigned to the variable after 'as' in the 'with' statement

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print("Exiting the context")
        # Perform cleanup or handle exceptions if needed

# Using the custom context manager
with MyContextManager('Intermediate//readfile.txt', 'r') as cm:
    # Do something within the context
    print("Inside the context")
    content = cm.read()
    print("File content:", content)

# Exiting the context automatically, even if an exception occurs
# The with statement is used to create a context managed block. The __enter__ method is called at the beginning,
#and the __exit__ method is called at the end, ensuring proper resource management.
