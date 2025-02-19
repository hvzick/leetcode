'''You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.'''

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        b = date.split("-")                     # split the list on every hyphen sign
        binaryDate = ''                         # initialise an empty string
        for i in b:                             # loop over the list of strings
            binaryDate += format(int(i), 'b')   # add binary to date to the string
            binaryDate += '-'                   # add hyphen sign after every date
        return binaryDate[:-1]                  # return all string except the last hyphen character

mySol = Solution()
date = "2080-02-29"
print(mySol.convertDateToBinary(date))