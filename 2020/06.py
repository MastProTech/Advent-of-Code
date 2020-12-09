import re

def read_file(path='06.txt')->list:
    fh=open(path)
    text=str()
    for line in fh:
        text=text+line
    return text.split('\n\n')
    
def part1(l:list):
    count=0
    for i in l:
        questions=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for j in questions:
            if i.find(j)!=-1:
                count+=1
    return count

def part2(l:list):
    count=0
    for i in l:
        questions=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for j in questions:
            # Each \n indicates a new person. So, I count('\n')+1=count(persons)
            # Plus, for each letter, check number of repetitions of that letter and compare it with no. of persons in that group.
            if len(re.findall(j, i))==(len(re.findall('\n', i))+1):
                count+=1
    return count

answers=read_file('06.txt')
print('Part 1: Number of Questions answered YES:', part1(answers))
print('Part 2: Number of Questions everyone in group answered YES:',part2(answers))