import re

def read_file(path)->str:
    try:
        fh=open(str(path))
    except FileNotFoundError:
        print('Error:404, File Not Found. Exiting...')
        exit(404)
    text=str()
    for line in fh:
        text=text+line
    return text

def read_file_split_by_lines(path)->list:
    text=read_file(path)
    text_list=text.split('\n')
    return text_list