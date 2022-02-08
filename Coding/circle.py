import matplotlib.pyplot as plt


def circleMidpoint(xCenter, yCenter, radius):
	x, y, p = 0, radius, 1 - radius
	circlePlotpoints(xCenter, yCenter, x, y)
	xmat = [[], ]
	ymat = [[], ]
	while x < y:
		x += 1
		if p < 0:
			p += (2 * x + 1)
		else:
			y, p = (y - 1), (p + (2 * (x - y) + 1))
		xmat[0].append(x)
		ymat[0].append(y)
		circlePlotpoints(xCenter, yCenter, x, y)
	plt.plot(xmat[0], ymat[0])
	circleJoinpoints(xmat[0], ymat[0])


def circlePlotpoints(xCenter, yCenter, x, y):
	plt.scatter(xCenter + x, yCenter + y, marker="s")
	plt.scatter(xCenter - x, yCenter + y, marker="s")
	plt.scatter(xCenter + x, yCenter - y, marker="s")
	plt.scatter(xCenter - x, yCenter - y, marker="s")
	plt.scatter(xCenter + y, yCenter + x, marker="s")
	plt.scatter(xCenter - y, yCenter + x, marker="s")
	plt.scatter(xCenter + y, yCenter - x, marker="s")
	plt.scatter(xCenter - y, yCenter - x, marker="s")


def circleJoinpoints(xmat[0], ymat[0]):
	xmat[1] = ymat[0]
	ymat[1] = xmat[0]
	plt.plot(xmat[1], ymat[1])
	xmat[2] = [(x * -1) for x in xmat[0]]
	ymat[2] = ymat[0]
	plt.plot(xmat[2], ymat[2])
	xmat[3] = ymat[2]
	ymat[3] = xmat[2]
	plt.plot(xmat[3], ymat[3])
	xmat[4] = xmat[1]
	ymat[4] = [(y * -1) for y in ymat[1]]
	plt.plot(xmat[4], ymat[4])
	xmat[5] = ymat[4]
	ymat[5] = xmat[4]
	plt.plot(xmat[5], ymat[5])
	xmat[6] = [(x * -1) for x in xmat[1]]
	ymat[6] = [(y * -1) for y in ymat[1]]
	plt.plot(xmat[6], ymat[6])
	xmat[7] = [(x * -1) for x in xmat[0]]
	ymat[7] = [(y * -1) for y in ymat[0]]
	plt.plot(xmat[7], ymat[7])


xCenter, yCenter, radius = int(input("Enter X co-ordinate of center : ")), int(input("Enter Y co-ordinate of center : ")), int(input("Enter radius : "))
circleMidpoint(xCenter, yCenter, radius)
plt.show()