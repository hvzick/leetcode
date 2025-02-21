'''You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        hashMap = {}                                    # initialise a dictionary
        counter = 0                                     # initialise a cpunter
        for k, v in enumerate(words):                   # create a dictionary whose key is the index of word list and values are the values at the corresponding index in the word list
            hashMap[k] = v
        for value in hashMap.values():                  # loop over the value of the hash map
            if all(char in allowed for char in value):  # check in each element of value is in allowed
                counter += 1                            # increment the counter when condition is true
        return counter                                  # return the counter

mySol = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(mySol.countConsistentStrings(allowed, words))