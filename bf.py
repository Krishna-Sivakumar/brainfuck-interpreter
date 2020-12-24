import argparse

commands = set(['<', '>', '+', '-', '.', ',', '[', ']'])

array = [0 for i in range(30000)]
curr_pointer = 0

with f as open("input.bf", 'r'):
    for command in f.read():
        if command not in commands:
            print(f'"{command}" is not a recognized command')
            exit()
