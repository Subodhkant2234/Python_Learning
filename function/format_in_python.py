str1 = "Jhon"
str2 = "Doe"
print(str1 + " " + str2)
print("John" * 3)

"""
String Formatting in Python
You might have the experience to use C language to print String and Integer using %s and %d. Python has similar string formatting to create new, formatted strings. The % operator is used to format variables.
"""
name = "John Doe"
print("Hello, %s How are you?" % name)

name = "John Doe"
salary = 10000
period = "Month"
print("%s earns %d" % (name, salary))
print("%s earns %d per %s" % (name, salary, period))

