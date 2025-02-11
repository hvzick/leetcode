'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.'''

class Solution:
    def sortSentence(self, s: str) -> str:
        r = []
        l= s.split()                        # convert string to list
        n = len(l)
        for i in range(0, n):               # iterate over the numbers
            for j in range(0, n):           # iterate over the words
                if str(i+1) in l[j]:        # check if current number + 1 is in current word
                    x = l[j]                # store the word in a variable
                    r.append(x[:-1])        # exclude the last letter of the word which is the sequence number 
        return " ".join(r)                  # convert the list back to the string and return it

mySol = Solution()
s = "is2 sentence4 This1 a3"
print(mySol.sortSentence(s)) 