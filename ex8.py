formatter = "{} {} {} {}"

# simple it is assigning 1,2,3,4 to four empty spaces
print(formatter.format(1, 2, 3, 4))

# and it is assigning 4 stings to that formatter variable
print(formatter.format("one", "two", "three", "four"))

# it is giving true, false values
print(formatter.format(True, False, False, True))

# it is assigning formatter to formatter variable only
# so in one empty space there will be 4 space so for 4 empty space equals 4*4 16 empty spaces
print(formatter.format(formatter, formatter, formatter, formatter))

# it is assigning string values to formatter variable
print(formatter.format(
"Hello everyone",
" my name is Aman",
"and I am from planet 'Earth'",
"and I don't fear anyone."
))
