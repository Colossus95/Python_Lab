for value in range(1, 21):
    print(value)

Biggy = list(range(1, 1000000))
for maans in Biggy:
    print(maans)

Biggy = list(range(1, 1000000))
choto = min(Biggy)
boro = max(Biggy)
total = sum(Biggy)
print(f"\nEi list er total sum holo {total}")

Evens = []
for maans in list(range(2, 21, 2)):
    Evens.append(maans)
print(Evens)    

Odds = []
for maans in list(range(1, 20, 2)):
    Odds.append(maans)
print(Odds)

multiples = []
for maans in list(range(3, 31)):
    multiples.append(maans*3)
print(multiples)    

cubes = []
for maans in list(range(1, 11)):
    cubes.append(maans**3)
print(cubes) 

cubes = [maans**3 for maans in range(1, 11)]
print(cubes)