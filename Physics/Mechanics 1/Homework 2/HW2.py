import numpy as np
import matplotlib.pyplot as plt


# Question 7
def part1():
    t = np.linspace(0, 3, 100000)
    vter = [0.3, 1, 3, 10000000]
    vy0 = 1
    vx0 = 1
    for i in range(len(vter)):
        x = vx0 * vter[i] * (1 - np.exp(-t / vter[i]))
        y = (vy0 + vter[i]) * vter[i] * (1 - np.exp(-t / vter[i])) - vter[i] * t
        plt.plot(t, y)
        plt.show()
        plt.plot(t, x)
        plt.show()


# Question 8
def part2():
    vter = 1
    theta = 0.75
    g = 9.8
    vx0 = np.cos(theta)
    vy0 = np.sin(theta)
    rvac = 2*vx0*vy0/g
    print(f"The maximum range in a vacuum is {rvac} m at an angle of 0.75.")
    x = np.linspace(0, 0.6, 100000)
    f = (vy0+1)/vx0 * x + np.log(1 - x / vx0)
    d = x[np.where(np.diff(np.sign(f)))[0][1]]
    print(f"The range with drag is {d} m at an angle of 0.75.")
    angle = np.linspace(0.4, 0.8, 10000)
    c = []
    for i in angle:
        vx0 = np.cos(i)
        vy0 = np.sin(i)
        f = (vy0+1)/vx0 * x + np.log(1 - x / vx0)
        l = x[np.where(np.diff(np.sign(f)))[0][1]]
        c.append(l)

    print(f"The maximum range with drag is {max(c)} m at an angle of {angle[np.argmax(c)]}.")


if __name__ == "__main__":
    part2()
