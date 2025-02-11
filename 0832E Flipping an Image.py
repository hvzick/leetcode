'''Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].'''

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        matrix = []                                             # initialise a new list to store the new image
        l = len(image)                                          # calculate length of the image
        for i in range(0, l):                                   # loop over the rows of the image
            n = []                                              # initialise a new list to store the row values of the new image
            for j in range(l-1, -1, -1):                        # loop over each row in reverse from last index to -1
                if image[i][j] == 1:                            # check if current element at current index is 1
                    image[i][j] = 0                             # change current element to 0
                elif image[i][j] == 0:                          # check if current element at current index is 0
                    image[i][j] = 1                             # change current element to 1
                n.append(image[i][j])                           # append the element to the new list 
            matrix.append(n)                                    # append the row to the matrix list which is the new image
        return matrix                                           # return the matrix

mySol = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(mySol.flipAndInvertImage(image))

