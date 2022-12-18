"""
DEFINITION: Range is a special procedure that returns something that behaves
like a tuple. It essentially gives you the numbers between two specified values
"""
print(range(5)) #Equivalent to [0, 1, 2, 3, 4]
print(range(2, 6)) #Equivalent to [2, 3, 4, 5]
print(range(5, 2, -1)) #Equivalent to [5, 4, 3]

"""
USES: When you use range in a for loop, the special procedure range behaves like
a list.
"""

# High Order Procedures
"""
DEFINITION: A high order procedure is a generalization of very common procedures 
in Python. To apply a function to every element, use map(function, array)
"""
for element in map(abs, [-1, 3, 5, -3]):
  print(element)