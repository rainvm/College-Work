from Electronics import Resistor


def main():
    r1 = Resistor(5000)
    r2 = Resistor(10000)
    r3 = Resistor(5000)
    r4 = Resistor(5000)
    req = r2 * (r3 + r4)
    vin = 10
    v2 = vin * (req.r / (r1.r + req.r))
    vth = v2 * (r4.r / (r3.r + r4.r))
    print(f"The thevanin potential is {vth} V.")
    rth = Resistor(5000) + (Resistor(10000) * Resistor(5000))
    print(f"The thevanin resistance is {rth.r} Ω")


if __name__ == '__main__':
    main()
