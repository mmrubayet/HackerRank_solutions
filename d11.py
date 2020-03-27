arr = []
for _ in range(6):
    tmp = [int(x) for x in str(input()).split(" ")]
    arr.append(tmp)

maximum = -9 * 7
for row in range(len(arr) - 2):
	for column in range(len(arr[row]) - 2):
		tl = arr[row][column]
		tc = arr[row][column + 1]
		tr = arr[row][column + 2]
		mc = arr[row + 1][column + 1]
		bl = arr[row + 2][column]
		bc = arr[row + 2][column + 1]
		br = arr[row + 2][column + 2]
		s = tl + tc + tr + mc + bl + bc + br
		maximum = max(s, maximum)

print(maximum)
