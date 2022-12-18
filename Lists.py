"""
DEFINITION: List is an ordered sequence of information that can be accessed by
an index. 

- "Ordered sequence" does not mean ascending order but rather they are ordered so
you can access specific indices. 

- Lists can contain different types of elements but they usually have just one 
specific element such as numbers or strings. 

- Lists can be changed, so they are mutable. You can change portions inside them.
"""
a_list = [] #Creates an empty list that is assigned to a variable
b_list = [2, 'a', True, 5] #Can contain multiple different types of elements
myList = [1, 2, 3, 4]

len(myList) #Returns the length of the list
myList[0] #Returns the first element of the list
myList[3] + 10 #Allows you to retrieve an element and then manipulate it

"""
INDICES: The indices of lists can be expressions or variables, however, they have
to be manipulated to an int type to work. 
"""
i = 2
myList[3 - i] #Returns the element at index 1 or the second element

"""
MANIPULATION: Because lists are mutable, it is possible to specify certain 
elements and change them however we like. 
"""
List = [1, 2, 3, 4] #Create a list with these four elements
List[1] = 22 #Identify the element at index 1 and change it to 22
print(List) #Print the new array which is now [1, 22, 3, 4]
List = [1, 2, [10, 11, 12], 3, 4]
print(List[2][2]) #Returns the number 12 

"""
USES: Lists are great for iterating through every element and adding them all
up to find the sum of all the elements.
"""
total = 0 
example = [1, 3, 45, 1]
for i in example:
  total += i
print(total)

"""
ADDITION: To add ONE ELEMENT at the end of the list, you can use the .append(#)
method at the end of the list's name. However, this mutates the list.
"""
List1 = [1, 2, 3, 4]
List1.append(5) #Adds this one element to the list above

"""
ADDITION: To add MULTIPLE ELEMENTS at the end of the list, you can use the 
.extend([elements]) method at the end of list's name.  
"""
List1.extend([6, 7, 8]) #Adds these MULTIPLE elements to the list

"""
ADDITION: To replace an element at a specified index, use .insert(index, element) 
method so it will add the specific element to that index
"""
grocery = [1, 2, 3, 4, 5]
grocery.insert(3, "three") #Replaces the element at index 3 to the str "three"
print(grocery)

"""
ADDITION: To add lists to other lists, you can simply concatenate them together
using their variable names.
"""
List2 = [9, 10]
List3 = List1 + List2

"""
DELETION: To delete specific indices, use the del(list_name[index]) 
"""
List4 = [1, 2, 3, 44, 4]
del(List4[3])
print(List4)

"""
DELETION: To delete a specific index from a list and also return it, use the 
listname.pop(index) or just .pop() to remove the last element
"""
List5 = [1, 2, 3, 4, 5]
x = List5.pop(2)
print(x)
print(List5)

"""
DELETION: To delete the first occurence of a specific element, use the 
listname.remove(element) method
"""
List6 = [5, 4, 3, 3, 2, 1]
List6.remove(3) #Removes first occurence only
print(List6)

"""
CONVERSION: To convert a string into a list, use the list(listname) function 
to put every letter of a word into its own index
"""
sting = "stings" #Define a string 
yyy = list(sting) #Converts the string into a list and stores it seperately
print(yyy)

"""
CONVERSION: To join a list of letters into a string, use the ''.join(listname)
method which also allows you to specify what goes in betweeen every letter
"""
xxx = "".join(yyy) #Joins every element of the list and leaves no space in between
print(xxx)

"""
CONVERSION: To split a string by a specified character, or split sentence of 
strings by words, use the .split('space or character')
"""
poem = "this is my poem i am so creative" #Define a string (sentence)
split_poem = poem.split(" ") #Split the sentence by spaces and assign away
print(split_poem)

"""
SORTING: To sort a list in ascending order or aplhabetically but NOT CHANGING the
original list use the sorted(listname) function
"""
newlist = ["ace", "zy", "aa", "bac"]
sortedlist = sorted(newlist) #Assings the sorted version of the list to variable
print(sortedlist)

"""
SORTING: To sort a list in ascending order or aplhabetically and CHANGING IT, use
the listname.sort() method which changes the list permanently.
"""
anotherlist = [4, 34, 5, 1, 7]
anotherlist.sort() #Directly sorts the original list
print(anotherlist)

"""
SORTING: To reverse a list from end to start, use the listname.reverse() function
"""
listsagain = [1, 2, 3, 4, 5]
listsagain.reverse()
print(listsagain)

"""
CLONING: To create a new list and copy every element in the list, use listname[:]
"""
red = ["red", "orange", "yellow"]
warm = red[:] #Creates a different version of the list and assigns to warm