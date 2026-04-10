# pass statement is passed as if we dont have logic or something we do we generally in that case use passs

# python match: instead of writing many if else we can switch to the match
# The match statemtn is used to perform different actions based on different conditions.   : The match statement selects one of many code blocks to be executed.

""" syntax : 
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block

eg : day = 4
match day:
    case1:
        print("Monday")
    case2:
        print("Tuesday")
    case3:
        print("Wednesday")
    case4:
        print("Thursday")
    case5:
        print("Friday")
    case6:
        print("Saturday")
    case7:
        print("Sunday")
    case _:
        print("Looking forward for the weekend") # This  _ will always match, so it is important to palce it as the last case to make it behave as a default case
"""

#The while loop : With the while loop we can execute a set of statements as long as a condition is true.
i =1
while i < 6:
    print(i)
    i += 1

# we can use the break statement to stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# With the continue statement we can stop the current iteration, and continue with the next:
# we can use the else at last after while to print the desired output such as 
i = 1
while i < 6:
   print(i)
   i += 1
else:
   print("i is no longer less than 6")

# for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple","banana","cherry"]
for x in fruits:
   print(x)

for x in "banana": # looping through the strings
   print(x)

for x in range(6):
   print(x)

for x in range(2,6): # 6 is not going to include
   print(x)  

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

