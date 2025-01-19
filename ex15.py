# we are importing argv package from sys module
# argv is a list that contains all command line argumnets passed to the script
from sys import argv

# unpacking argumnets passed while running the file
script, filename = argv

# open function opens the specific file
txt = open(filename)

# simple print statement 
print(f"Here's your file {filename}:")
# read function reads the contents of the file
print(txt.read())

print("Type the filename again:")
# Again we are waiting for the user input
file_again = input("> ")

# again opening the specific file
txt_again = open(file_again)

# first reading content of file and then printing
print(txt_again.read())
