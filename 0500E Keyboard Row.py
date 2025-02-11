class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = 'qwertyuiopQWERTYUIOP'
        second = 'asdfghjklASDFGHJKL'
        third = 'zxcvbnmZXCVBNM'
        counter1 = 0
        counter2 = 0
        counter3 = 0
        result = []
        for i in words:
            for j in i:
                if j in first:
                    # print(f'j in 1')
                    counter1 += 1
                elif j in second:
                    # print(f'j in 2')
                    counter2 += 1
                elif j in third:
                    # print(f'j in 3')
                    counter3 += 1
                
            
            # print(f'len of {i} is {len(i)}')
            # print(counter1,counter2,counter3)
            # print()
            if counter1 == len(i):
                result.append(i)
            elif counter2 == len(i):
                result.append(i)
            elif counter3 == len(i):
                result.append(i)
            counter1 = counter2 = counter3 = 0
        return result



mySol = Solution()
words = ["Hello","Alaska","Dad","Peace"]
word = ["adsdf","sfd"]
print(mySol.findWords(words))
print(mySol.findWords(word))