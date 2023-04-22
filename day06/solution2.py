# Open file
with open("input.txt", "r") as file:
    for line in file:
        for i in range(len(line)):
            # Start interation from 13th character
            if i > 13:
                my_list = line[i - 14:i]
                # If there are no duplicates in the recent fourteen characters, print fourteenth character
                if len(my_list) == len(set(my_list)):
                    print(i)
                    break