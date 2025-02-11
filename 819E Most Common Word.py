'''Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.'''
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        x = re.sub(r'(?<=\S)[\W_](?=\s)', '', paragraph)
        p = x.split()
        dict1 = {}
        for i in p:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_dict)
        l = []
        for i in sorted_dict.keys():
            if i not in banned:
                l.append(i)
        print(l)
        return l[0]
    
mySol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mySol.mostCommonWord(paragraph.lower(), banned))

class Solution2:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Convert paragraph to lowercase
        paragraph = paragraph.lower()

        # Remove punctuation using regex and split the paragraph into words
        words = re.findall(r'\b\w+\b', paragraph)

        # Count the frequency of each word
        word_count = Counter(words)

        # Filter out the banned words and find the most frequent non-banned word
        max_word = ''
        max_count = 0
        
        for word, count in word_count.items():
            if word not in banned and count > max_count:
                max_word = word
                max_count = count
        
        return max_word