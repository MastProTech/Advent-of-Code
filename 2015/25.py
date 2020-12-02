def part_1(find_row, find_col):
    size=max(find_col, find_row)*2 # Because the table should be square (cols=rows) and half of the table is zero
    table=[[0 for i in range(size)] for i in range(size)] # Declaring table with zeros
    num=20151125 # Initial number
    for limit in range(0,size+1):
        for i in range(0, limit):
            row=limit-i
            col=i+1
            if row==find_row and col==find_col: # Required location found or not?
                print('Part 1: At location (',row,',',col,') :',num)
                return
            table[row-1][col-1]=num
            num=(num*252533)%33554393

part_1(find_row=2947, find_col=3029)
