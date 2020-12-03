import re

def read_file(path):
    try:
        fh=open(str(path))
    except FileNotFoundError:
        print('Error:404, File Not Found. Exiting...')
        exit(404)
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
