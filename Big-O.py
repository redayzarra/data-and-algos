"""
Big O describes the performance of an algorithm and the relationship between
the input of function and time.

Constant time is    O(1)
Lograthmic time is  O(logn)
Linear time is      O(n)
Quadratic time is   O(n^2)

O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)

T = a*n + b
To find the time complexity:
    1. Find the fastest growing term in a function... T = a*n
    2. Remove the coefficient... T = n so its O(n)

Example: T = cn^2 + dn + e 
    1. Find the fastest growing term... T = cn^2
    2. Take out the coefficient... T = n^2 so its O(n^2)
"""
given_array = [1, 4, 3, 2, 10]

# Constant time complexity - time does does not increase as the input increases
def stupid_function(given_array):
  total = 0
  return total

"""
The function above does not do anything with the input array so the time 
complexity is constant. 

T = O(1) because the time it takes to run the function is constant.
"""

# Practice 1
def find_sum(given_array):
  total = 0 #O(1)
  for i in given_array: #O(n)
    total += i #O(1)
  return total #O(1)

"""
The function above is linear time complexity because the for loop is looping thru
the entire input making it so that more input means more time.
"""

# Practice 2
array_2d = [[1, 4, 3],
            [3, 1, 9],
            [0, 5, 2]]

def find_sum_2d(array_2d):
  total = 0
  for row in array_2d:
    for i in row:
      total += i
  return total

"""
The function above is O(n^2) because the first for loop is O(n) and the second
for loop is also O(n). So they both multiply to be O(n^2) meaning its quadratic.
"""

# Logarithmic Time Complexity - logarithm is the power a given number needs to be
#                               raised to, to get some desired number.
# 2^? = 8 can be rewritten as Log2(8) = ?

def log_function(n):
  if n == 0:
    return "Done."
  n /= 2
  return

"""
The function above takes the argument n and then divides it every time. This means
that if n is 8... then it will become 4, and then 2. The function is logarithmic
because it is recursive and becomes exponentially smaller.
"""

# nlog(n) Time Complexity:

def nLogN_function(n):
  y = n
  i = 1
  while (n > 1):
    n /= 2
    while i <= y:
      print(i)

"""
The function above has two loops: top loop and bottom loop. The top loop divides
the value of n everytime, and the bottom loop prints out a certain value until a
certain condition is met. This means that one loop is O(logn) and it has to be 
repeated n times. This is why the function is O(nlogn)
"""