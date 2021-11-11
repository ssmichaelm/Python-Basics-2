import string
import inspect
import sys

# Michael Moreland - Smoothstack, Python basics 2; 11/11/2021

# Part 1: Write a string that returns just the letter ‘r’ from ‘Hello World’.
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.
print("\nPart 1")
print("Hello World"[8])

# Part 2: String slicing to grab the word ‘ink’ from the word  ‘thinker’
print("\nPart 2")
thinker = "thinker"
ink = thinker[2:5]
print(ink)

# Part 3: S = ’hello’, what is the output of h[1]?
print("\nPart 3")
# print("hello"[0][1]) Will output an error
print("From the string 'hello', h[1] outputs an error. While string is a recursive data structure, where each character in a string is a string itself (and thus an immutable array),\n'h' is a single character. \nSo while h[0] outputs 'h', h[1] points out of bounds.")

# Part 4: S = ’Sammy’, what is the output of s[2:]”
print("\nPart 4")
s = 'Sammy'
print(s[2:])

# Part 5: With a single set function can you turn the word ‘Mississippi’ to distinct character word.
print("\nPart 5")
distinctMississippi = set("Mississippi")
print("".join(str(s) for s in distinctMississippi))

# Part 6: Palindromes
print("\nPart 6")
def removePunctuation(str_line):
    return "".join(s.lower() for s in str_line if s in string.ascii_letters)

def isPalindrome(str_line):
    str_line = removePunctuation(str_line)
    if(str_line == str_line[::-1]):
        return "Y"
    else:
        return "N"

data = []
answers = []
print("Input data to see if the provided phrase(s) is a palindrome (first input a value representing number of strings to check): ")
x = eval(input())

while(x > 0):
    user_str_line = input()
    data.append(user_str_line)
    answers.append(isPalindrome(user_str_line) )
    x -= 1

print("Answers: ")
print(" ".join(str(s) for s in answers))


