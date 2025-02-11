'''You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.'''

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        n = len(ranges)
        l = list(range(left, right+1))                          # create a list with numbers ranging from left to right+1
        largest = max(max(sg) for sg in ranges)                 # find largest number in the list
        smallest = min(min(sk) for sk in ranges)                # find smallest number in the list
        if right > largest or left < smallest:                  # check if left and right are within largest and smallest numbers
            return False                                        # if not return false
        else:
            for i in range(left, right+1):                      # iterate of the numbers
                for j in range(0, n):                           # iterate over ranges
                    if ranges[j][0] <= i <= ranges[j][1]:       # if number is in the range remove it from the l
                        l.remove(i)
                        break                                   # break and move to next number
            if l:
                return False                                    # if l is not empty 
            else:                                               # if l is empty
                return True

mySol = Solution()
ranges = [[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]
left = 2
right = 5
print(mySol.isCovered(ranges, left, right))