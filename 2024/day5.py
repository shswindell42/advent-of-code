before_rules = {}
after_rules = {}
middle_sum = 0
incorrect_middle_sum = 0

with open("./2024/day5.txt", "r") as fp:
    while True:
        line = fp.readline()
        if line == "\n":
            break
        
        before, after = line.strip().split('|')
        if before_rules.get(after):
            before_rules.get(after).append(before)
        else:
            before_rules[after] = [before]
            
        if after_rules.get(before):
            after_rules.get(before).append(before)
        else:
            after_rules[before] = [after]
            
    
    # process lines against the rules
    line = fp.readline()
    while line:
        pages = line.strip().split(',')
        
        # check that the pages adhere to the rules
        valid = True
        i = 0
        while i < len(pages):
            reset = False
            page = pages[i]
            
            before_list = before_rules.get(page, [])
            after_pages = pages[i:]
            for ap in after_pages:
                if ap in before_list:
                    valid = False
                    # fix it!
                    pages.remove(ap)
                    pages.insert(i, ap)
                    i = 0
                    reset = True
            
            if reset:
                continue
                
            after_list = after_rules.get(page, [])
            before_pages = pages[:i]
            for bp in before_pages:
                if bp in after_list:
                    valid = False
                    # fix it!
                    pages.remove(bp)
                    pages.insert(i+1, bp)
                    i = 0
                    reset = True
                    
            if reset:
                continue

            i += 1
        
        if valid:
            # get the middle number
            middle_sum += int(pages[int(len(pages) / 2)])
        else:
            # fix the incorrect
            incorrect_middle_sum += int(pages[int(len(pages) / 2)])
            
        line = fp.readline()

print(middle_sum)
print(incorrect_middle_sum)