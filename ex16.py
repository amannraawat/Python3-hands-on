# import argv package from sys module
from sys import argv

# unpacking items
script, filename = argv

# simple print statements
print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRl-C (^C).")
print(f"If you want that, hit RETURN.")

# waiting for user's input 
input("?")

print("Opening the file...")
# opening the file in write mode 
target = open(filename, 'w')

print(f"Truncating the file. Goodbye!")
# truncating the file i.e. simple emptying the contents of the file
# truncate only works in write and write read mode only
target.truncate()

print(f"Now I'm going to ask you for three lines.")
# asking inputs for three lines 
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I'm going to write these to the file.")

# below lines writes into the file what user has typed down
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"And finally, we close it.")
# last closing the file
target.close()
