#Changing, Adding, and Removing Elements

#modifying elements in a list
print("\nModifying Elements in a List")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"\n{motors}")

motors[0] = 'Harley-Davidson'
print(f"{motors}")   

#Appending Elements to the End of a List using the append() Method
#adds an element to the end of the list
print("\nAppending Elements to the End of a List")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"\n{motors}")

motors.append('Ducati')
print(f"{motors}")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(f"{motorcycles}")

#Inserting Elements into a List using the insert(index number, 'name') Method
#adds an element at a specific position in the list
print("\nInserting Elements into a List")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"\n{motors}")

motors.insert(0, 'Harley-Davidson')
print(f"{motors}")

#Removing an Item Using the del Statement
#removes an item from a specific position in the list
print("\nRemoving an Item Using the del Statement")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"\n{motors}")

del motors[0]
print(f"{motors}")

#Removing an Item Using the pop() Method
#removes an item from the end of the list
print("\nRemoving an Item Using the pop() Method")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"\n{motors}")

popped_motor = motors.pop()
print(f"{motors}")
print(f"{popped_motor}")

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print(f"\nusing the pop() method to remove an item from any position in a list")
motos =  ['discovery', 'bmw', 'audi', 'mercedes']
print(f"{motos}")

first_owned = motos.pop(0)
print(f"The first car I owned was a {first_owned.title()}.")
#each time you use pop(), the item you work with is no longer stored in the list.

#Removing an Item by Value using the remove() Method
#removes an item by value instead of by position
print("\nRemoving an Item by Value using the remove() Method")
motors = ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
print(f"{motors}")

motors.remove('Suzuki')
print(f"{motors}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"\n{motorcycles}")
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"{motorcycles}")
print(f"A {too_expensive.title()} is too expensive for me.")

# We can use both the pop(index) and remove(value) methods to remove an item from a list. 
# The pop() method is useful when you want to work with the item after removing it,
# while the remove() method is useful when you know the value of the item you want to remove.