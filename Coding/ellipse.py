import matplotlib.pyplot as plt
import math


def ellipseMidpoint(xCenter, yCenter, Rx, Ry):
	Rx2, Ry2 = Rx * Rx, Ry * Ry
	twoRx2, twoRy2 = 2 * Rx2, 2 * Ry2
	x, y, px = 0, Ry, 0
	py = twoRx2 * y
	ellipsePlotpoints(xCenter, yCenter, x, y)
	p = math.fabs(Ry2 - (Rx2 * Ry) + (0.25 * Rx2))
	while px < py:
		x, px = (x + 1), (px + twoRy2)
		if p < 0:
			p += Ry2 + px
		else:
			y, py, p = (y - 1), (py - twoRx2), (p + Ry2 + px - py)
		ellipsePlotpoints(xCenter, yCenter, x, y)
	p = math.fabs(Ry2 * (x + 0.5) * (x + 0.5) + Rx2 * (y - 1) * (y - 1) - Rx2 * Ry2)
	while y > 0:
		y, py = (y - 1), (py - twoRx2)
		if p > 0:
			p += Rx2 - py
		else:
			x, px, p = (x + 1), (px + twoRy2), (p + Rx2 - py + px)
		ellipsePlotpoints(xCenter, yCenter, x, y)

	
def ellipsePlotpoints(xCenter, yCenter, x, y):
	plt.scatter(xCenter + x, yCenter + y, marker="s")
	plt.scatter(xCenter - x, yCenter + y, marker="s")
	plt.scatter(xCenter + x, yCenter - y, marker="s")
	plt.scatter(xCenter - x, yCenter - y, marker="s")


xCenter, yCenter, Rx, Ry = int(input("Enter X co-ordinate of center : ")), int(input("Enter Y co-ordinate of center : ")), int(input("Enter Rx : ")), int(input("Enter Ry : "))
ellipseMidpoint(xCenter, yCenter, Rx, Ry)
plt.show()
		