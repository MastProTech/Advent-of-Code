import re
def read_file(file:str('03.txt')):
    try:
        fh=open(file)
    except FileNotFoundError:
        print('File Not Found. Exiting...')
        exit(1)
    line_list=list()
    for line in fh:
        line_sp=re.split('|\n', line) # Splitting each line character by character into a list
        line_sp=[i for i in line_sp if i!='' and i!=None] # For removing empty enteries in list
        line_list.append(line_sp)
    return line_list

def count_trees(start:tuple((0,0)), right:int, down:int, line_list:list):
    row, col=start # NOTE: Even if start is out of range, it will be adjusted as col=col%len(line_list[0])
    count=0
    while True:
        row=row+down
        if row>=len(line_list):
            break # Break when reached at the bottom of line_list
        col=(col+right)%len(line_list[0])
        if line_list[row][col]=='#':
            count=count+1
    print('Right',right,'Down',down,':',count)
    return count

line_list=read_file('03.txt')
r1d1=count_trees(start=(0,0), right=1, down=1, line_list=line_list)
r3d1=count_trees(start=(0,0), right=3, down=1, line_list=line_list)
r5d1=count_trees(start=(0,0), right=5, down=1, line_list=line_list)
r7d1=count_trees(start=(0,0), right=7, down=1, line_list=line_list)
r1d2=count_trees(start=(0,0), right=1, down=2, line_list=line_list)
total=r1d1*r3d1*r5d1*r7d1*r1d2
print('Total=',total)