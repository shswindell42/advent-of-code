input = open("./2024/day17.txt").readlines()

init_reg_a = int(input[0].strip().split(":")[1])
init_reg_b = int(input[1].strip().split(":")[1])
init_reg_c = int(input[2].strip().split(":")[1])
program = [int(o) for o in input[4].split(":")[1].strip().split(",")]
output = []

reg_a = init_reg_a
reg_b = init_reg_b
reg_c = init_reg_c


def decode_combo_operand(reg_a, reg_b, reg_c, operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c

def run_program(reg_a, reg_b, reg_c, program):
    output = [] 
    instruction_pointer = 0
    while instruction_pointer < len(program):
        step = 2
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]

        #print(f"Computing {opcode} {operand}")
        
        if opcode == 0:
            result = reg_a // (2 ** decode_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_a = result
        elif opcode == 1:
            result = reg_b ^ operand
            reg_b = result
        elif opcode == 2:
            reg_b = decode_combo_operand(reg_a, reg_b, reg_c, operand) % 8
        elif opcode == 3:
            if reg_a != 0:
                instruction_pointer = operand
                step = 0
        elif opcode == 4:
            result = reg_b ^ reg_c
            reg_b = result
        elif opcode == 5:
            result = decode_combo_operand(reg_a, reg_b, reg_c, operand) % 8
            output.append(result)
        elif opcode == 6:
            result = reg_a // (2 ** decode_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_b = result
        elif opcode == 7:
            result = reg_a // (2 ** decode_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_c = result

        instruction_pointer += step

        if output != program[:len(output)]:
            break
        
    return output

override = 0
output = []

# the magic number should be divisible by 8
# the number ends with 2da4e0
# the number has c21 then a b or d, try b
while output != program:
    override += 1
    reg_a =  (override << 40) | int("c21b2da4e0", 16) 
    output = run_program(reg_a, reg_b, reg_c, program)
    if len(output) >= 14:
        print(f"{reg_a} = {hex(reg_a)}-> {output}")


print(",".join([str(o) for o in output]))
print(reg_a)
