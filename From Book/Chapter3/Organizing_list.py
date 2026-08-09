#sorting a list
cars = ['BMW', 'AUDI', 'MERCEDES', 'BUGATTI']
cars.sort()
print(f"\n{cars}")

#reverse sorting a list
cars = ['BMW', 'AUDI', 'MERCEDES', 'BUGATTI']
cars.sort(reverse = True)
print(f"\n{cars}")

#Temporarily sorting a list
cars = ['BMW', 'AUDI', 'MERCEDES', 'BUGATTI']

message_1 = "Heres the original list : "
print(f"\n{message_1}")
print(cars)

message_2 = "Heres the sorted list :  "
print(f"\n{message_2}")
print(sorted(cars))

message_3 = "Heres the reverse sorted list :  "
print(f"\n{message_3}") 
print(sorted(cars, reverse=True))

print(f"\n{message_1}")
print(cars)

#reversing a list 
cars = ['BMW', 'AUDI', 'MERCEDES', 'BUGATTI']
cars.reverse()
print(f"\n{cars}")

#getting the length of a  list
cars = ['BMW', 'AUDI', 'MERCEDES', 'BUGATTI']
length = len(cars)
print(f"The length of the list is: {length}")



