import csv
import math

# Used to hold data from a single line to multi line - not super neccessary but can help with readability
new_list = []

with open('day2.csv', mode='r') as file:
    file_data = csv.reader(file)
    for csv_data in file_data:
        for data in csv_data:
            # removes that pesky '-' character and gives us easier accessibility to our start and end ranges
            split_list = data.split('-')
            # pushes the data 
            new_list.append(split_list)

total = 0

for item in new_list:
    # pulls the start number
    start = int(item[0])
    # pulls the end number
    end = int(item[1])
    print(f'Start: {start}')
    print(f'End: {end}')

    # starts incrementing from start to end
    for i in range(start, end):
        # string conversion for string method use
        i_str = str(i)
        # pulls the length of the string for slicing, ensures the number is rounded up to 0 for small int ranges
        i_len = math.ceil(int(len(i_str) / 2))
        # passes over any data that we're unable to slice
        if i_len == 0:
            continue
        else:
            # finds the string from start to mid point and then concatenates it
            i_sliced = i_str[0:i_len]
            i_sliced += i_sliced
        # evaluates if it falls in the appropriate range and adds it to the total - plus verbose output
        if i == int(i_sliced):
            total += i
            print(f'Found one: {i}')

print(total)