# Looping Through a String 
for x in "banana":   
    print(x)

# string length
a = "hello, world!"
print(len(a))

# check string
txt = "The best things in life are free!"
# print("free" in txt) # return true

# or we can use the if command as well
if "free" in txt:
    print("true")

# similary for hte not in text is also there
if "expensive" not in txt:
    print("true")

# slicing: You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "hello world"
print(b[2:5])
print(b[:5]) # both are same 1st and second one as if you leave start index so it asssumes as 0

# negative indexing start from back and slice to the end all are also comes in this

# python- modify strings
print(b.upper()) # returns the string in uppercase
print(b.lower()) # return it in lowercase

a = "  hello, world! "
print(a.strip())  # returns "hello, world!" remove whitespaces means remove the space from begining and from end.

# replace() method - replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# split string - split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', 'World']

# string concatenation
# we use the + operator for this
a = "hello"
b = "world"
c = a+b
# c = a + " " + b  # this we can use to add space in between
print(c)

# stirng format - we cannot combine string with no using the + operator
# f- string : simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is john, I am {age}"
print(txt)

# if we had to represent in the float format so we should write:
txt = f"My name is john, I am {age:.2f} years old"
print(txt)

# so these curly braces are called placeholder and we can do the math operattion as well inside to get the value in theoutput when we print

# ESCAPE CHARACTERS : To insert characters that are illegal in a string, use an escape character. An escape character is a backslash \ followed by the character you want to insert.
# suppose the txt is : txt = "We are the so-called "Vikings" from the north."
# so To fix this problem, use the escape character \":

txt = "We are the sol called \"Vikings\" from the north"

# string methods - you can refer the readme file of this week to get into this
# python has an builtin methods that we can use on the strings



 




