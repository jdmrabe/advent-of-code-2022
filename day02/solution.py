# Store corresponding points for round results
scoresTable = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}
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