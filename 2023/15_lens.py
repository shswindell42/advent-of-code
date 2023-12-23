import re
from dataclasses import dataclass

@dataclass
class Lense:
    label: str
    focal_length: int

def hash(operation: str) -> int:
    current_value = 0
    for ascii_code in list(operation.encode('ascii')):
        current_value += ascii_code
        current_value = (current_value * 17) % 256
    return current_value


with open('./day15.txt', 'r') as fp:
    operations = fp.readline().split(',')

total = sum([hash(operation) for operation in operations])

print(f"Verifcation total: {total}")


boxes = {}
for operation in operations:
    # parse the label, operation, and focal length
    op_parts = re.search(r"([a-z]+)([-=])(\d*)", operation)
    label, op_code = op_parts.group(1), op_parts.group(2)

    label_hash = hash(label)

    box = boxes.get(label_hash)
    if op_code == '-':
        if box:
            for lense in box:
                if lense.label == label:
                    box.remove(lense)

    else:
        focal_length = int(op_parts.group(3))
        new_lense = Lense(label, focal_length)
        if box:
            if new_lense.label in [l.label for l in box]:
                for lense in box:
                    if lense.label == label:
                        lense.focal_length = focal_length
            else:
                box.append(new_lense)
        else:
            boxes[label_hash] = [new_lense]

focus_power = 0
for box_number, box in boxes.items():
    for slot, lense in enumerate(box):
        # print(f"{lense.label}: {box_number + 1} * {slot + 1} * {lense.focal_length}")
        focus_power += (box_number + 1) * (slot + 1) * lense.focal_length

print(focus_power)