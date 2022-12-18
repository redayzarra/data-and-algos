"""
DEFINITION: Tuples are an ordered sequence of elements that can include any 
different kind of element within them.

- "Ordered element" as in the sequence itself has an order. So you can get to 
different parts of a sequence by indexing. 

- Tuples are immutable, meaning the values inside them cannot change. Just like
with strings, you cannot change the values inside either of them.
"""

tuple_example = () #Parenthesis indicate that its a tuple

tuple_1 = (2, "one", 4) #Tuples can contain anything inside of them

answer = tuple_1[0] #Tuples can also be indexed
print(answer)

tuple_1 + (5, 7) #Tuples can be concatenated together

tuple_1[1:3] #Slices the tuple and only returns elements with index 1 and 2

"""
FORMATTING: If a tuple only has one element such as 'one' then the tuple has to 
have a comma next to it for Python to understand... so instead of ('one') it will
be written as ('one',)
"""
not_tuple = ('one')
is_tuple = ('one',)

"""
USES: Tuples are really convenient for swapping variables because they can do it 
directly without using a temporary variable.
"""
x = 1
y = 2 #Assigns variables
(x, y) = (y, x) #Utilize tuple to change swap the variables
print(x, y)

"""
USES: Tuples are also great for returning more than one value from a function.
"""
def quotient_and_remainder(x, y): #Defines a function with parameters x and y
  q = x//y #Assigns the value q to the whole number dividend of x and y
  r = x%y #Assigns the value r to the remainder of x divided by y
  return (q, r) #Return the values of q and r
(quot, rem) = quotient_and_remainder(4, 5) #Assigns quot and rem to q and r

"""
MANIPULATION: Tuples are iterable meaning you can use loops to walk down them.
"""
def getData(aTuple): #Defines a function that takes a tuple for a parameter
  nums = () 
  words = () #Assigns variables nums and words to empty tuples
  for t in aTuple: #Iterates through the elements of the argument aTuple
    nums = nums + (t[0],) #Add the first element of the given pair to nums
    if t[1] not in words: #If the second element of the pair is not in words
      words = words + (t[1],) #Then add that second element to words
  min_nums = min(nums) #Finds the smallest number in nums
  max_nums = max(nums) #Finds the largest number in nums
  unique_words = len(words) #Finds the length of words 
  return min_nums, max_nums, unique_words