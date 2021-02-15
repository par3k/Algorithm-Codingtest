input_data = input()

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

knight_steps = {
    (-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)
}

ans = 0

for step in knight_steps:
    n_row = row + step[0]
    n_col = col + step[1]

    if n_row >= 1 and n_row <= 8 and n_col >= 1 and n_col<= 8:
        ans +=1
print(ans)