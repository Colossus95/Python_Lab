# lets learn list, [] is used to create a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elements in a List
print(bicycles[0])               # python also starts counting at 0
print(bicycles[1])               # accessing the second element
print(bicycles[1].title())       # title() method capitalization
print(bicycles[-1])              # accessing the last element in the list
print(bicycles[-2])              # accessing the second last 
print(bicycles)

bicycles = ['veloce', 'giant', 'phoenix', 'turbo']
message = f"\nMy first bicycle was a {bicycles[0].title()}."
print(message)