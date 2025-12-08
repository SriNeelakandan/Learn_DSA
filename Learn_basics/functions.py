"""
How Values Are Passed in Python
- In Python, everything is an object, and variables are references (names pointing to objects).
- This means Python uses a system called:
- “Call by Object Reference” (also called Call by Sharing)

Let’s see how it works for immutable and mutable types.
"""

# Case 1: Immutable Objects (int, float, str, tuple)
# act like pass by value
"""
def modify(x):
    x = x + 10
    print("Inside:", x)

a = 5
modify(a)
print("Outside:", a)

"""

#Output:

"""
Inside: 15
Outside: 5

Explanation:
- The reference to 5 is passed to x.
- When x = x + 10 executes, Python creates a new object 15.
- The original variable a still points to 5.
- So changes inside the function don’t affect the original variable.
"""

# Case 2: Mutable Objects (list, dict, set)

"""
def modify_list(lst):
    lst.append(4)
    print("Inside:", lst)

nums = [1, 2, 3]
modify_list(nums)
print("Outside:", nums)
"""
#Output:

"""
Inside: [1, 2, 3, 4]
Outside: [1, 2, 3, 4]

Explanation:
- lst and nums point to the same list object.
- Modifying the list inside the function affects the original.
- Because the object itself is mutable, both see the change.
"""
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())