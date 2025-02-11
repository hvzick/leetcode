def checkStraightLine(coordinates):
    for i in range(0, len(coordinates)-1):
        #print(f'{coordinates[i][0]+1} == {coordinates[i+1][0]} and {coordinates[i][1]+ 1} == {coordinates[i+1][1] }')
        if len(coordinates) == 2 and coordinates[i][0] + 1 == coordinates[i+1][0]:
            return True

        if coordinates[i][0] + 1 == coordinates[i+1][0]:
            if coordinates[i-1][1] + 1 == coordinates[i][1]:
                x = True
        else:
            return False
    return x



coordinates = [[1,2],[2,3]]
print(checkStraightLine(coordinates))