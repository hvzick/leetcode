'''International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
'''
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]  # list of values of alphabets in morse code 0 = 'a' to 25 = 'z'
        j = 97                                                  # j = starting number of ASCII value of 'a'
        hashMap = {}                                            # initialise a dictionary
        for i in range(0, 26):                                  # loop over all alphabets
            hashMap[chr(j)] = morseCodes[i]                     # fill dictionary with key as alphabet and value as its morse code value
            j += 1                                              # increment j to change ASCII value of alphabets in each iteration
        codeWords = []                                          # initialise an empty list 
        for i in words:                                         # loop over words
            temp = ''                                           # initialise a temporary string
            for j in i:                                         # loop over each alphabet in the word
                temp += hashMap[j]                              # add morse value at current alphabet in hashmap to the temp string
            codeWords.append(temp)                              # append the string to the list
        transformations = len(set(codeWords))                   # convert the list to set and check its length, its length would be the number of different and unique transformations among all words 
        return transformations                                  # return the transformations

mySol = Solution()
words = ["gin","zen","gig","msg"]
print(mySol.uniqueMorseRepresentations(words))