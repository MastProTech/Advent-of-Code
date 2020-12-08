'''
This challenge might have confusion in part 2. Well here the explanation:
1. In part 1, I've made list of all people who're seated on their seats.
2. You haven't sat down, so only your seat is missing from your list. (Because your seat is empty right now)
3. You'll have to find that Seat ID.

Proceedure that I followed:
Observe the pattern:
    The first seat i.e. Seat ID at seat[0] is 6, seat[1] is 7, seat[2] is 8... and so on. (Pattern: seat[i]=i+6)
    Now there will be somewhere in the list where this pattern will break. Means somewhere, seat[i]!=i+6. 
    Find that ID and return it.

''' 
from runner import read_file_split_by_lines

def decode_seat_id(text:str)->int:
    text=text.replace('F','0')
    text=text.replace('B','1')
    text=text.replace('L', '0')
    text=text.replace('R', '1')
    row=text[:-3]
    col=text[-3:]
    return int(row, 2)*8+int(col, 2)

def part1(seat_list_decoded:list)->int:
    return max(seat_list_decoded)

def part2(seat_list_decoded:list, start_id:int)->int:
    sorted_seats=sorted(seat_list_decoded)
    my_seat = next(i + sorted_seats[0] for i in range(len(sorted_seats)) if sorted_seats[i] != i + sorted_seats[0])
    # If above line is confusing, try running just the for loop section in your mind (or IDE), Google about next function etc.
    return my_seat

seat_list=read_file_split_by_lines('05.txt')
seat_list_decoded=list(map(decode_seat_id, seat_list))
p1=part1(seat_list_decoded)
print('Part 1: Highest Seat ID on boarding pass', p1)
print('Part 2: My Seat ID', part2(seat_list_decoded, start_id=p1))