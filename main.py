from cpu import CpuState, run

import os
from sys import argv

def main():
    if len(argv) < 2:
        raise Exception("program file required")

    program = load_program(argv[1])

    state = CpuState()

    try:
        run(program, state)
        print(state)
    except Exception as e:
        print(e)


def load_program(path):
    with open(path, 'r') as program_file:
        contents = program_file.read().strip()
        return list(map(lambda byte: int(f"0x{byte}", 0), contents.split(' ')))


if __name__ == "__main__":
    main()