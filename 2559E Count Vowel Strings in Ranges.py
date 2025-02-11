'''You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.'''

class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        x = []
        n = len(queries)
        vowels = ['a', 'e', 'i', 'o', 'u']
        yes = []
        word_status = []
        # for i in range(0, n):
        #         li = queries[i][0]
        #         ri = queries[i][1]
        #         count = 0
        #         for word in words[li:ri+1]:
        #             if word[0] in vowels and word[-1] in vowels:
        #                 count += 1
        #                 # print(word, count)
        #         yes.append(count)
                # print()
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                word_status.append(1)
            else:
                word_status.append(0)
        prefix_Sum = [0] * (len(word_status) + 1)
        for i in range(1, len(prefix_Sum)):
            prefix_Sum[i] = prefix_Sum[i-1] + word_status[i-1]
        
        for li, ri in queries:
            count = prefix_Sum[ri+1] - prefix_Sum[li]
            yes.append(count)
        return yes

mySol = Solution()
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
print(mySol.vowelStrings(words, queries))