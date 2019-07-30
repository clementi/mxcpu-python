class CpuState(object):
    def __init__(self):
        self.cycles = 0
        self.counter = 0
        self.program_counter = 0
        self.accumulator = 0
        self.registers = 16 * [0]

    def __repr__(self):
        return f"Cycles    : {self.cycles}\n" \
               f"INC       : {self.counter}\n" \
               f"PC        : {self.program_counter}\n" \
               f"ACC       : {self.accumulator}\n" \
               f"Registers : {self.registers}"


def run(program, state):
    state.cycles += 1
    op_code = program[state.program_counter]
    
    if op_code == 0x00:
        return
    elif op_code == 0xB1:
        value = program[state.program_counter + 1]
        state.program_counter = value
    elif op_code == 0xB2:
        index = program[state.program_counter + 1]
        value = program[state.program_counter + 2]
        if state.accumulator == state.registers[index]:
            state.program_counter = value
        else:
            state.program_counter += 3
    elif op_code == 0xB3:
        value = program[state.program_counter + 1]
        pc_value = program[state.program_counter + 2]
        if state.accumulator == value:
            state.program_counter = pc_value
        else:
            state.program_counter += 3
    elif op_code == 0xC0:
        index = program[state.program_counter + 1]
        state.accumulator += state.registers[index]
        state.program_counter += 2
    elif op_code == 0xC1:
        value = program[state.program_counter + 1]
        state.accumulator += 1
        state.program_counter += 2
    elif op_code == 0xC2:
        state.counter += 1
        state.program_counter += 1
    elif op_code == 0xC3:
        state.counter -= 1
        state.program_counter += 1
    elif op_code == 0xC4:
        state.counter = 0
        state.program_counter += 1
    elif op_code == 0xC5:
        state.accumulator = state.counter
        state.program_counter += 1
    elif op_code == 0xC6:
        state.counter = state.accumulator
        state.program_counter += 1
    elif op_code == 0xD0:
        index = program[state.program_counter + 1]
        value = state.registers[index]
        state.accumulator = value
        state.program_counter += 2
    elif op_code == 0xD1:
        value = program[state.program_counter + 1]
        state.accumulator = value
        state.program_counter += 2
    elif op_code == 0xD2:
        index = program[state.program_counter + 1]
        state.registers[index] = state.accumulator
        state.program_counter += 2
    else:
        raise Exception(f"unknown instruction {op_code}")

    return run(program, state)
