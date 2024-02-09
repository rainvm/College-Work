import itertools as it


class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance

    # Series
    def __add__(self, other):
        return Resistor(self.resistance + other.resistance)

    # Parallel
    def __or__(self, other):
        return Resistor((1 / self.resistance + 1 / other.resistance) ** -1)

    def __repr__(self):
        return f"{self.resistance}"


def main():
    # Question 3
    r1 = Resistor(5000)
    r2 = Resistor(10000)
    r3 = Resistor(5000)
    r4 = Resistor(5000)
    req = r2 | (r3+r4)
    vin = 10
    v2 = vin * (req.resistance / (r1.resistance + req.resistance))
    vout = v2 * (r4.resistance / (r3.resistance + r4.resistance))
    print(vout)
    rth = r1 + (r2 | r3)
    print(rth)

    # Question 4
    p_target = 1 / 2
    r_target = 5.4e3
    p = 1 / 8
    resistors = [10, 15, 22, 33, 47, 68, 100, 150, 220, 330, 470, 680, 1000, 1500, 2200, 3300, 4700, 6800, 10000,
                 15000, 22000, 33000, 47000, 68000]
    resistance = 0


if __name__ == '__main__':
    main()
