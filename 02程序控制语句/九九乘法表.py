row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d " % (col, row, row*col), end=" ")
        col += 1
        pass
    row += 1
    print()
    pass
