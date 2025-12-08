#-------------------------------------------------------------------------------------#
"""
Conditional statements are a fundamental concept in programming that allows you to make decisions based on certain conditions. These statements enable your code to execute different blocks of code depending on whether specific conditions are met or not. In this blog post, we'll delve into the basics of conditional statements, starting with the ubiquitous if-else statement and gradually exploring more complex scenarios.


'if statement' is used to execute a block of code only if a certain condition is met. It allows us to conditionally execute code based on whether the specified condition is true.

'else statement', on the other hand, is an optional companion to the if statement. It specifies what code to execute if the condition in the if statement is not met (i.e. if it is false).

Let's break down the flow of control:

If the test condition in the if statement is true, a block of code inside the if block will be executed.
If the test condition is false, the code inside the else block (if present) will be executed.
"""

#-------------------------------------------------------------------------------------#

# Problem statement:

# If marks are less than 25, it prints "Grade: F."
# If marks are between 25 and 44 (inclusive), it prints "Grade: E."
# If marks are between 45 and 49 (inclusive), it prints "Grade: D."
# If marks are between 50 and 59 (inclusive), it prints "Grade: C."
# If marks are between 60 and 69 (inclusive), it prints "Grade: B."
# If marks are 70 or higher, it prints "Grade: A."
# If marks are outside the valid range, it prints "Invalid marks entered."

#-------------------------------------------------------------------------------------#

marks = -2
grade ='X'
if marks >0:
    if marks<25 :
        grade ='F'
    elif marks<=44:
        grade ='E'
    elif marks<=49:
        grade ='D'
    elif marks<=59:
        grade ='C'
    elif marks<=69:
        grade ='B'
    elif marks >=70 :
        grade ='A'

print(f"Grade: {grade}")