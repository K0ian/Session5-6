s = "hello"
useful_methods = [m for m in dir(s) if "--" not in m]

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as .lower() method

print("hello".center(50))
print("hello".center(50, "*"))

print("I see a little dove".count("e")) # how many times do I see "e"
print("bananananananananana".count("ana"))
x = "I do not cook nor compare"
print(f"There are {x.count("o")}os inside: '{x}'")
