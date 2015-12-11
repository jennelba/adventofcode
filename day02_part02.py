# --- Day 2: I Was Told There Would Be No Math ---

# The elves are running low on wrapping paper, and so they need to submit an order
# for more. They have a list of the dimensions (length l, width w, and height h)
# of each present, and only want to order exactly as much as they need.

# Fortunately, every present is a box (a perfect right rectangular prism), which
# makes calculating the required wrapping paper for each gift a little easier:
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
# need a little extra paper for each present: the area of the smallest side.

# The elves are also running low on ribbon. Ribbon is all the same width, so they
# only have to worry about the length they need to order, which they would again
# like to be exact.

# The ribbon required to wrap a present is the shortest distance around its sides,
# or the smallest perimeter of any one face. Each present also requires a bow made
# out of ribbon as well; the feet of ribbon required for the perfect bow is equal
# to the cubic feet of volume of the present. Don't ask how they tie the bow, though;
# they'll never tell.

# For example:
#   - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap
#     the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
#   - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap
#     the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

# How many total feet of ribbon should they order?



fhand = open('day02_input.txt')
data = fhand.read()

ribbonNeeded = 0

dimensions = data.splitlines()

for dim in dimensions:
	"""Parse dimensions into length, width, height."""
	l, w, h = dim.split('x')
	length = int(l)
	width = int(w)
	height = int(h)

	"""Find, compute and return smallest perimeter."""
	if length == max(length, width, height):
		perimeter = 2 * (width + height)
	elif width == max(length, width, height):
		perimeter = 2 * (length + height)
	else:
		perimeter = 2 * (length + width)

	"""Compute volume for bow and add perimeter to compute total."""
	bow = length * width * height
	total = bow + perimeter
	ribbonNeeded += total

print ribbonNeeded



	# firstxPos = inp.find('x')
	# length = int(inp[:firstxPos])
	# secondxPos = inp.find('x',firstxPos+1)
	# width = int(inp[firstxPos+1:secondxPos])
	# height = int(inp[secondxPos+1:])

	


