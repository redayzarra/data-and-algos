"""
Dictionaries are tables that can be used to have keys refer to corresponding 
values. These pairs are called key-value pairs and they are stored in 
dictionaries where they can be used as data.

In dictionaries, you can manipulate them with:
      search() - looks for a specific key to retrieve a corresponding value
      insert() - adds a new entry with specified a key-value pair
      delete() - deletes an existing key-value pair

All the opearations above are usually O(1) time complexity.

LISTS CANNOT BE KEYS. CANNOT HAVE DUPLICATE KEYS.
"""
from collections import defaultdict


my_dict = {} #Creates an empty dictionary
grades = {"Ana":"B", "James":"A", "Miguel":"B"} #The format is key:value

"""
DEFAULTDICT: If you want a dictionary-like object that assigns any key that does
not exist to return an empty list, set, or integer zero use defaultdict() with 
the list, set, or int parameter
"""
idnum = defaultdict(int) #Creates a dictionary that will automatically add the value of 0 to a key if the key doesn't already exist in the dictionary
print(idnum[3]) #Look for key 3, if its not there then assign and print 0

people = defaultdict(list) #Creates a dictionary that will create an empty list for the value if the key provided doesn't already exist
people['one'].append(1) #Create key called 'one' that has a list as the value, add the integer 1 to that list
people['two'].append(2)
people['one'].append('1') #Add an entry of '1' in the list associated with the key of 'one' 
people['three'] #Create a key called 'three' that has no specified value so it automatically assigns an empty list as the value
print(dict(people.items())) #Converts the defaultdict to a readable dictionary, can also be converted into a list.


food = defaultdict(set) #Creates a dictionary that will add an empty set as a value if the key doesn't exist. Makes it so that values for every key have to be distinct.
food['one'].add(1) #Create a key called 'one' with a set as a value, and add int 1 to that set
food['two'].add(2)
food['one'].add('1') #Add '1' to the set associated with 'one'
food['three'] #Automatically adds an empty set to key of 'three' because it does not already exist in the dictionary
print(dict(food.items())) #Convert food into a readable dictionary and print all the items from it

"""
RETURN: To search for a value, use the dictname[key] to return the value
"""
print(grades["Ana"]) #Only works if the key exists

"""
RETURN: To return both the keys and the values associated with them in a for 
loop, use the x,y in dictname.items() method to assign keys to x and values to y
"""
exampledict = {1: "kratos", 2: "atreus", 3: "mimir"}
for x,y in exampledict.items():
      print(x,y)

"""
ADDITION: To add an entry in to a dictionary, use dictname[key] = value
"""
grades["Marina"] = "A"

"""
ADDITION: To RETURN a value of a specific key or to ADD it if it doesn't already
exist in the dictionary, use dictname.get(key, value)
"""
newexample = {1:"one", 2:"two", 3:"three"}
checkingtest = newexample.get(1, "four")
print(checkingtest)

"""
TEST: To see if a value is in a dictionary, use key in dictname
"""
print("Ana" in grades)

"""
DELETE: To delete an entry in a dictionary, use del(dictname[key])
"""
del(grades["Marina"])

"""
RETURN: To get all the keys from a dictionary, use dictname.keys()
"""
print(grades.keys()) #Returns an iterable tuple that can be used for loops

"""
RETURN: To get all values from a dictionary, use dictname.values()
"""
print(grades.values())

################################################################################

"Example #1: Create a dictionary that counts the frequency of words in songs"

#user_song = input("Copy and paste a song: ") #Asks for user's song
#lyrics_given = user_song.split(" ") #Split's the song lyrics by spaces into array

def lyrics_frequencies(lyrics): #Define a function for word frequency
      myDict = {} #Create an empty dictionary
      for word in lyrics: #Iterate through every word in song lyrics
            if word in myDict: #If the word alread exists in dict...
                  myDict[word] += 1 #Then go ahead and add one to it every time
            else: #If the word doesn't exist in the dict...
                  myDict[word] = 1 #Then set the value to the key to be 1
      return myDict

def most_common_words(freqs): #Define a function for most common words
      values = freqs.values() #Assign the values of word occurences to variable
      best = max(values) #Find the highest number out of that
      words = [] #Create an array named words
      for k in freqs: #Iterate through every element in the words to count dict
            if freqs[k] == best: #If the key word's value equals to best
                  words.append(k) #Add the key word to empty array words
      return (words, best) #Return the key word and value of most common word

def words_often(freqs, minTimes): 
      result = [] #Create an empty array
      done = False #Assign variable called done to the boolean of False
      while not done: #As long as not done, or not False, continue executing
            temp = most_common_words(freqs) #Assign temp the result of function
#THE TRICK ^^^ The dictionary is being put through the function every time the while loop executes, meaning the dictionary changes every time until the loop is told to stop.
            if temp[1] >= minTimes: 
                  result.append(temp) #Add temp to array called result
                  for w in temp[0]: #Iterate through the most common words given
                        del(freqs[w]) #Delete them from the original dictionary
            else: #If the number of occurences of most common word is not minTimes
                  done = True #Then done is now True and the loop ends.
      return result

################################################################################
"""
Example #2: Fibonacci Recursive Code - Dictionaries are helpful because instead
of calculating the same value many times, we can simply store and call them. By 
using a recurive function, we are modifying the dictionary as we progress.
"""
def fib_efficient (num, dict): #Create a function that takes a number and a dictionary as an argument
      if num in dict: #If the number key already exists then...
            return dict[num] #Just give us the value associated with the num
      else: #If not already in dictionary then...
            answer = fib_efficient(num - 1, dict) + fib_efficient(num - 2, dict) #Recall the answer for the smaller values of num and then assign that to variable answer
#THE TRICK ^^^ The function calls itself again with a subtracted values of num to see if they already exist in the dictionary, if they don't then the function runs for those smaller values of num as well. 
            dict[num] = answer #Add a new entry in the dictionary for answer
            return answer 