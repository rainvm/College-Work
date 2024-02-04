import itertools as it


class Resistor:
    def __init__(self, resistance, power):
        self.resistance = resistance
        self.power = power

    # Series
    def __add__(self, other):
        return self.resistance + other.resistance,

    # Parallel
    def __or__(self, other):
        return (1 / self.resistance + 1 / other.resistance) ** -1


def main():
    p_target = 1 / 2
    r_target = 5.4e3
    p = 1 / 8
    resistors = [10, 15, 22, 33, 47, 68, 100, 150, 220, 330, 470, 680, 1000, 1500, 2200, 3300, 4700, 6800, 10000,
                 15000, 22000, 33000, 47000, 68000]
    resistance = 0


if __name__ == '__main__':
    main()
