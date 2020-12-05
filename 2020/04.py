import re
from runner import read_file

def extract_keys_values(text:str)->list: # Seperates each passport, and then each passport's keys and values
    t_list=re.split('\n{2}', text)
    t_list=list(map(str.split, t_list))
    output=list() 
    for i in range(len(t_list)):
        output.append([])
        for j in range(len(t_list[i])):
            output[i].append(t_list[i][j].split(':'))
        output[i]=dict(output[i])
    return output

def return_passport_validity_part1(l:list)->bool:
    i=l.keys()
    if 'ecl' in i and 'pid' in i and 'eyr' in i and 'hcl' in i and 'byr' in i and 'iyr' in i and 'hgt' in i:
        return True
    return False

def verify(key:str, val:str)->bool: # Verifies if keys are assigned valid values or not
    if key=='byr':
        if int(val)>=1920 and int(val)<=2002:
            return True
    elif key=='iyr':
        if int(val)>=2010 and int(val)<=2020:
            return True
    elif key=='eyr':
        if int(val)>=2020 and int(val)<=2030:
            return True
    elif key=='hgt':
        if val[-2:]=='cm':
            if int(val[:-2])>=150 and int(val[:-2])<=193:
                return True
        elif val[-2:]=='in':
            if int(val[:-2])>=59 and int(val[:-2])<=76:
                return True
    elif key=='hcl':
        match=re.match('^#[0-9a-f]{6}$', val)
        if match is not None:
            return True
    elif key=='ecl':
        ecl=['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if val in ecl:
            return True
    elif key=='pid':
        match=re.match('^[0-9]{9}$', val)
        if match is not None:
            return True
    return False

def return_passport_validity_part2(l:list)->bool:
    i=l.keys()
    if (
        ('byr' in i and verify('byr', l['byr'])) and
        ('iyr' in i and verify('iyr', l['iyr'])) and
        ('eyr' in i and verify('eyr', l['eyr'])) and
        ('hgt' in i and verify('hgt', l['hgt'])) and
        ('hcl' in i and verify('hcl', l['hcl'])) and
        ('ecl' in i and verify('ecl', l['ecl'])) and
        ('pid' in i and verify('pid', l['pid']))):
        return True
    return False

def clone_part2(l:list)->bool: # NOTE: Copied code of this function. Source: https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gemhjlu/
    valid=False
    fields_required={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    field_pattern = {'byr': '(^(19)[2-9][0-9]$)|(^(200)[0-2]$)',
                     'iyr': '(^(201)[0-9]$)|(^(2020)$)',
                     'eyr': '(^(202)[0-9]$)|(^(2030)$)',
                     'hgt': '(^((1[5-8][0-9])|((19)[0-3]))cm$)|(^((59)|(6[0-9])|(7[0-6]))in$)',
                     'hcl': '^#[0-9a-f]{6}$',
                     'ecl': '(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)',
                     'pid': '^[0-9]{9}$',
                     'cid': '(.*?)'}
    if fields_required.issubset(l.keys()):
        valid=True
        for key in l.keys():
            valid=valid and bool(re.match(field_pattern[key], l[key]))
    return valid

if __name__=='__main__':
    text=read_file('04.txt')
    output=extract_keys_values(text)
    print('Total Passports:',len(output))
    print('Part 1: Valid Passports:',list(map(return_passport_validity_part1, output)).count(True))
    print('Part 2: Valid Passports:',list(map(return_passport_validity_part2, output)).count(True))
    print('Part 2: (Using another function):',list(map(clone_part2, output)).count(True)) # One of the best solutions I found on the internet. ♥ Source: https://www.reddit.com/r/adventofcode/comments/k6e8sw/2020_day_04_solutions/gemhjlu/