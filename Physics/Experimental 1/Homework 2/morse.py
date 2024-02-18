import sys
import time

morse = {
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
}


def main(args):
    argument = " ".join(args[1:])
    argument = argument.replace(" ", "  ")
    for letter, code in morse.items():
        argument = argument.replace(letter, code)
        argument = argument.replace(letter.upper(), code)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 1000)
    pwm.start(0)
    if GPIO.input(16):
        for c in argument:
            if c == " ":
                time.sleep(0.2 * t)
            else:
                for l in morse[c]:
                    if l == "-":
                        pwm.ChangeDutyCycle(1)
                        time.sleep(0.2 * t)
                        pwm.ChangeDutyCycle(0)
                    elif l == ".":
                        pwm.ChangeDutyCycle(1)
                        time.sleep(0.1 * t)
                        pwm.ChangeDutyCycle(0)
                    time.sleep(0.1 * t)
                time.sleep(0.1 * t)


if __name__ == "__main__":
    main(sys.argv)
