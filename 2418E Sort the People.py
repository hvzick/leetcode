'''You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.'''

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        hashMap = {}                                            # initialise a dictionary
        for i in range(0, len(names)):                          # loop over the names
            hashMap[heights[i]] = names[i]                      # add height at ith index as key and names at ith index as value
        hashMap = dict(sorted(hashMap.items(), reverse=True))   # sort the hashmap on basis of key in reverse order
        return list(hashMap.values())                           # convert values of hashmap to list and return them

mySol = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(mySol.sortPeople(names, heights))