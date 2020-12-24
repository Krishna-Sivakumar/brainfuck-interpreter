import argparse

array = [0 for i in range(30000)]
curr_pointer = 0

file = open("input.bf", 'r').read()
file = "".join([x for x in file if x in '<>+-.,[]'])

curr_command, max_len = 0, len(file)
loop_stack, skip_loop = [], False

while curr_command < max_len:
    command = file[curr_command]

    if skip_loop:
        skip_loop = file[curr_command] != ']'
        curr_command += 1
        continue

    if command == '>':
        curr_pointer = curr_pointer + 1
    elif command == '<':
        curr_pointer = curr_pointer - 1
    elif command == '+':
        array[curr_pointer] += 1
    elif command == '-':
        array[curr_pointer] -= 1
    elif command == '.':
        print(chr(array[curr_pointer]), end='')
    elif command == ',':
        array[curr_pointer] = int(input())
    elif command == '[':
        skip_loop = array[curr_pointer] == 0
        if not skip_loop:
            loop_stack.append(curr_command)
    elif command == ']':
        if array[curr_pointer] != 0:
            curr_command = loop_stack[-1] + 1
            continue
        else:
            loop_stack.pop()

    curr_command += 1
