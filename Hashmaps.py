"""
DEFINITION: A hashmap is a data structure that maps pairs of keys to values. It 
utilizes dictionaries to set up these key-value pairs and store data when needed.

Example #1 - Two Sum: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""
from collections import defaultdict


def twoSum(nums,target):

  hashmap1 = {} #Create an empty hashmap
  for index, number in enumerate(nums): #Iterate with the current index value
    difference = target - number
    if number in hashmap1: #If the number is already in the hashmap...
      return[hashmap1[difference], index] #Then use the difference as a key to find the value associated with it, return that value alongside the current index
    hashmap1[number] = index #If the number is not in the hashmap, add the number to the hashmap as a key with its index as a value

"""
Example #2 - Group Anagrams: Given an array of strings strs, group the anagrams 
together. You can return the answer in any order.
"""
def groupAnagrams(strs):

  result = defaultdict(list) #Creates a defaultdict that automatically creates an empty list if the key doesn't exist in the dictionary
  for word in strs: #Iterate through every word in the array strs
    count = [0] * 26 #For every new word used in the loop, set count to 26 zeroes

    for letter in word: #Iterate through every letter in the word
      count[ord(letter)- ord("a")] += 1 #If "a" is the first letter, then it is automatically assigned to index 0 and then it is increased by 1 every time it appears... "b" would be the index 1 and so on
    result[tuple(count)].append(word) #Convert the list of count to a tuple, because lists cannot be keys in dictionaries. Use the tuple as a key and then add the current word as the value
  
  return result.values() #Only return the values, or the words, from the defaultdict

"""
Example #3 - Top K Frequent Elements: Given an integer array nums and an int k, 
return the k most frequent elements. You may return the answer in any order.
"""
def topKFrequent(nums, k):
  count = {}
  freq = [[] for i in range(len(nums) + 1)]

  for n in nums:
    count[n] = 1 + count.get(n, 0)
  for n, c in count.items():
    freq[c].append(n)

  result = []
  for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
      result.append(n)
      if len(result) == k:
        return result