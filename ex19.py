# below lines of code is a function syntax in python
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} crackers.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")


# this way of passing arguments by straight away passing numbers    
print("We can just give the function numbers directly.")
cheese_and_crackers(20,30)

# this way of passing arguments by making varibales and then passing variables to function calling
print("OR, we can use variables from our script:")
amount_of_cheeese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheeese, amount_of_crackers)

# this way of passing arguments by applying math
print("we can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

# or we can use this way by combining both varibales and math
print("And we can combine the two, variables and math.")
cheese_and_crackers(amount_of_cheeese+100, amount_of_crackers+1000)
