'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        word = []                           # inirialise an empty list
        for i in range(0, len(address)):    # loop over the IP address
            if address[i] == '.':           # if current element is .
                word.append('[.]')          # add [.] to the list
            else:
                word.append(address[i])     # add whatever is present at that index
        return ''.join(word)                # convert the list to the string and return it
        
mySol = Solution()
address = "1.1.1.1"
print(mySol.defangIPaddr(address))