name = 'Aman Rawat'
age = 21
height = 65 # inches
weight = 143 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

inches = 74
inches_to_centimeters = inches * 2.54
print(f"{inches} inches when converted to centimeters, it gives {inches_to_centimeters} centimeters.")

pounds = 65
pounds_to_kgs = pounds / 2.20462262
print(f"{pounds} pounds when converted to kilograms it gives {pounds_to_kgs} kilograms.")
