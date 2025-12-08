#-------------------------------------------------------------------------------------#

"""Python does not support switch case,
it can be implemented by using if-elif-else statements

match - case introduced in later 3.10 version
"""
#-------------------------------------------------------------------------------------#

x=2
match x:
    case 1:
        print("One")
    case 3:
        print("Two")    
    case _:
        print("Hello")