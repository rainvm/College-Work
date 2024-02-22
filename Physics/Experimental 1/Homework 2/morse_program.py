import sys
import time
import RPi.GPIO as GPIO

morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def main(args):
    argument = " ".join(args[1:])
    t = 0.2
    if GPIO.input(16):
        for c in argument:
            if c == " ":
                time.sleep(t*7)
            else:
                for l in morse[c]:
                    if l == "-":
                        pwm.ChangeDutyCycle(1)
                        time.sleep(t*3)
                        pwm.ChangeDutyCycle(0)
                    elif l == ".":
                        pwm.ChangeDutyCycle(1)
                        time.sleep(t)
                        pwm.ChangeDutyCycle(0)
                    time.sleep(t)
                time.sleep(t*3)


if __name__ == "__main__":
    main(sys.argv)
