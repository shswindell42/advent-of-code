from dataclasses import dataclass
import queue

import numpy as np
from scipy.optimize import LinearConstraint, milp


@dataclass
class Manual:
    lights: tuple[bool]
    buttons: list[tuple[int]]
    joltage: list[int]

def parse_lights(lights):
    return tuple([True if x == '#' else False for x in lights])

manuals = []
with open("./2025/day10.txt", "r") as fp:
    for line in fp.readlines():
        parts = line.strip().split(' ')
        lights = parse_lights(parts[0].replace('[', '').replace(']', ''))
        buttons = [tuple([int(y) for y in x.removeprefix('(').removesuffix(')').split(",")]) for x in parts[1:len(parts) - 1]]
        joltage = [int(x) for x in parts[-1].removeprefix('{').removesuffix('}').split(',')]
        manual = Manual(lights, buttons, joltage)
        manuals.append(manual)

button_lengths = []
for manual in manuals:
    known_states = set() 
    start_state = tuple([False]) * len(manual.lights)
    buttons_presses = queue.Queue()
    for b in manual.buttons:
        buttons_presses.put([b])

    while buttons_presses:
        buttons = buttons_presses.get()
        
        state = list(start_state)
        for button in buttons:
            for b in button:
                state[b] = not state[b]
        
        state = tuple(state)
        
        if state == manual.lights:
            button_lengths.append(len(buttons))
            break
        
        if state not in known_states:
            known_states.add(state)
            
            # add neighbors
            for b in manual.buttons:
                buttons_presses.put(buttons + [b])

print(sum(button_lengths))

# solution for part 2
joltage_button_press_counts = []
for manual in manuals:
    c = np.ones(len(manual.buttons))
    button_bits = []
    for button in manual.buttons:
        bits = [0] * len(manual.joltage)
        for b in button:
            bits[b] = 1
        button_bits.append(bits)
        
    A = np.array(button_bits).transpose()

    bound = np.array(manual.joltage)
    constraints = LinearConstraint(A, lb=bound, ub=bound)
    integrality = np.full_like(c, True)

    res = milp(c=c, constraints=constraints, integrality=integrality)
    joltage_button_press_counts.append(sum(res.x))

print(sum(joltage_button_press_counts))