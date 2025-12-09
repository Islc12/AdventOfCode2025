clean_operators = []

with open('d6.csv', 'r') as file:
    rows = file.readlines()
    for row in rows:
        operators = row.strip().split()
        clean_operators.append(operators)

for row in rows[:-1]:
    row0 = rows[0].split()
    row1 = rows[1].split()
    row2 = rows[2].split()
    row3 = rows[3].split()

col_total = []
i = 0
for oper in operators:
    match oper:
        case '+':
            total = int(row0[i]) + int(row1[i]) + int(row2[i]) + int(row3[i])
            col_total.append(total)
        case '*':
            total = int(row0[i]) * int(row1[i]) * int(row2[i]) * int(row3[i])
            col_total.append(total)
        case _:
            print("Error")
            exit
    i += 1

total = 0
for nums in col_total:
    total += nums

print(total)