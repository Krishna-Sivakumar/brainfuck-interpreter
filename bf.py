import argparse

array = [0 for i in range(30)]
data_pointer = 0

file = open("input.bf", 'r').read()
program = "".join([x for x in file if x in '<>+-.,[]'])

loops = []

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
        array[data_pointer] += 1
    elif command == '-':
        # Decrement data at pointer
        array[data_pointer] -= 1
    elif command == '.':
        # Print data at pointer
        print(chr(array[data_pointer]), end='')
    elif command == ',':
        # Set data at pointer to input
        inp = input()
        # If input is a character, convert it to ASCII
        array[data_pointer] = int(inp) if not inp.isalpha() else ord(inp)
        pass
    elif command == '[':
        # Check if data at pointer is 0
        if array[data_pointer] == 0:
            # Skip to nearest closing bracket if data is 0
            while program[instruction] != ']':
                instruction += 1
        else:
            # Push index of the start of the loop so that it can be jumped back to later
            loops.append(instruction)
    elif command == ']':
        # Check if data at pointer is non-zero
        if array[data_pointer] != 0:
            # Jump to corresponding opening bracket
            instruction = loops[-1]
        else:
            # Pop index of the start of current loop, as it's over
            loops.pop()

    # Move on to the next instruction
    instruction += 1
