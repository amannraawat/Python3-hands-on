# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
    
#     i = i + 1
#     print("Numbers now: ", numbers)
    
#     print(f"At the bottom i is {i}")


# print("The numbers: ")

# for num in numbers:
#     print(num)
  


def func_like_above(num):
    numbers = []
    i=0
    
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i += 1
        print("Numbers now: ", numbers)
        
        print(f"At the bottom i is {i}")
        
    for num in numbers:
        print(num)


inp = int(input("Enter the number: "))  
func_like_above(inp)
