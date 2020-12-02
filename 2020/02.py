from runner import read_file
import re

def part_1(text):
    count=0
    for i in range(0,len(text), 4):
        start, end, ch, inp=(int(text[i+0]), int(text[i+1]), text[i+2], text[i+3])
        match_list=re.findall(ch, inp)
        if len(match_list) >=start and len(match_list)<=end:
            count=count+1
    print('Part 1: Total Valid:', count)
    
def part_2(text):
    count=0
    for i in range(0,len(text), 4):
        first, second, ch, inp=(int(text[i+0]), int(text[i+1]), text[i+2], text[i+3])
        match_list=re.findall(ch, inp)
        if (inp[first-1]==ch or inp[second-1]==ch) and inp[first-1]!=inp[second-1]:
            count=count+1
    print('Part 2: Total Valid:', count)

text=read_file('02.txt')

text=re.split('-| |:|\n', text)
text=[i for i in text if i !='' and i != None] # To remove blank entries in text
part_1(text)
part_2(text)