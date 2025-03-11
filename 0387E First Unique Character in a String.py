'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:                     # if s has only 1 letter
            return 0                        # coz it will be at 0th index
        else:
            hashMap = {}
            for i in range(0, len(s)):      # loop over the letters in s
                if s[i] not in hashMap:     # check if current letter is not in hash map
                    hashMap[s[i]] = 1       # add it to hashmap as key and its frequency as value
                else:                       # if the key is already in the hash map
                    hashMap[s[i]] += 1      # increment the value 
            for k in hashMap:               # loop over the hash map
                if hashMap[k] == 1:         # check the first key with value as 1
                    return s.index(k)       # return the index of that key in s
        return -1                           # return -1 if no such value is found

mySol = Solution()
s = "leetcode"
print(mySol.firstUniqChar(s))