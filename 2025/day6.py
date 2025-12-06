from functools import reduce
params = []
with open("./2025/day6.txt", "r") as fp:
    for line in fp.readlines():
        params.append(line.strip().split())

total = 0
for i in range(len(params[0])):
    values = []
    for v in range(len(params)):
        value = params[v][i]
        if value == "+":
            total += sum(values)
        elif value == "*":
            total += reduce(lambda a, x: a * x, values)
        else:
            values.append(int(value))

print(total)

# repull the data for part 2
with open("./2025/day6.txt", "r") as fp:
    data = [line.removesuffix("\n") for line in fp.readlines()]

# transpose the data for cephalopod math
transposed_data = ["" for _ in range(len(data[0]))]
for i in range(len(data)-1):
    for j in range(len(data[0])):
        transposed_data[j] = transposed_data[j] + data[i][j]
transposed_data.append("")

# convert to numbers, group into lists and add the operator
cephalopod_data = []
row = []
operations = data[-1].strip().split()
operator_index = 0
for x in transposed_data:
    value = x.strip()
    if value == "":
        row.append(operations[operator_index])
        cephalopod_data.append(row)
        row = []
        operator_index += 1
    else: 
        row.append(value)

# process similar to how part 1 went
# this code could be refactored, so it's not repeated
total = 0
for i in range(len(cephalopod_data)):
    values = []
    for v in range(len(cephalopod_data[i])):
        value = cephalopod_data[i][v]
        if value == "+":
            total += sum(values)
        elif value == "*":
            total += reduce(lambda a, x: a * x, values)
        else:
            values.append(int(value))
print(total)