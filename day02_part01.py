# --- Day 2: I Was Told There Would Be No Math ---

# The elves are running low on wrapping paper, and so they need to submit an order
# for more. They have a list of the dimensions (length l, width w, and height h)
# of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which
# makes calculating the required wrapping paper for each gift a little easier:
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
# need a little extra paper for each present: the area of the smallest side.

# For example:
#   - A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet
#     of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
#   - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet
#     of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

# All numbers in the elves' list are in feet. How many total square feet of wrapping
# paper should they order?



fhand = open('day02_input.txt')
data = fhand.read()

paperNeeded = 0

dimensions = data.splitlines()

for dim in dimensions:
	"""Parse dimensions into length, width, height."""
	l, w, h = dim.split('x')
	length = int(l)
	width = int(w)
	height = int(h)

	"""Find, compute and return area of smallest side."""
	if length == max(length, width, height):
		extra = width * height
	elif width == max(length, width, height):
		extra = length * height
	else:
		extra = length * width

	"""Compute surface area and add extra to compute total."""
	area = (2 * length * width) + (2 * width * height) + (2 * length * height)
	total = area + extra
	paperNeeded += total

print paperNeeded



	# firstxPos = inp.find('x')
	# length = int(inp[:firstxPos])
	# secondxPos = inp.find('x',firstxPos+1)
	# width = int(inp[firstxPos+1:secondxPos])
	# height = int(inp[secondxPos+1:])

	


