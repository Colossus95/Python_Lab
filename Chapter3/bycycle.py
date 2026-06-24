# lets learn list, [] is used to create a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elements in a List
print(bicycles[0])               # python also starts counting at 0
print(bicycles[1])               # accessing the second element
print(bicycles[1].title())       # title() method capitalization
print(bicycles[-1])              # accessing the last element in this list
print(bicycles[-2])              # accessing the second last 
print(bicycles)

bicycles = ['veloce', 'giant', 'phoenix', 'turbo']
message = f"\nMy first bicycle was a {bicycles[0].title()}."
print(message)

#some practice with lists
friends = ['Alice', 'Bob', 'Charlie', 'David']

print(f"\n{friends[0]}")        # accessing the first element
print(friends[1])               # accessing the second element
print(friends[2])               # accessing the third element
print(friends[3])               # accessing the fourth element

print (f"\nMy friend {friends[0].title()} is a greedy person.")
print (f"My friend {friends[1].title()} is a kind person.")
print (f"My friend {friends[2].title()} is a helpful person.")
print (f"My friend {friends[3].title()} is a friendly person.")

motors = ['honda', 'yamaha', 'suzuki', 'kawasaki']
print(f"\nI have a dream to get a ride on a {motors[0].title()} motorcycle.")
print(f"I have a dream to get a ride on a {motors[1].title()} motorcycle.")
print(f"I have a dream to get a ride on a {motors[2].title()} motorcycle.")
print(f"I have a dream to get a ride on a {motors[3].title()} motorcycle.")
