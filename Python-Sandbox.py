import math

#str = "Batman"
# print(str[-1::-1])


# def narcissistic(value):
# split up then multiplied by exponent of digits of number
#x = 0
#nw = 0
# if value > 9:
#    x = value.str.split
#    for i = 0, i > x.length, i + 1:
#        nw += math.pow(x=-1 y=-1):
# if nw == = value:
#    return True
# else:
#    return False


# print(narcissistic(371))

def digital_root(n):
    # First make a digit sum for the process to have a starting point = 0
    # make a temp = n so you can bring n into the equation
    # While temp > 9 keep going through till it isn't
    # make a for loop so it will take the single digits and start adding them together
    # once done set temp to the sum
    # if temp is till over 9 go back through again
    if(None):
        return 0
    return (n - 1) % 9 + 1 if n else 0


print(digital_root(10))
print(digital_root(942))
print(digital_root(8))
