c = 0 # Cycle 
x = 1 # x register
xpos = [0, 0 ,0] # Sprite position
crt = [] # CRT output
rc = 0 # Cycle relative to screen position

def assign(line):
    # Assign instructions form input file
    line_split = line.split()
    if len(line_split) == 2:
        cmd, num = line_split
        num = int(num)
    else:
        cmd, num = line_split[0], 0
    return cmd, num

def check():
    # Assign proper CRT row
    global crt, c, rc, xpos
    for i in range(1, 11):
        if c > 40 * i:
            rc = c - 40 * i
        elif c < 40:
            rc = c

    # Draw pixel  
    if rc in xpos:
        crt.append("#")
    else:
        crt.append(".")
    
def map(x)-> list:
    # Map sprite positions
    for i in range(3):
        xpos[i] = x + i
    return xpos

with open("input.txt", "r") as file:
    for line in file:
        cmd, num = assign(line)

        # Interpret instructions
        if cmd == "addx":
            for i in range(2):
                xpos = map(x)
                c += 1
                check()

            x += num
        else:
            xpos = map(x)
            c += 1
            check()

# Print CRT output
for i in range(0, len(crt), 40):
    print("".join(crt[i:i+40]))

print(f"Cycles: {c}")