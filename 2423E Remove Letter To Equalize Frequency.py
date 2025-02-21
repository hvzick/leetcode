'''You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.'''
class Solution:
    def equalFrequency(self, word: str) -> bool:
        hashMap = {}                            # initialise a dictionary
        j = 97                                  # j = starting number of ASCII value of 'a'
        for i in range(0, len(word)):           # loop over all alphabets
            if word[i] not in hashMap:          # check if current alphabet is not in hashmap
                hashMap[word[i]] = 1            # set dictionary key as alphabet and value as 1
            else:                               
                hashMap[word[i]] += 1           # increment value of the key which represents the frequency of the alphabets
        for key in hashMap:                     # loop over key and values in the hashmap
            temp = hashMap.copy()               # create another dict as copy of hashmap
            temp[key] -= 1                      # decrement values of cuurent key
            if temp[key] == 0:                  # check if its value is 0
                del temp[key]                   # delete the key and value
            if len(set(temp.values())) == 1:    # check if length of set is 1 which is possible only when all have same frequency
                return True                     # return True
        return False                            # return False

mySol = Solution()
word = "aabb"
print(mySol.equalFrequency(word))