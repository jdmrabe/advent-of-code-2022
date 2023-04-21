# Store corresponding points for round results
#| A - ROCK     | X - LOSS
#| B - PAPER    | Y - DRAW
#| C - SCISSORS | Z - WIN
scoresTable = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
score = 0
    
# Open the input file
with open("input.txt", "r") as file:
    # Iterate each line for whole file
    for line in file:
        # Use each line as a key in scoresTable
        key = line.strip().replace(" ","")
        if key in scoresTable:
            score += scoresTable[key]
print(score)