guests = ['Maruf', 'Labib', 'Arib', 'Tanvir']
print (f"\nKew na ashleo {guests[0].title()} ashbei!")
print (f"Free word shunlei {guests[-1].title()} ashbei!")
print (f"Hajar nattomi korar por {guests[1].title()} ashbei!")
print (f"Senior manush {guests[-1].title()} vai na ashle kmne hoi!")

print (f"\nUnfortunately {guests[-1].title()} cant come for family issues!")
guests[-1] = 'Anik'
print (f"So im replacing him with {guests[-1].title()} !")
print (f"Bakira {guests[0].title()}, {guests[1].title()}, {guests[2].title()} ashbei!")

print (f"\nGuyzz new guests are coming tonight, be ready !!")
guests.insert(0, 'Towhid')
guests.insert(2, 'Albab')
guests.append('Sharafat') 
message = "So guyzz our new guests arrived, now the members are : "
print(message)
print(guests)

print (f"\nGuyzz having a bad news , dinner table aint ready!!")
first_victim = guests.pop(0)
print (f"Im extremely sorry dear {first_victim.title()}, its written!!")
sec_victim = guests.pop()
print (f"Im extremely sorry dear {sec_victim.title()}, its written!!")
thrd_victim = guests.pop(4)
print (f"Im extremely sorry dear {thrd_victim.title()}, its written!!")
vic_4 = guests.pop(-2)
print (f"Im extremely sorry dear {vic_4.title()}, its written!!")
vic_5 = guests.pop(1)
print (f"Im extremely sorry dear {vic_5.title()}, its written!!")

print (f"\nYo my boizz {guests[0]}, {guests[1]}, come enjoy the dinner!!")
del guests[1]
del guests[0]
print(guests)





