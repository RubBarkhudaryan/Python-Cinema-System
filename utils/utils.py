
def	print_seat(i, j, seat):
	if seat:
		if (i >= 9 and j < 9):
			print(f"\033[32m| {i + 1}-{j + 1}|\033[0m", end="  ")
		elif i >= 9 and j >= 9:
			print(f"\033[32m| {i + 1}-{j + 1}|\033[0m", end="  ")
		else:
			print(f"\033[32m| {i + 1}-{j + 1} |\033[0m", end="  ")
	else:
		if (i >= 9 or j >= 9):
			print(f"\033[31m| {i + 1}-{j + 1}|\033[0m", end="  ")
		elif i >= 9 and j >= 9:
			print(f"\033[31m| {i + 1}-{j + 1}|\033[0m", end="  ")
		else:
			print(f"\033[31m| {i + 1}-{j + 1} |\033[0m", end="  ")