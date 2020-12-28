#!/usr/bin/env pypy3
from sys import stdout, stdin

array = [0 for i in range(30000)]
data_pointer = 0

file = open("input.bf", 'r').read()
program = "".join([x for x in file if x in '<>+-.,[]'])

# Setting up a dictionary for loop jumping
loops = []
loopdict = {}

for instruction, command in enumerate(program):
    if command == '[':
        loops.append(instruction)
    elif command == ']':
        opening = loops.pop()
        loopdict[opening], loopdict[instruction] = instruction, opening

instruction = 0

while instruction < len(program):
    command = program[instruction]

    if command == '>':
        # Move data pointer to the right
        data_pointer += 1
    elif command == '<':
        # Move data pointer to the left
        data_pointer -= 1
    elif command == '+':
        # Increment data at pointer
        array[data_pointer] = (array[data_pointer] + 1) % 2 ** 8
    elif command == '-':
        # Decrement data at pointer
        array[data_pointer] = (array[data_pointer] - 1) % 2 ** 8
    elif command == '.':
        # Print data at pointer
        # print(chr(array[data_pointer]))
        stdout.write(chr(array[data_pointer]))
    elif command == ',':
        # Set data at pointer to input
        inp = stdin.read(1).rstrip()
        # If input is a character, convert it to ASCII
        if len(inp) > 0:
            array[data_pointer] = int(inp) if not inp.isalpha() else ord(inp)
    elif command == '[':
        # Check if data at pointer is 0
        if array[data_pointer] == 0:
            # Skip to nearest closing bracket if data is 0
            instruction = loopdict[instruction]
    elif command == ']':
        # Check if data at pointer is non-zero
        if array[data_pointer] > 0:
            # Jump to corresponding opening bracket
            instruction = loopdict[instruction]

    # Move on to the next instruction
    instruction += 1
