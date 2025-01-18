types_of_people = 10
# 10 was assigned to types_of_people so it will print that
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# below we are just adding values of binary and do_not varibale
y = f"Those who know {binary} and those who {do_not}."

# x and y will print what was assigned to it earlier
print(x)
print(y)

# simple it will first print string and then value of x varibale
print(f"I said: {x}")
# first print string and then in single quotes print value of y variable
print(f"I also said: '{y}'")

hilarious = False
# we have to leave a empty space with curly brackets to make use of format() formatting
joke_evaluation = "Isn't that joke so funny?! {}"
# in empty space we are assigning hilarious variable value
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# in python we can concatenate or join strings using the plus(+) opeartor
print(w + e)
