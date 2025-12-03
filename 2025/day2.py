invalid_product_ids = []
new_invalid_product_ids = []

with open("./2025/day2.txt", "r") as fp:
    line = fp.readline()
    
ranges = line.split(",")

for r in ranges:
    start, end = r.split("-")
    
    for product_id in range(int(start), int(end) + 1):
        digits = str(product_id)
        # solve for part 1, digits only repeat twice
        if len(digits) % 2 == 0:
            midpoint = len(digits) // 2
            left = digits[:midpoint]
            right = digits[midpoint:]
            if left == right:
                invalid_product_ids.append(int(digits))
        
        # solve for part 2, any repeating amount of digits
        for i in range(1, (len(digits) // 2) + 1):
            check = digits[:i] * (len(digits) // len(digits[:i]))
            if check == digits:
                new_invalid_product_ids.append(int(digits))
                break
                
print(f"Part 1 - {sum(invalid_product_ids)}")
print(f"Part 2 - {sum(new_invalid_product_ids)}")