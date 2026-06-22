# Normal case, upper case, and lower case
# f means format, it allows us to insert variables into a string
name = "ada lovelace"
print(f"Normal case: {name.title()}")
print(f"Upper case: {name.upper()}")
print(f"Lower case: {name.lower()}")

# using \t and \n to add whitespace
first_name = "yousuf"
last_name = "zulqernine"
full_name = f"{first_name} {last_name}"
print(f"\n{full_name.title()}")
print(f"\tHello, I am {full_name.title()}")
message = f"\tThe name {last_name.title()} draws inspiration from Surah Al-Kahf!"
print(f"{message}") 

# using strip() to remove whitespace
favorite_language = " python "
print(f"\nfavorite_language")
print(f"'{favorite_language.rstrip()}'")
print(f"'{favorite_language.lstrip()}'")
print(f"'{favorite_language.strip()}'")    