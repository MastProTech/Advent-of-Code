from runner import read_file_split_by_lines

def part1(command_list:list)->int:
    accumulator=0
    visited=list()
    i=0
    while True:
        if i not in visited:
            visited.append(i)
            input=command_list[i]
            if input[:3] == 'acc':
                val=int(input[3:])
                accumulator+=val
                i+=1
            elif input[:3] == 'jmp':
                val=int(input[3:])
                i+=val
            else:
                i+=1
        else:
            print('Cycle Detected')
            break
    return accumulator

command_list=read_file_split_by_lines('08.txt')
print('Part 1: Done by Myself:', part1(command_list))

# Copied Code. Source: Reddit I forgot to copy the link... :(

instructions = []
with open('08.txt') as fp:
  line = fp.readline()
  while line:
    tokens = line.strip().split()
    instructions.append((tokens[0], int(tokens[1])))
    line = fp.readline()

def execute(instrs):
  hasLoop = False
  visited = set()
  ptr = acc = 0
  while ptr < len(instrs):
    op, value = instrs[ptr]
    if ptr in visited:
      hasLoop = True
      break
    visited.add(ptr)
    if op == 'jmp':
      ptr = ptr + value
      continue
    elif op == 'acc':
      acc = acc + value
    ptr = ptr + 1
  return (acc, hasLoop)

print(f'Part 1\n{execute(instructions)[0]}\n')

swapDict = {'nop':'jmp','jmp':'nop'}
for i, (op,value) in enumerate(instructions):
  if op == 'nop' or op == 'jmp':
    swappedOp = [(swapDict[op], value)]
    newInstructions = instructions[:i] + swappedOp + instructions[i+1:]
    accValue, hasLoop = execute(newInstructions)
    if not hasLoop:
      print(f'Part 2\n{accValue}')