from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}.")

# in_file = open(from_file)
# data = in_file.read()

data = open(from_file).read()

print(f"The input file is {len(data)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(data)

print(f"Alright, all done.")

out_file.close()
# in_file.close()
