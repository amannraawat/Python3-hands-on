# argv is used when we have to pass arguments during calling of the program. First argument is name of the program itself
from sys import argv
# read the WYSS section for how to run this
# below we are just unpacking values which are being passed while running the program
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
