'''You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.'''

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        hashMap1 = {}                                   # initialise an empty dictionary
        seen = []                                       # initialise an empty list
        i = 0                                           # initialise i to keep track of indicies
        j = 97                                          # initialise j to keep track of ASCII number
        decodedMessage = ''                             # initialise this variable to store the final decoded message
        while True:
            if len(hashMap1) == 26:                     # if true, that means all alphabets have been added to the hash map and we have reached the end
                break
            if key[i] not in seen:                      # we have to add each element at its first occurance only only
                seen.append(key[i])                     # add the current element to seen
                hashMap1[key[i]] = chr(j)               # add string keys element as key and alphabets starting froma to z z as values in the hash map
                j += 1                                  # every time we add an alphabet, increment this counter to add next alphabet in next iteration
            i += 1                                      # in crement the counter to increment the index of key
        for i in range(0, len(message)):                # loop over the length of message
            if message[i] == ' ':                       # if current character is ' ' then it means ther is space in decoded message
                decodedMessage += ' '                   # add space to the decoded message
            else:
                decodedMessage += hashMap1[message[i]]  # add value of dictionary at current element of message
        return decodedMessage                           # return the decoded message

mySol = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(mySol.decodeMessage(key, message))