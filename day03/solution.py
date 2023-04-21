# Initialize a dictionary of letters to priority numbers
priority_dict = {
    # Lowercase item types a through z have priorities 1 through 26
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 
    # Uppercase item types A through Z have priorities 27 through 52
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 
    'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}

sum = 0

# Open input file
with open("input.txt", "r") as file:
    # Iterate over whole file line by line
    for line in file:
        # Determine midpoint of line
        line_size = len(line)
        line_mid = line_size // 2
        # Assign each halfs to a new list
        left_half = line[:line_mid]
        right_half = line[line_mid:]
        # Iterate over each letter in the line
        for letter in left_half:
            if letter in right_half:
                # If duplicate is found, add item's priority to the sum
                sum += priority_dict[letter]
                break

print(sum)