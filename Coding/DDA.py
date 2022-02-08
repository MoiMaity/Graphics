import matplotlib.pyplot as plt
import math


def lineDDA(xa, ya, xb, yb):
    dx, dy, x, y = xb - xa, yb - ya, xa, ya
    if math.fabs(dx) > math.fabs(dy):
        steps = math.fabs(dx)
    else:
        steps = math.fabs(dy)
    xinc, yinc, lx, ly = (dx / steps), (dy / steps), [round(x), ], [round(y), ]
    for k in range(0, int(steps)):
        x, y = x + xinc, y + yinc
        lx.append(round(x))
        ly.append(round(y))
    ax, ay = (sum(lx) / len(lx)), (sum(ly) / len(ly))
    lax, lay = [lx[0], round(ax), lx[-1]], [ly[0], round(ay), ly[-1]]
    plt.scatter(lx, ly)
    plt.plot(lax, lay, color='green')
    plt.show()


xa, ya, xb, yb = int(input("Enter 1st x-coordinate : ")), int(input("Enter 1st y-coordinate : ")), int(input("Enter 2nd x-coordinate : ")), int(input("Enter 2nd y-coordinate : "))
lineDDA(xa, ya, xb, yb)
