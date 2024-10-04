move = input("Enter the move (e.g., e4): ")
column = move[0].lower()
row = int(move[1])

# Calculate the column number
num_col = ord(column) - ord('a') + 1

# Determine the color of the square
if (row + num_col) % 2 == 0:
    print("black")
else:
    print("white")

