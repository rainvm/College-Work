import time
import sys
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
    "z": "--.."
}


def blink_on_switch():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(17, GPIO.OUT)
    while True:
        if GPIO.input(16):
            time.sleep(1)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(17, GPIO.LOW)


def variable_power():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 1000)
    pwm.start(0)
    i = 10
    while True:
        if GPIO.input(16):
            pwm.ChangeDutyCycle(i)
            i = (i+10) % 100
            time.sleep(0.5)


def morse_name():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 1000)
    pwm.start(0)
    name = "daniel albu"
    t = 2
    while True:
        if GPIO.input(16):
            for c in name:
                if c == " ":
                    time.sleep(0.2*t)
                else:
                    for l in morse[c]:
                        if l == "-":
                            pwm.ChangeDutyCycle(1)
                            time.sleep(0.2*t)
                            pwm.ChangeDutyCycle(0)
                        elif l == ".":
                            pwm.ChangeDutyCycle(1)
                            time.sleep(0.1*t)
                            pwm.ChangeDutyCycle(0)
                        time.sleep(0.1*t)
                    time.sleep(0.1*t)


if __name__ == "__main__":
    if sys.argv[1] == "blink_on_switch" or sys.argv[1] == "blink":
        blink_on_switch()
    if sys.argv[1] == "pwm":
        variable_power()
    if sys.argv[1] == "morse":
        morse_name()