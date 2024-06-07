# Basic usage
name = "Alice"
age = 30
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)  # Output: My name is Alice and I am 30 years old.

# Positional arguments
sentence = "My name is {0} and I am {1} years old.".format(name, age)
print(sentence)  # Output: My name is Alice and I am 30 years old.

# Keyword arguments
sentence = "My name is {name} and I am {age} years old.".format(name=name, age=age)
print(sentence)  # Output: My name is Alice and I am 30 years old.

# Formatting options
pi = 3.14159
formatted_pi = "The value of pi is {:.2f}".format(pi)
print(formatted_pi)  # Output: The value of pi is 3.14




# this featur in latest update of python 3.6
name = "Alice"
age = 30
sentence = f"My name is {name} and I am {age} years old."
print(sentence)  # Output: My name is Alice and I am 30 years old.
