# please run this command on the terminal:
# pip install -r requirements.txt

# then run this:
# nosetests
# if it said OK then u're good to go ! :))


def add (a, b): 
    return a + b # jie <3

def subtract (a, b): 
    return a - b

def multiply (a, b): 
    return a * b # replaced this code by yours truly ken2ut

def divide (a, b): 
    # a sample code
    if b == 0:
        raise ZeroDivisionError("0 is not a valid denominator.")
    return a / b

def modulo (a, b): 
    return a % b # jie <3
