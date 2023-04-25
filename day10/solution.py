cycle = 0
x = 1 # Register
ss = 0 # Signal Strength
cyc_list = [20, 60, 100, 140, 180, 220]

def count():
    global cycle, ss
    if cmd == "addx":
        for i in range(2):
            cycle += 1
            if cycle in cyc_list:
                ss += cycle * x
    else:
        cycle += 1
        if cycle in cyc_list:
            ss += cycle * x

if __name__ == "__main__":

    with open("input.txt", "r") as file:
        for line in file:

            if len(line.split()) == 2:
                cmd, num = line.split()[0], int(line.split()[1])
            else:
                cmd = line.split()[0]
                num = 0

            if cmd == "addx":
                count()
                x += num
            else:
                count()

    print(ss)

