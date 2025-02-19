'''There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.'''
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        hashMap = {}                                                # initialise an empty dictionary
        for i in range(0, len(score)):                              # loop over the rows of score list
            hashMap[score[i][k]] = score[i]                         # add value at ith row and jth column of score list as key to the hash map and the whole row as its value
        hashMap = dict(sorted(hashMap.items(), reverse=True))       # sort the hash map on basis of keys, convert it back to dictionary
        i = 0
        for key, values in hashMap.items():
            score[i] = values                                       # replace the values with sorted values
            i += 1                                                  # increment the index of the score list
        return score                                                # return new score list

mySol = Solution()
score = [   [10,6,9,1],
            [7,5,11,2],
            [4,8,3,15]   ]
k = 2
print(mySol.sortTheStudents(score, k))