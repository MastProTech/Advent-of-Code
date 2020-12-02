import re

def read_file(path):
    fh=open(str(path))
    text=str()
    for line in fh:
        text=text+line
    return text

def text_to_list(text:str):
    num_list=list()
    pattern=re.compile('[0-9]+')
    matches=pattern.finditer(text)
    for match in matches:
        num_list.append(int(match.group(0)))
    return num_list
