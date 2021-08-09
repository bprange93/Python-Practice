import math
import string

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

# first I want to make an array to hold all of the letters in a position
# then I want to make a method that takes the poisionts in the array of coors and remove that position
# For loop through all of them till 1 is remaining
# return last letter


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
    # Loops through words
    for words in text:
        new = ""
        # Ensures what is coming in just letters (isalpha)
        if words.isalpha():
            # follow pig latin convention
            for word in range(1, len(words)):
                new += words[word]
            new += (words[0] + "ay")
            answer += (new + " ")
        else:
            # takes care of code if there are numbers mixed in
            if text[-1] == '?' or '!':
                # gives answer correctly and takes away empty space to pass Kata
                answer += str(text).join(' ').strip() + text[-1]
            else:
                answer += str(text).join(' ')

    return answer.strip()


def is_pangram(s):
    # make a array containing all letters
    # create if statement for if s contains all letters
    # if they do return True if not return False
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    counter = 0
    # this takes away any open space between the letters
    s = str(s).split(" ")
    for words in s:
        for letters in words:
            if letters.isalpha():
                if letters.lower() in alphabet:
                    counter += 1
                    continue
            elif letters == ',' or '!' or '?':
                continue
    if counter >= 26:
        return True
    else:
        return False


# Detect Pangram codewars
# come back to fix potential problems (for fun) (if letters aren't all there but over 26 letters present)


def last_survivor(letters, coords):
    # take in the string and turn it into an array
    # each letter will be own character and have coorodinate that will need to be removed
    # for loop through removing letters till only one is left
    # return the final letter
    new_letters = list(letters)
    for pos in coords:
        new_letters.pop(pos)
    return ''.join(new_letters)


def to_camel_case(text):
    # seperate each word in text into its own string
    # once put into an array use capitalize method to capitalize the first letter in each word
    # work if statement this way in order to have the method only look for one character at a time
    if "_" and "-" in text:
        text = str(text).replace('_', ' ').replace('-', ' ').split()
    elif "-" in text:
        text = str(text).replace('-', ' ').split()
    else:
        text = str(text).replace('_', ' ').split()

    # created variables in order to hold the string and in order to seperate the words from one aother
    # in the order they are in while keeping the first word exactly how it is input.
    answer = ""
    words = []
    # for loops through the text by each word.
    # if it is the first word it is suppose to append it
    # else if its not it will append a capitalized version of it
    for word in text:
        if word == text[0]:
            words.append(word)
        else:
            words.append(word.title())
    # suppose to display the words as a string but still displaying in an array

    return (answer.join(words))


def zeros(n):
    # set a int to 1
    # make a for loop from 1 - n
    # multiply the int by itself + 1 add 1 to int and loop back through again till reaches value n
    # set new int to hold the value being multiplied
    # return the value multiplied when you finally reach the value of n
    start = 1
    answer = []
    total = 0
    # This will set up the array in order to get all the numbers that need to be multiplied.
    while start <= n:
        answer.append(start)
        start += 1
    # once the array is set we will loop through to start multiplying and setting the number each time through
    # Once i == answer then that means it will multiply by the last number setting total to what it should be.
    for i in answer:
        if i == len(answer):
            # brings back the proper total. Next need to get all of the leading 0's counted.
            return total
        elif i == 1:
            total += i * answer[i]
        else:
            total = total * answer[i]
    # set to 1 because I want it to count the 0 that already is there.
    trailZero = 1
    # pulling out where a 0 is and if the next number is a 0 add if not display trailZero.
    # for 0 in total:
    #     if i + 1 == 0:
    #         trailZero += 1
    #     if i + 1 == None:
    #         return trailZero


def solution(n):
    # set roman numeral values
    # once set make sure to set in order of if less than 5 or more which to use
    # set symbol as answer after done appending
    # make counter for how many numbers in int
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL',
               'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    i = 12
    output = ''
    while n != 0:
        if numbers[i] <= n:
            output += symbols[i]
            n = n - numbers[i]
        else:
            i -= 1
    return output


# since f is getting set to none the if statement will be triggered making f = 1 to pass into the plus function.
# rinsed and repeated for following numbers and added 0
def zero(f=None):
    return 0 if not f else f(0)


def one(f=None):
    return 1 if not f else f(1)


def two(f=None):
    return 2 if not f else f(2)


def three(f=None):
    return 3 if not f else f(3)


def four(f=None):
    return 4 if not f else f(4)


def five(f=None):
    return 5 if not f else f(5)


def six(f=None):
    return 6 if not f else f(6)


def seven(f=None):
    return 7 if not f else f(7)


def eight(f=None):
    return 8 if not f else f(8)


def nine(f=None):
    return 9 if not f else f(9)

# using lambda to bring in a from the function that is prior to the plus function


def plus(b):
    return lambda a: a+b


def minus(b):
    return lambda a: a-b


def times(b):
    return lambda a: a*b

# found that // returns the nearest digit alone no decimals. look into how this works


def divide_by(b):
    return lambda a: a//b


def even_and_odd(n):
    # create arrays to hold numbers whether they be even or odd
    # use for loop to split n into single digits
    # if numbers = 1,3,5,7,9 append to NO
    # if numbers = 0,2,4,6,8 append to NE
    # have to turn n into a string to be split
    NE = []
    NO = []
    number = []
    stringNum = str(n)

    # for loop should take in the numbers individually as a string
    for numbers in stringNum:
        number.append(numbers)

    for a in number:
        if int(a) == 0:
            pass
        elif int(a) % 2 == 0:
            NE.append(a)
        else:
            NO.append(a)

    # if odd contains nothing it will be equal and return 0
    if not NO:
        NO.append('0')
    # if even contains nothing then it will equal and return 0
    if not NE:
        NE.append('0')

    values = (int(''.join(NE)), int(''.join(NO)))

    return values


# print(even_and_odd(126453))
print(even_and_odd(2046))
