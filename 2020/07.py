# from runner import read_file_split_by_lines
# import re
# import time

# def foo(bags, target='shiny gold'):
#     lst=[i for i in bags.keys() if target in bags[i]]
#     if lst==[]:
#         return None
#     for i in range(len(lst)):
#         out=foo(bags, lst[i])
#         if out is not None and not set(out).issubset(set(lst)):
#             lst.extend(out)
#     return lst


# def fool(bags, target='shiny gold'):
#     print('target', target)
#     lst=[i for i in bags.keys() if target in bags[i]]
#     time.sleep(1)
#     print('1', lst)
#     if lst==[]:
#         return None
#     for i in range(len(lst)):
#         print('2', lst[i])
#         out=foo(bags, lst[i])
#         print('out', out)
#         if out is not None and not set(out).issubset(set(lst)):
#             lst.extend(out)
#             print(lst)
#             print('extended return')
#         else:
#             print('else None')
#     print('end return')
#     return lst
        

# text=read_file_split_by_lines('07.txt')
# bags=dict()
# for line in text:
#     pattern=re.compile('bags contain')
#     matchBag=pattern.search(line)
#     start=line[:matchBag.start()].rstrip()
#     if line[matchBag.end():]==' no other bags.':
#         bags.setdefault(start, [])
#     pattern2=re.compile('[0-9] [a-z ]+')
#     matches=pattern2.finditer(line)
#     for match in matches:
#         bags.setdefault(start, list())
#         index=match.group(0).find('bag')
#         end=match.group(0)[2:index].rstrip()
#         bags[start].append(end)


# for key in bags.keys():
#     print(key,':', bags[key])
# print()
# print(len(foo(bags)))


import re
with open('07.txt', 'r') as input:
    rules = [line.rstrip() for line in input]
bag_rules = {}
certain_parents = set()
maybe_parents = set()
never_parents = set()
for rule in rules:
    words = rule.split(' ')
    color = words[0] + ' ' + words[1]
    contents = re.findall(r'\d+ ([\w\s]+) bag',rule) # get all the colors in a bag
    print(contents)
    bag_rules.update({color : contents})
    if('shiny gold' in contents): # if shiny gold bag is in current bag, add it to certain parents
        certain_parents.add(color)
    elif contents==[]:  # if a bag has no other bags in it, directly add it to never parents
        never_parents.add(color)
    elif color!='shiny gold': # else add it to maybe parents
        maybe_parents.add(color)

while len(maybe_parents): # loop until there are maybe parents left
    for item in bag_rules.items():
        # check if current bag contains any certain parents, if yes remove it from maybe parent and add it to certain_parent
        if any([b in certain_parents for b in item[1]]):
            maybe_parents.discard(item[0])
            certain_parents.add(item[0])
        # if the current bag doesn't contain any parent bag, check if any of the bags in current bag are maybe parent. If none of them are maybe parent, current bag is obviously not a parent bag. remove it from maybe and add it to never parents.
        else:
            if not any([b in maybe_parents for b in item[1]]):
                maybe_parents.discard(item[0])
                never_parents.add(item[0])

print(len(certain_parents))