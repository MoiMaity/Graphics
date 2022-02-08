import matplotlib.pyplot as plt
import math
import numpy as np


def creatematrix(a, b, c, d, tx, ty, e, f):
	m = [[a, b, tx], [c, d, ty], [e, f, 1]]
	return m

def multiply(a, b, r, c):
	res = [[0 for i in range(c)] for j in range(r)]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				res[i][j] += a[i][k] * b[k][j]
	return res

def reflect(p, q, m):
    	for i in range(len(p)):
    		pxy = [[p[i]], [q[i]], [1]]
    		res = multiply(m, pxy, 3, 1)
    		p[i] = res[0][0]
    		q[i] = res[1][0]
    	return p, q

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
	return lx, ly


xa, ya, xb, yb = int(input("Enter 1st x-coordinate : ")), int(input("Enter 1st y-coordinate : ")), int(input("Enter 2nd x-coordinate : ")), int(input("Enter 2nd y-coordinate : "))
xc, yc = linebres(xa, ya, xb, yb)
p = []
q = []
p.extend(xc)
q.extend(yc)
ch = int(input("1.Reflection about X-Axis\n2.Reflection about Y-Axis\n3.Reflection about an axis perpendicular to xy plane and passing through origin\n4.Reflection about line y=x\n"))
if(ch == 1):
	m = creatematrix(1, 0, 0, -1, 0, 0, 0, 0)
	p, q = reflect(p, q, m)
	plt.scatter(p, q)
	plt.plot(np.unique(p), np.poly1d(np.polyfit(p, q, 1))(np.unique(p)), color="blue")
elif(ch == 2):
	m = creatematrix(-1, 0, 0, 1, 0, 0, 0, 0)
	p, q = reflect(p, q, m)
	plt.scatter(p, q)
	plt.plot(np.unique(p), np.poly1d(np.polyfit(p, q, 1))(np.unique(p)), color="blue")
elif(ch == 3):
	m = creatematrix(-1, 0, 0, -1, 0, 0, 0, 0)
	p, q = reflect(p, q, m)
	plt.scatter(p, q)
	plt.plot(np.unique(p), np.poly1d(np.polyfit(p, q, 1))(np.unique(p)), color="blue")
elif(ch == 4):
	m = creatematrix(0, 1, 1, 0, 0, 0, 0, 0)
	p, q = reflect(p, q, m)
	plt.scatter(p, q)
	plt.plot(np.unique(p), np.poly1d(np.polyfit(p, q, 1))(np.unique(p)), color="blue")
plt.show()


