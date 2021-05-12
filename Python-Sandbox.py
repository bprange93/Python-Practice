import math

# str = "Batman"
# print(str[-1::-1])


# def narcissistic(value):
# split up then multiplied by exponent of digits of number
# x = 0
# nw = 0
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


def divisors(integer):
    # Make an array to contain the numbers
    # Check to see if the number is divisible
    # if is divisible then divide number and put into list
    # if divisible by more than 1 number loop back to do it again
    # put this into the list from smallest to largest
    # if not divisible make it a prime number
    listDivisors = []
    for x in range(2, integer - 1):
        if integer % x == 0:
            listDivisors.append(x)
    if len(listDivisors) == 0:
        return str(integer) + 'is prime.'
    else:
        return listDivisors


def friend(x):
    # make list which returns a list
    # returned list can only have names with exactly 4 letters
    # if more or less than 4 letters not friend
    # return list of friends
    return [letters for letters in x if len(letters) == 4]


def myFriend(names):
    friendsList = []

    for words in names:
        if len(words) == 4:
            friendsList.append(words)

    return friendsList


def get_sum(a, b):
    # get integers between the two numbers
    # add all the numbers together
    c = []
    total = 0
    if a < b:
        while a < b:
            # add the original number plus all numbers a turns into to c
            c.append(a)
            a += 1
            # once a == b we dont want that number so we break out
            if a == b:
                break
        # we want the total to be b + the sum of the numbers in c list.
        total = b + sum(c)

    return total


print(get_sum(1, 3))
