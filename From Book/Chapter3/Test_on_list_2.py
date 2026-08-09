places = ['ANDALUS', 'PALESTINE', 'SWITZERLAND', 'KASHMIR', 'SAMARKHAND']
print(f"\n{places}")

print (f"\nTemporary Sorted list : ")
print(sorted(places))


print (f"\nOriginaal list : ")
print(places)

print (f"\nTemporary  Reverse Sorted list : ")
print(sorted(places, reverse = True))

print (f"\nOriginaal list : ")
print(places)

places = ['ANDALUS', 'PALESTINE', 'SWITZERLAND', 'KASHMIR', 'SAMARKHAND']
places.reverse()
print(f"\n{places}")

places.reverse()
print(f"\n{places}")

places.sort()
print(f"\n{places}")

places.sort(reverse = True)
print(f"\n{places}")

length = len(places)
print(f"\nThe number of places id like to travel is {length}")

