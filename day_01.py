# --- Day 1: Not Quite Lisp ---

def floor_count(data):
	floor = 0
	position = 0
	for char in data:
		if char == '(':
			floor += 1
		else:
			floor -= 1
		position += 1
		if floor == -1:
			print char, position, floor
	return floor

fhand = open('input_01.txt')
inp = fhand.read()

print floor_count(inp)