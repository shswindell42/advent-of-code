def det(m):
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    
    denom = (a * d) - (b * c)
    
    if denom == 0:
        return None
    
    return 1 / denom

def inverse(m):
    d = det(m)
    if not d:
        return None
    
    return [[d * m[1][1], d * (-1*m[0][1])]
            ,[d * (-1 * m[1][0]), d * m[0][0]]]
    
def matrix_mul(m, y):
    p = []
    for i in range(len(m)):
        r = []
        for j in range(len(y[0])):
            s = 0
            for k in range(len(m[i])):
                s += m[i][k] * y[k][j]
            r.append(s)
        p.append(r)
        
    return p

cost = [3, 1]
total_cost = 0

with open("./2024/day13.txt") as fp:
    for line in fp:
        if line.startswith("Button A"):
            button_a = [int(i.split('+')[1].strip()) for i in line.split(':')[1].split(',')]
        elif line.startswith("Button B"):
            button_b = [int(i.split('+')[1].strip()) for i in line.split(':')[1].split(',')]
        elif line.startswith("Prize"):
            prize = [[int(i.split('=')[1].strip()) + 10000000000000] for i in line.split(':')[1].split(',')]

            # calculate the tokens needed to get the prize
            m = [[button_a[0], button_b[0]],
                 [button_a[1], button_b[1]]]
            m_i = inverse(m)
            if m_i:
                plays = matrix_mul(m_i, prize)

                valid = True
                for c in plays:
                    if abs(c[0] - round(c[0])) > 0.0001:
                        valid = False
                
                if valid:
                    for i, c in enumerate(plays):
                        total_cost += c[0] * cost[i]
                    
print(int(total_cost))
        
