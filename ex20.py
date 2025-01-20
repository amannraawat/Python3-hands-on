from sys import argv

# unpacking passed arguments when running the file
script, input_file = argv

# function for reading and printing the file
def print_all(f):
    print(f.read())

# function to take file as argument and then using seek() function.
# seek(0) function take control to the beginning of the file 
def rewind(f):
    f.seek(0)

# function for taking current line as argument and then reading current line's content
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
# open function to open a file specified
current_file = open(input_file)

print("First let's print the whole file:\n")

# calling print_all function 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
 
# calling rewind function
rewind(current_file)

print("Let's print three lines.")

# calling print_a_line function by specifying current_line variable as argument
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
