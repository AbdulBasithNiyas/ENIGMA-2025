arr = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_set = set(num_list)
for i in range(9):
    row_arr = []
    row = input()
    for x in row:
        row_arr.append(int(x))
    arr.append(row_arr)

print(arr)

for r in arr:
    if set(r) != num_set:
        print('Invalid')
        exit()
    elif set(r) == num_set:
        double_sudoku_list = []
        for i in range(1, 7, 3):
            for j in range(1, 7, 3):
                double_sudoku_list.append(arr[i][j])
        print(double_sudoku_list)
