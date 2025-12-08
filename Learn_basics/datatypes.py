#-------------------------------------------------------------------------------------#
"""
At the core of any programming language lies the concept of data types a way for the language to understand what kind of value a variable can hold. Data types define not only the nature of the data but also the operations you can perform on it and the amount of memory it will consume. If you think of a variable as a box, then the data type is the label on that box telling the computer what’s inside and how to handle it. In some languages (like C++ and Java), you must explicitly declare the data type before using a variable. In others (like Python and JavaScript), the type is determined automatically at runtime based on the assigned value.
"""
#-------------------------------------------------------------------------------------#
"""
Python is dynamically typed, meaning you don’t need to declare the data type the interpreter figures it out at runtime. This makes coding faster but can also lead to subtle bugs if you’re not careful.

Numeric Types:
int for integers (unlimited size).
float for decimal numbers (double precision).
complex for complex numbers (3+5j).
Sequence Types: list, tuple, and range for ordered collections.
Text Type: str for strings.
Mapping Type: dict for key-value pairs.
Set Types: set and frozenset for unordered collections of unique elements.
Boolean Type: bool for logical operations.


Python is flexible you can assign an integer to a variable, then later assign a string to the same variable without errors. But this flexibility means you have to be more cautious with type-related logic.

Dynamic typing; immutable vs mutable matters (tuple vs list); integers unbounded.
"""

#-------------------------------------------------------------------------------------#
# a_int =3
# print(a_int,type(a_int))
# b_float=4.5
# print(b_float,type(b_float))
# c_complex=4+3j
# print(c_complex,type(c_complex))
# d_list= [2,3,4,5]
# print(d_list,type(d_list))
# e_tuple =(2,4,5,6)
# print(e_tuple,type(e_tuple))
d_set ={1,2,4,4,1,2,3}
d_set.add(10)
print(d_set,type(d_set))
f_set= frozenset([2,4,5,4,5,6,7])
# f_set.add(10)
print(f_set,type(f_set))

# dict_c= {
#     "name":"neels",
#     "age":12
# }
# print(dict_c,type(dict_c))
# x_bool= True
# print(x_bool,type(x_bool))

#-------------------------------------------------------------------------------------#

"""
Set vs frozen set

set (Mutable):
A set is a mutable data type, meaning its contents can be modified after creation.
Elements can be added using methods like add() and update(), and removed using methods like remove(), discard(), and pop().
Sets are created using curly braces {} or the set() constructor.


frozenset (Immutable):
A frozenset is an immutable data type, meaning its contents cannot be changed once created.
It does not support methods that modify the set, such as add(), remove(), or update(). Attempting to use these methods will result in an AttributeError.
Frozensets are created using the frozenset() constructor, which takes an iterable as an argument.
"""