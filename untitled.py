import sys

args = sys.argv
print(args)
x = len(args[1])
y = args[1]
answer = '';
for i in range(x):
    if y[i] == 'A' or y[i] == 'a':
        answer = answer + ".-"
    elif y[i] == 'B' or y[i] ==  'b':
        answer = answer + '-...'
    elif y[i] == 'C' or y[i] ==  'c':
        answer = answer + "-.-."
    elif y[i] == 'D' or y[i] ==  'd':
        answer = answer + '-..'
    elif y[i] == 'E' or y[i] ==  'e':
        answer = answer +'.'
    elif y[i] == 'F' or y[i] ==  'f':
        answer = answer +'..-.'
    elif y[i] == 'G' or y[i] ==  'g':
        answer = answer + '--.'
    elif y[i] == 'H' or y[i] ==  'h':
        answer = answer + '....'
    elif y[i] == 'I' or y[i] ==  'i':
        answer = answer + '..'
    elif y[i] == 'J' or y[i] ==  'j':
        answer = answer + ".---"
    elif y[i] == 'K' or y[i] ==  'k':
        answer = answer + '-.-'
    elif y[i] == 'L' or y[i] ==  'l':
        answer = answer +'.-..'
    elif y[i] == 'M' or y[i] ==  'm':
        answer = answer +'--'
    elif y[i] == 'N' or y[i] ==  'n':
        answer = answer +'-.'
    elif y[i] == 'O' or y[i] ==  'o':
        answer = answer +'---'
    elif y[i] == 'P' or y[i] ==  'p':
        answer = answer +'.--.'
    elif y[i] == 'Q' or y[i] ==  'q':
        answer = answer +'--.-'
    elif y[i] == 'R' or y[i] ==  'r':
        answer = answer +'.-.'
    elif y[i] == 'S' or y[i] ==  's':
        answer = answer +'...'
    elif y[i] == 'T' or y[i] ==  't':
        answer = answer +'-'
    elif y[i] == 'U' or y[i] ==  'u':
        answer = answer +'..-'
    elif y[i] == 'V' or y[i] ==  'v':
        answer = answer +'...-'
    elif y[i] == 'W' or y[i] ==  'w':
        answer = answer +'.--'
    elif y[i] == 'X' or y[i] ==  'x':
        answer = answer +'-..-'
    elif y[i] == 'Y' or y[i] ==  'y':
        answer = answer +'-.--'
    elif y[i] == 'Z' or y[i] ==  'z':
        answer = answer +'--..'
    elif y[i] == '':
        answer = answer +' '

print(answer)
    

