# Open file
with open("input.txt", "r") as file:
    for line in file:
        for i in range(len(line)):
            # Start interation from 4th character
            if i > 3:
                my_list = line[i - 4:i]
                # If there are no duplicates in the recent four characters, print fourth character
                if len(my_list) == len(set(my_list)):
                    print(i)
                    break