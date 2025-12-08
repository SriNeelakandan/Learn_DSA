# Arithmetic Operators
# +
# -
# *
# /
# //
# %
# a,b=map(int,input().split())
# print(f"Add: {a}+{b}= {a+b}")
# print(f"Sub: {a}-{b}= {a-b}")
# print(f"Mul: {a}*{b}= {a*b}")
# print(f"Div: {a}/{b}= {a/b}")
# print(f"FloorDiv: {a}//{b}= {a//b}")
# print(f"Modulus: {a}%{b}= {a%b}")

# Output:

# Add: 15+4= 19
# Sub: 15-4= 11
# Mul: 15*4= 60
# Div: 15/4= 3.75
# FloorDiv: 15//4= 3
# Modulus: 15%4= 3

# Assignment operators

# a=int(input())
# b=a
# print(a,b)
# print(a is b)

# Short hand Operators

# a=int(input())
# a+=3
# print(f"a+=3: {a}")

# a-=5
# print(f"a-=5: {a}")

# a*=10
# print(f"a*=10: {a}")

# a/=3
# print(f"a/=3: {a:.2f}")

# a//=3
# print(f"a//=3: {a}")

# a%=4
# print(f"a%=4: {a}")

# a**=2
# print(f"a**=2: {a} ")

# Output:

# a+=3: 18
# a-=5: 13
# a*=10: 130
# a/=3: 43.33
# a//=3: 14.0
# a%=4: 2.0
# a**=2: 4.0 

# a=int(input())
# b=2
# # c=(a>>b) # a/(2**b)
# c=a<<b # a*(2**b)
# print(c)
# x_and=a&2
# print(f"a: {bin(a)}")
# print(f"2: {bin(2)}")
# print(f"and: {x_and},{bin(x_and)}")

# _or=a|3
# print(f"a: {bin(a)}")
# print(f"2: {bin(3)}")
# print(f"_or: {_or},{bin(_or)}")

# x_not=~a
# print(f"a: {bin(a)}")
# print(f"2: {bin(x_not)}")
# print(f"not: {x_not}")

# x_or=a^3
# print(f"a: {bin(a)}")
# print(f"2: {bin(3)}")
# print(f"x_or: {x_or},{bin(x_or)}")

# Output:
# a: 0b1111
# 2: 0b10
# and: 2,0b10
# a: 0b1111
# 2: 0b11
# _or: 15,0b1111
# a: 0b1111
# 2: -0b10000
# not: -16
# a: 0b1111
# 2: 0b11
# x_or: 12,0b1100


# # Comparison Operator
# x = 10

# print(1 < x < 10)

# print(1 < x and x < 10)

# Logical Operator

# and, or, not

# Identity Operator:
# is,is not 

# Membership operators
#in, not in 

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

x = "global"

def outer():
  x = "enclosing"
  def inner():
    # nonlocal x
    x="Local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)