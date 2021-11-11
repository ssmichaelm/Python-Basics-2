from io_class import io_class
import math

# Michael Moreland - Smoothstack, Python basics 2; 11/11/2021

# Function that retrieves all numbers divisible by 7 but not a multiple of 5 within a specific range
# Returns a list
def divBy7ButNot5():
    r = range(2000, 3201)
    results = []
    for n in r:
        if n % 7 == 0:
            if n % 5 != 0:
                results.append(n)

    return results
    
# Function that returns a factorial of a given number
def getFactorial(userNum):
    return math.factorial(userNum)

# Function that, given n, generates a dictionary such that {1: 1*1, 2: 2*2,..., n : n*n}
def generateDictionary(n):
    squaredDictionary = {}
    for i in range(1, n+1):
        squaredDictionary[i] = i*i
    return squaredDictionary

# Function that creates a list from a string separated by commas
def generateListFromString(str_line):
    l = str_line.split(",")
    return l

# Part 1: Create a list with one number, one word and one float value. Display the output of the list.
print("\nPart 1")
l = [11, "wish", 11.11]
print(l)

# Part 2: I have a nested list [1,1,[1,2]], how to grab the value of 2 from the list.
print("\nPart 2")
l = [1, 1,[1,2]]
print(f"Access the value of 2 from the list l = {l} with l[2][1]")
print(l[2][1])

# Part 3: lst=['a','b','c'] What is the result of lst[1:]?
print("\nPart 3")
lst = ['a', 'b', 'c']
print(f"The output of lst[1:] {lst} is {lst[1:]}")

# Part 4: Create a dictionary with weekdays as keys and week index numbers as values. Do assign dictionary to a variable
print("\nPart 4")
weekdays = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5,
            "Saturday": 6, "Sunday": 7}
print(f"Created a dictionary {weekdays}")

# Part 5: D = {‘k1’:[1,2,3]} what is the output of d[k1][1]
print("\nPart 5")
D = {'k1': [1,2,3]}
print(f"For a dictionary D = {D}, output of D[k1][1] is {D['k1'][1]}")

# Part 6: Can you create a list [1,[2,3]] into a tuple
print("\nPart 6")
l = [1, [2,3]]
print(f"Yes, a list {l} can be created into a tuple {tuple(l)} by casting a list to tuple with tuple(list_name)")

# Part 7: With a single set function can you turn the word ‘Mississippi’ to distinct character word.
print("\nPart 7")
distinctMississippi = set("Mississippi")
print("".join(str(s) for s in distinctMississippi))
# Part 8: Can you add an element ‘X’ to the above created set
print("Part 8")
distinctMississippi.add('X')
print(distinctMississippi)

# Part 9: Output of set([1,2,3])
print("\nPart 9")
print(set([1,2,3]))

####################################################

# Question 1: divisible by 7 but not a multiple of 5
print("\nPart 10")
print("All numbers divisible by 7 but not a multiple of 5")
result = divBy7ButNot5()
print(", ".join(str(r) for r in result))

# Question 2: get factorial given user input
print("\nPart 11")
userNum = int(input("Enter a value to get a factorial for: "))
print(getFactorial(userNum))

# Question 3: given an integer n, generate a dictionary that contains (i, i*i)
print("\nPart 12")
userNum = int(input("Enter an integer n to generate a dictionary for: "))
print("Generated dictionary is {}".format(generateDictionary(userNum)))

# Question 4: given a list of numbers separated with commas, generate a list and tuple
print("\nPart 13")
userNum = input("Enter values separated by a comma: ")
l = generateListFromString(userNum)
print(f"List {l}")
t = tuple(l)
print(f"Tuple {t}")

# Question 5: define a class with two methods getString and printString
print("\nPart 14")
print("Type a string to be capitalized")
ioObj = io_class()
ioObj.getString()
ioObj.printString()
