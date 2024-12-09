def generate_ops(n):
    ops_list = [None] * n
    
    def generate(n, ops_list, i, generated_list):
        if i == n:
            generated_list.append("".join(ops_list))
            return
    
        ops_list[i] = '0'
        generate(n, ops_list, i + 1, generated_list)
        
        ops_list[i] = '1'
        generate(n, ops_list, i + 1, generated_list)
        
        ops_list[i] = '2'
        generate(n, ops_list, i + 1, generated_list)
        
    generated_list = []
    generate(n, ops_list, 0, generated_list)    
    return generated_list

def is_valid(number, operands):
    ops = ['+', '*', '||']
    n = len(operands) - 1
    ops_list = generate_ops(n)

    for attempt in ops_list:
        ans = operands[0]
        for i in range(1, len(operands)):
            op = ops[int(attempt[i-1])]
            if op == '+':
                ans = ans + operands[i]
            elif op == '*':
                ans = ans * operands[i]
            elif op == '||':
                ans = int(str(ans) + str(operands[i]))
            
        if ans == number:
            return True
        
    return False

possible_count = 0
with open("./2024/day7.txt") as fp:
    for line in fp.readlines():
        
        number_raw, operands_raw = line.split(":")
        number = int(number_raw)
        operands = [int(x) for x in operands_raw.split()]

        if is_valid(number, operands):
            possible_count += number
            
print(possible_count)