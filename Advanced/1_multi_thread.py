'''
Thread:
What is a Thread? A thread is the smallest unit of execution within a process.
What Does it Do? Threads enable concurrent execution of different parts of a program. 
Multiple threads within a process share the same resources, such as memory space.
Example: Think of threads like workers in a restaurant kitchen. Each worker (thread) performs a
 specific task, and multiple workers can work together to complete different aspects of the meal preparation simultaneously.

Multiprocessing:
What is Multiprocessing? Multiprocessing involves running multiple processes concurrently, where each process has its own memory space.
What Does it Do? Multiprocessing is about executing multiple independent programs or tasks simultaneously.
Example: Imagine multiple independent programs running on your computer at the same time. Each program is a 
separate process with its own resources.

Parallelism:
What is Parallelism? Parallelism is the simultaneous execution of multiple tasks or processes.
What Does it Do? It's about doing many things at once. In the context of computing, this often refers 
to the simultaneous execution of tasks on multiple CPU cores.
Example: Picture a factory with multiple assembly lines. Each assembly line is working independently, 
contributing to the overall production, similar to how multiple CPU cores can work on different tasks at the same time.

Concurrency:
What is Concurrency? Concurrency is the ability of a system to handle multiple tasks or processes 
at the same time, regardless of whether they are truly executing simultaneously.
What Does it Do? It's about making progress on multiple tasks in overlapping time periods.
Example: Consider a chef cooking a meal. While waiting for water to boil, the chef can chop vegetables. 
It's not true simultaneous execution (boiling water and chopping vegetables at the exact same time), 
but tasks overlap to make efficient use of time.

In summary:

Thread: Smallest unit of execution within a process.
Multiprocessing: Running multiple independent processes concurrently.
Parallelism: Simultaneous execution of tasks, often on multiple CPU cores.
Concurrency: Handling multiple tasks or processes at the same time, whether truly simultaneous or overlapping.
'''

import threading
import time

def func(x):
    print('1 this is from created thread, now this thread is going to sleep for 1sec so the original thread run (command after x.start() ) and print the active threads')
    time.sleep(1)
    print('3 from create thread exiting crreated thread , now 2 sec sleep of og thread will get over and print active thread as 1')
#creating a thread object
x = threading.Thread(target = func, args = (8,)) #x stores the thread , func witthout paranthesis , args is argto func with tuple format

x.start() #start the thread

print('active threads',threading.active_count(),'now this original thread will sleep for 2 sec ,in that time created threads sleep wil get over ') # number of currently running threadas
x.join() #this stop the og thread until thread x finishes
print('active threads',threading.active_count())

#order of the output of the above function  is
'''
1
active threads 2
3
active threads 1
'''


# LOCKING OF THREADS TO MAKE SURE THE SHARED RESOURCE IS NOT PROCESSED BY MULTIPLE THREADS AT SAME TIME
p = 16

lock = threading.Lock()
# whenver wants to acces the resource first lock the rersource
def double():
    global p, lock
    lock.acquire()
    while p <=32:
        p*=2
        print(p)
        time.sleep(0.1)
    lock.release()


def half():
    global p, lock
    lock.acquire()
    while p>=1:
        p/=2
        print(p)
        time.sleep(0.1)
    lock.release()

t1 = threading.Thread(target = half)
t2 = threading.Thread(target = double)

t1.start()
t2.start()    
t1.join()
t2.join()

#EVENT

event = threading.Event()
def func():
    print('wait for event trigger \n')
    event.wait()
    print('peforing some action')

t1 = threading.Thread(target = func)
t1.start()

x = input("want to start the thread y/n \n")
if x=='y':
    event.set()
else:
    event.clear()
t1.join()
#daemon threads : a thread that will terminate automatically when the scripts end 
#ex: reading input from a file 

path = 'Code-in-Python//Intermediate//readfile.txt'
text = ""

def read():
    global text
    with open(path, 'r') as file:
        while True:
            text = file.read()
            file.seek(0)
def print_text():
    for _ in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target = read, daemon = True)
t2= threading.Thread(target = print_text)

t1.start()
t2.start()
