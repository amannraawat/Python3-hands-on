cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# cars is assigned value 100 so it prints "There are 100 cars available."
print("There are", cars, "cars available.")

# drivers is assigned number 30
print("There are only", drivers, "drivers available.")

# cars_not_driven is assigned the sustraction of variable cars and varibale drivers
print("There will be", cars_not_driven, "empty cars today.")

# carpool_capacity is cars_driven multiplied by space_in_a_car
print("We can transport", carpool_capacity, "people today.")

# passengers is assigned to 90 so it will print "We have 90 to carpool today."
print("We have", passengers, "to carpool today.")

# average_passengers_per_car is passengers divided by cars_driven
print("We need to put about", average_passengers_per_car,"in each car.")
