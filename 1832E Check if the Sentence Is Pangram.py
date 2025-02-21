'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashMap = {}                            # initialise a dictionary
        j = 97                                  # j = starting number of ASCII value of 'a'
        for i in range(0, 26):                  # loop over all alphabets 
            hashMap[chr(j)] = 0                 # fill dictionary with key as alphabet and value = 0
            j += 1                              # increment j to change ASCII value of alphabets in each iteration
        for i in range(0, len(sentence)):       # loop over each character of sentence
            if sentence[i] in hashMap.keys():   # check if current character is already is key of hashmap
                hashMap[sentence[i]] += 1       # increment its value
        if sum(hashMap.values()) >= 26:         # if sum of value values of hashmap is greater or equal to 26
            if 0 not in list(hashMap.values()): # if 0 is not in values of hashmap, which means every alphabet from a to z is present
                return True                     # return true
            else:                               # if 0 is in values of hashmap, which means not every alphabet from a to z is present
                return False                    # return false
        else:                                   # if sum is < 26
            return False                        # return false
        ''' OR 
        return len(set(sentence)) == 26
        '''

mySol = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(mySol.checkIfPangram(sentence))