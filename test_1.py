# 2-3 Personal Message
name = "Eric"
print(f"\nHello {name}, would you like to learn some Python today?")

# 2-4 Name Cases
first_name = "eric"
last_name = "matthes"
fullname = f"{first_name} {last_name}"
print(f"\n{fullname.title()}")
print(fullname.upper())
print(fullname.lower())

# 2-5 Famous Quote
print(f"\n\"Albert Einstein once said, \"A person who never made a mistake never tried anything new.")

# 2-6 Famous Quote 2
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# 2-7 Stripping Names
name = ' Eric '
print(f"\n'{name}'")
print(f"'{name.lstrip()}'")
print(f"'{name.rstrip()}'")
print(f"'{name.strip()}'")