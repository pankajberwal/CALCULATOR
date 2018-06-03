import re
print("*************CALCULATOR***************")
print("_____Enter 'quit' to EXIT_____\n")
previous = 0
run= True
def calculate():
    global run
    global previous
    if previous is 0:
        equation=input("ENTER THE EQUATION:")
    else:
        equation=input(str(previous))
    if equation=='quit':
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:;()""]','',equation)
        if previous is 0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

while run:
    calculate();