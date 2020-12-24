import argparse

array = [0 for i in range(30000)]
curr_pointer = 0

with open("input.bf", 'r') as f:
    for command in f.read():
        if command not in '<>+-.,[]':
            print(f'"{command}" is not a recognized command')
            exit()

        if command == '>':
            curr_pointer = (curr_pointer + 1) % 30000
        elif command == '<':
            curr_pointer = (curr_pointer - 1) % 30000
        elif command == '+':
            array[curr_pointer] += 1
        elif command == '-':
            array[curr_pointer] -= 1
        elif command == '.':
            print(array[curr_pointer], end='')
        elif command == ',':
            array[curr_pointer] = int(input())
        elif command == '[':
            pass
        elif command == ']':
            pass
