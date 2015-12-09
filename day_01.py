# --- Day 1: Not Quite Lisp ---

def floor_count(data):
	floor = 0
	for char in data:
		if char == '(':
			nextFloor = floor + 1
		else:
			nextFloor = floor - 1
		floor = nextFloor
	return floor

fhand = open('input_01.txt')
inp = fhand.read()

print floor_count(inp)