# --- Day 1: Not Quite Lisp ---

# Santa is trying to deliver presents in a large apartment building, but he can't find
# the right floor - the directions he got are a little confusing. He starts on the
# ground floor (floor 0) and then follows the instructions one character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ),
# means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will never find
# the top or bottom floors.

# For example:
#   - (()) and ()() both result in floor 0.
#   - ((( and (()(()( both result in floor 3.
#   - ))((((( also results in floor 3.
#   - ()) and ))( both result in floor -1 (the first basement level).
#   - ))) and )())()) both result in floor -3.

# To what floor do the instructions take Santa?


def floorCount(data):
	"""Function to find the floor number to which the instructions take Santa."""
	floor = 0
	for char in data:
		if char == '(':
			floor += 1
		else:
			floor -= 1
	return floor


fhand = open('day01_input.txt')
inp = fhand.read()

print floorCount(inp)