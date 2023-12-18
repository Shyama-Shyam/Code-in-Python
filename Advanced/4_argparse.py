"""
Argument parsing in Python refers to the process of extracting values from 
command-line arguments provided when a Python script is executed. It allows 
scripts or programs to accept input or configuration from users running the 
script in a command-line environment. The argparse module is commonly used for argument parsing in Python.
"""
from argparse import ArgumentParser
parser = ArgumentParser(description = 'transfer the money between two person')
#parameters : 
'''
name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
action - The basic type of action to be taken when this argument is encountered at the command line.
nargs - The number of command-line arguments that should be consumed.
const - A constant value required by some action and nargs selections.
default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.
type - The type to which the command-line argument should be converted.
choices - A sequence of the allowable values for the argument.
required - Whether or not the command-line option may be omitted (optionals only).
help - A brief description of what the argument does.
metavar - A name for the argument in usage messages.
dest - The name of the attribute to be added to the object returned by parse_args().
'''

#positional args : without a flag or dash are identified on position , written in specific order, cant have default val
#optional args : flags or options, specified with flags such as --input or -i. not tied to a specific position . can have default values

parser.add_argument('sender', help ='name of sender' , type = str )
parser.add_argument('reciever', help ='name of reciever' , type = str  )
parser.add_argument('amount' , help = 'amount to be transferred', type = int )
parser.add_argument('--type','-t' , help = 'time to transfer' ,choices = ['now','2','3'], default= 'now' )
parser.add_argument('--schedule','-s', help = 'list of schedule for transferring the money in parts',type = int, nargs='+', default=[])
parser.add_argument('--reciept','-r', action='store_const', const=True, default=False, help='email the reciept or not')

args = parser.parse_args()

amount = args.amount
schedule = args.schedule
sender  = args.sender
reciever = args.reciever
Type = args.type
reciept = args.reciept


def check_schedule_sum(schedule, amount):
    if schedule ==[]:
        return
    else:
        if sum(schedule) != amount:
            raise Exception("The sum of schedule amounts must be equal to the specified amount.")

def print_message():
    print(f"{amount} will be transferred from {sender} to {reciever}" ,end = ' ')
    if Type == 'now':
        print(f"toady", end = ' ')
    else:
        print(f"under {Type} days", end = ' ')
    if len(schedule)!=0:
        print(f"\nThe money will be transferred in deposits as {schedule}", end = ' ')
    if reciept==True:
        print(f"the reciept will be mailed")
check_schedule_sum(schedule, amount)
print_message()

#commands to run in terminal 
#1/go to Code-in-Python\Advanced
#  python 4_argparse.py -h
#python 4_argparse.py shyama shyam 500 --type 2 --schedule 250 100 150 --reciept
