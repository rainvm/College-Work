import time
import sys
import RPi.GPIO as GPIO

# Morse Code dictionary
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


# Turns on pin 17 for 2 seconds one second after it receives a signal from pin 16.

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


# Increases the signal strength through pin 18 each time it receives a signal from pin 16 until it reaches 100
# and then resets to zero.
def variable_power():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 100)
    pwm.start(0)
    i = 10
    while True:
        if GPIO.input(16):
            pwm.ChangeDutyCycle(i)
            i = (i + 10) % 100
            time.sleep(0.5)


# Blinks Dan's name in morse code.
def morse_name():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 1000)
    pwm.start(0)
    name = "daniel albu"
    t = 0.2  # Time of a dot
    while True:
        if GPIO.input(16):
            for c in name:
                if c == " ":
                    time.sleep(t * 7)
                else:
                    for l in morse[c]:
                        if l == "-":
                            pwm.ChangeDutyCycle(1)
                            time.sleep(t * 3)
                            pwm.ChangeDutyCycle(0)
                        elif l == ".":
                            pwm.ChangeDutyCycle(1)
                            time.sleep(t)
                            pwm.ChangeDutyCycle(0)
                        time.sleep(t)
                    time.sleep(t * 3)


if __name__ == "__main__":
    # Calls one of the three functions based on arguments passed in the command line
    if sys.argv[1] == "blink":
        blink_on_switch()
    if sys.argv[1] == "pwm":
        variable_power()
    if sys.argv[1] == "morse":
        morse_name()
