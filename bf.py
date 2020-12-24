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
        data_pointer += 1
    elif command == '<':
        data_pointer -= 1
    elif command == '+':
        array[data_pointer] += 1
    elif command == '-':
        array[data_pointer] -= 1
    elif command == '.':
        print(chr(array[data_pointer]), end='')
    elif command == ',':
        inp = input()
        array[data_pointer] = int(inp) if not inp.isalpha() else ord(inp)
        pass
    elif command == '[':
        if array[data_pointer] == 0:
            while program[instruction] != ']':
                instruction += 1
        else:
            loops.append(instruction)
    elif command == ']':
        if array[data_pointer] != 0:
            instruction = loops[-1]
        else:
            loops.pop()

    instruction += 1
