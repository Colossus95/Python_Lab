#Using the range() Function
for value in range ( 1, 6 ):
    print(value)   # prints the given range numbers

print("\n")
for value in range ( 6 ):
    print(value)   # prints from the 0  

# using range function inside list function
print("\n")
numbers = list(range(1, 5))
print(numbers)

print("\n")
o_numbers = list(range(1, 10, 2))  #here the last digit indicates the number gap
print(f"The odd numbers are : {o_numbers}")

e_numbers = list(range(2, 11, 2))  #here the last digit indicates the number gap
print(f"The even numbers are : {e_numbers}")

#some in built functions
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
choto = min(digits)
boro = max(digits)
total = sum(digits)
print(f"\nEi list er moddhe choto hoilo {choto}, boro hoilo {boro}, r total hoilo {total}")

#beginner loop
n_numbers = []
for values in range(1, 11):
    n_numbers.append(values**2)
print(f"\n{n_numbers}")

#pro loop 
square = [maan**2 for maan in range(1, 11)]
print(square)


