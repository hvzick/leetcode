'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashMap = {}
        for i in range(0, len(arr)):    # create a dictionary with numebrs as keys and their occurances as values
            if arr[i] not in hashMap:   # if the key isnt in the dict
                hashMap[arr[i]] = 0     # add it to the dict with 0 as its value
            else:                       # if the key is in the dict
                hashMap[arr[i]] += 1    # increment the value by 1
        if len(set(hashMap.values())) == len(hashMap): # check if the length of set values of dictionary is equal to the length of hashmap
            return True                 # if yes return true
        else:
            return False                # return false

mySol = Solution()
array = [-3,0,1,-3,1,1,1,-3,10,0]
print(mySol.uniqueOccurrences(array))
