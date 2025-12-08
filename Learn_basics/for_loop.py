#------------------------------------------------------------------------------#

# basic for loop:

"""
for variable in sequence:
    code block
"""

# Loop through a List

"""fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) # apple \n banana \n cherry
"""
# for Loop with Strings

"""
name = "NEELS"

for ch in name:
    print(ch) # print each character line by line

N
E
E
L
S
"""
# Using range() in for Loops

# The range() function is used to generate a sequence of numbers.
"""
for i in range(5):
    print(i) # 0 1 2 3 4
"""

# Range with Start, Stop, Step
"""
for i in range(2, 10, 2):
    print(i) # 2 4 6 8
"""

# Loop Through Tuple and Set
"""
nums = (10, 20, 30)
for n in nums:
    print(n) # 10 20 30
"""

"""
colors = {"red", "green", "blue"}
for c in colors:
    print(c) # red green blue
"""


# Loop Through Dictionary
"""
student = {"name": "Neels", "age": 21, "course": "AI"}

# Loop through keys
for x in student:
    print(x) # name age course {only keys are printed}

# Loop through values
for x in student.values():
    print(x) # Neels 21 AI {only values are printed}

# Loop through both
for key, value in student.items():
    print(key, ":", value) # name : Neels \n age : 21 \n course : AI

"""

#------------------------------------------------------------------------------#
# nested for loop:
"""
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
"""
#------------------------------------------------------------------------------#
# Loop Control Statements:

# break - Stops the loop completely.

# continue - Skips the current iteration.

# else with for loop

# The else block executes after the loop finishes, unless the loop was broken with break.
#------------------------------------------------------------------------------#
# If you want both the index and value while looping, use enumerate().
"""
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
"""

#------------------------------------------------------------------------------#



#------------------------------------------------------------------------------#
