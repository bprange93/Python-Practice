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
    if a == b:
        total = a
    elif a < b:
        while a < b:
            # add the original number plus all numbers a turns into to c
            c.append(a)
            a += 1
            # once a == b we dont want that number so we break out
            if a == b:
                break
        # we want the total to be b + the sum of the numbers in c list.
        total = b + sum(c)
    elif a > b:
        while a > b:
            # add the original number plus all numbers a turns into to c
            c.append(b)
            b += 1
            # once a == b we dont want that number so we break out
            if b == a:
                break
        # we want the total to be b + the sum of the numbers in c list.
        total = a + sum(c)

    return total


def descending_order(num):
    # take the number and separate each individual number into separate characters
    # sort these numbers from highest to the lowest
    seperatedNumber = []
    stringNum = str(num)
    # Takes each number in num to make them individual characters
    for numbers in range(0, len(stringNum)):
        seperatedNumber.append(stringNum[numbers])
        # takes the array in and sorts it from the largest number down to the smallest
        seperatedNumber.sort(reverse=True)
    largestNumber = ''.join(seperatedNumber)
    return int(largestNumber)


def pig_it(text):
    # get the number of characters in each word
    # take the first 2 positions and swap them with the last 2 (-2)
    # add ay to the end of each word after letters have been swapped
    text = str(text).split(" ")
    answer = ""
    for words in text:
        new = ""
        # Ensures what is coming in just letters (isalpha)
        if words.isalpha():
            for word in range(1, len(words)):
                new += words[word]
            new += (text[0] + "ay")
            answer += (new + " ")
        else:
            print("not alpha")
            new += (" " + words)

    return answer


print(pig_it("This code will work"))
