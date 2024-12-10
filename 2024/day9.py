def print_disk(disk):
    for b in disk:
        print(b, end="")
    print("")
    
def blockwise_fragment(disk):
    front_index = 0
    back_index = len(disk) - 1

    while front_index < back_index:
        if disk[front_index] == '.' and disk[back_index] != '.':
            disk[front_index] = disk[back_index]
            disk[back_index] = '.'
            back_index -= 1
            front_index += 1
        elif disk[front_index] != '.' and disk[back_index] != '.':
            front_index += 1
        elif disk[front_index] == '.' and disk[back_index] == '.':
            back_index -= 1
        elif disk[front_index] != '.' and disk[back_index] == '.':
            back_index -= 1
            front_index += 1
            
def filewise_fragment(disk, file_size_map):
    for file_index in reversed(file_size_map.keys()):
        size, start, end = file_size_map[file_index]
        empty_file = ['.'] * size
        for i in range(len(disk)):
            if i >= start:
                break
            if disk[i:i+size] == empty_file:
                disk[i:i+size] = disk[start:end]
                disk[start:end] = empty_file
                break
        

with open("./2024/day9.txt") as fp:
    disk_map = fp.readline().strip()
    
on_file = True
file_index = 0
file_size_map = {}
disk = []
for s in disk_map:
    if on_file:
        file = [str(file_index)] * int(s)
        file_start = len(disk)
        disk.extend(file)
        file_size_map[file_index] = (int(s), file_start, len(disk))
        
        file_index += 1
    else:
        empty_file = ['.'] * int(s)
        disk.extend(empty_file)
    
    on_file = not on_file
    

filewise_fragment(disk, file_size_map)

# calculate the "checksum"
checksum = 0
for i, f in enumerate(disk):
    if f != '.':
        checksum += i * int(f)
    
print(checksum)