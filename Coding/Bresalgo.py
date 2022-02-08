import matplotlib.pyplot as plt
import math
import numpy as np


def linebres(xa, ya, xb, yb):
	dx, dy = math.fabs(xa - xb), math.fabs(ya - yb)
	p, twody, twodydx = (2 * dy - dx), (2 * dy), (2 * (dy - dx))
	if xa > xb:
		x, y, xend = xb, yb, xa
	else:
		x, y, xend = xa, ya, xb
	lx, ly = [x, ], [y, ]
	while x < xend:
		x += 1
		if p < 0:
			p += twody
		else:
			y, p = (y + 1), (p + twodydx)
		lx.append(x)
		ly.append(y)
	ax, ay = (sum(lx) / len(lx)), (sum(ly) / len(ly))
	lax, lay = [lx[0], lx[-1]], [ly[0], ly[-1]]
	plt.scatter(lx, ly)
	plt.plot(np.unique(lx), np.poly1d(np.polyfit(lx, ly, 1))(np.unique(lx)), color="green")


xa, ya, xb, yb = int(input("Enter 1st x-coordinate : ")), int(input("Enter 1st y-coordinate : ")), int(input("Enter 2nd x-coordinate : ")), int(input("Enter 2nd y-coordinate : "))
linebres(xa, ya, xb, yb)
plt.show()


