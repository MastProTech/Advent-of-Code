from runner import read_file
import re

def text_to_list(text:str)->list:
    num_list=list()
    pattern=re.compile('[0-9]+')
    matches=pattern.finditer(text)
    for match in matches:
        num_list.append(int(match.group(0)))
    return num_list

def part1(num_list:list, target:int):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            sum=num_list[i]+num_list[j]
            if sum==target:
                mul=num_list[i]*num_list[j]
                print('YES',i, 'and', j, 'mul:',mul)

def part2(num_list:list, target:int):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                sum=num_list[i]+num_list[j]+num_list[k]
                if sum==target:
                    mul=num_list[i]*num_list[j]*num_list[k]
                    print('YES',i, 'and', j, 'k', k, 'mul:',mul)

text=read_file('01.txt')
num_list=text_to_list(text)
part1(num_list, 2020)
part2(num_list, 2020)