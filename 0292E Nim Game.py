'''You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.'''

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:          # if n is muktiple of 4, the first player will always lose
            return False
        else:                   # if n is not multiple of 4, the first player will always win
            return True

mySol = Solution()
n1 = 4
n2 = 3
print(mySol.canWinNim(n1))
print(mySol.canWinNim(n2))