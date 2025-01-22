name = input("what is your name?")
print("hello", name)
age = input("How old are you?")
try:
    age = int(age)  # I am trying to convert it to a number
    print("you were probably born in", 2024 - age)
    new_age = age / 0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    print("something unexpected happened")
else: # this happens if no error occurs
    print("you were probably born in", 2024 - age)
finally:
    print("thanks for playing")


