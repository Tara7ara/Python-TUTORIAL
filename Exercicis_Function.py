#Write a function even_or_odd(n) that takes an integer n and returns "Even" if the number is even and "Odd" if the number is odd.

def even_or_odd(n):
    if n % 2 == 0:
        print(f"This number {n}: is even")
    else:
        print(f"This number {n}: is odd")

even_or_odd(2)

#2) Write a function find_largest(lst) that takes a list of integers and returns the largest number in the list.
def find_largest(lst):
    largestNumber = 0
    for bucleLista in lst:
        if bucleLista > largestNumber:
            largestNumber = bucleLista
    
    print(f"The largest number for this list is: {largestNumber}")
        
find_largest([1,2,3,4,5,6,7,8,9,10])

#3) Write a function sum_of_numbers(lst) that calculates the sum of all the numbers in a list.
def sum_of_numbers(lst):
    sumNumbers = 0
    for bucleLista in lst:
        sumNumbers = bucleLista + sumNumbers 
    
    print(f"The sum of all number is: {sumNumbers}")

sum_of_numbers([1,2,3,4,5,6,7,8,9,10])

#4) Write a function count_vowels(s) that takes a string s and counts how many vowels (a, e, i, o, u) are in the string.
def count_vowels(s):
    countVowels = 0
    for bucleStr in s:
        if bucleStr in "aeiou":
            countVowels += 1
    print(f"Count on this str = {countVowels}")

count_vowels("qwertyuiopñlkjhgfdsazxcvbnm")

#5) Write a function find_primes(start, end) that finds all prime numbers between start and end (inclusive).
def find_primes(start, end): 
    for sumadorBucle in range(start, end +1):
        if sumadorBucle <= 1:
            continue
        prime = True
        for buclePrime in range(2,int(sumadorBucle ** 0.5) + 1):
            if sumadorBucle % buclePrime == 0:
                prime = False
                break
        if prime:
            print(f"This number is a PRIME number: {sumadorBucle}")              

find_primes(10,30)

#6) Write a function multiplication_table(n) that prints the multiplication table for a given number n.
def multiplication_table(n):
    solution = 0
    print(f"Multiplication table of the {n}")
    for bucleMultiplication in range(0,11):
        solution = n * bucleMultiplication
        print(f"{n} x {bucleMultiplication} = {solution}")

multiplication_table(8)

#7) Write a function factorial(n) that calculates the factorial of a number using a loop.
def factorial(n):
    factorialOperation = 1
    for bucleFactorial in range(1, n +1):
        factorialOperation *= bucleFactorial
    print(f"The factorial number {n} is {factorialOperation}")

factorial(22)

#8) Write a function fizzbuzz() that prints the numbers from 1 to 50. But for multiples of 3, print "Fizz", for multiples of 5, print "Buzz", and for multiples of both 3 and 5, print "FizzBuzz".
def fizzbuzz():
    contador35 = 0
    while contador35 < 50:
        if contador35 % 3 == 0 and contador35 % 5 == 0:
            print("FizzBuzz")
        elif contador35 % 3 == 0:
            print("Fizz")
        elif contador35 % 5 == 0:
            print("Buzz")
        else:
            print(contador35)
        contador35 += 1
fizzbuzz()

#9) Write a function find_min_max(lst) that returns both the smallest and largest number in a list.
def find_min_max(lst):
    min = 0
    max = 0
    for bucleNumber in lst:
        if bucleNumber < min:
            min = bucleNumber
        elif bucleNumber > max:
            max = bucleNumber 
    print(f"The min number is: {min}, the max number is: {max}")

find_min_max([1,2,3,4,5,6,7,8,9,10])

#10) Write a function reverse_list(lst) that takes a list and returns a new list that is the reverse of the input list.
def reverse_list(lst):
    reversedList = lst.copy()
    reversedList.reverse()
    print(reversedList)

reverse_list([1,2,3,4,5,6,7,8,9,10])

#11) Write a function that categorizes a person's age into three groups: "Child" if age is less than 12, "Teenager" if age is between 12 and 18 (inclusive),"Adult" if age is greater than 18.
def agePerson(lst):
    for bucleAge in lst:
        if bucleAge < 12:
            print(f"This age {bucleAge} is a Chield")
        elif bucleAge == 12 or bucleAge <= 18:
            print(f"This age {bucleAge} is a Teenager")
        else:
            print(f"This age {bucleAge} is a Adult")

agePerson([9,10,12,13,18,19, 42])

#12) Write a function that prints all multiples of n between 1 and 30.
def multiple(n):
    for bucleMultiple in range(1, 30):
        if bucleMultiple % n == 0:
            print(f"This number {bucleMultiple} is multiple for number {n}")

multiple(3)

#13) Write a function area_of_circle(radius) that calculates and returns the area of a circle, given the radius. Use the formula:Area = π * radius^2 (Use π = 3.14159).
def area_of_circle(radius):
    radius = float(radius)
    π = 3.14159
    area = π * (radius ** 2)
    print(f"The area for this radius {radius} is {area}")

area_of_circle(3.3)

#14) Write a function find_largest(a, b, c) that takes three numbers as arguments and returns the largest one.
def find_largest(a, b, c):
    largestNumber = 0
    if a < b:
        largestNumber = b
    elif b < c:
        largestNumber = c
    elif a < c:
        largestNumber = a

    print(f"The largest number is {largestNumber}")

find_largest(2,1,3)

#15)Write a function fahrenheit_to_celsius(fahrenheit) that converts a given temperature from Fahrenheit to Celsius using the formula: Celsius = (Fahrenheit - 32) * 5/9
def fahrenheit_to_celsius(fahrenheit):
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5/9)
    print(f"fahrenheit = {fahrenheit} ==> Celsius = {celsius}")

fahrenheit_to_celsius (122.2)

#16) Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2 , the first 10 terms will be:
def fibonnaci(int):
    f0 = 0
    f1 = 1
    fresult = f0 + f1
    for bucleFibonnaci in range(0, int + 1):
        fresult = f0 + f1
        f0 = f1
        f1 = fresult

        print(f"FIIBONNACI nº {bucleFibonnaci}= {fresult}")

fibonnaci(22)

#17) The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor of the number 600851475143?

def bigPrime(n):
    bigPrime = 0
    while n % 2 == 0:
       bigPrime = 2
       n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            bigPrime = i
            n //= i  
    if n > 2:
        bigPrime = n
    print(f"THE BIGEST PRIME IN THIS NUMBER {n} IS {bigPrime}") 

bigPrime(600851475143)

#18) A palindromic number reads the same both ways. The largest palindrome made from the product of two  2-digit numbers is 9009 = 91x99. Find the largest palindrome made from the product of two -digit numbers.
def bigPalindromic():
    maxPalindrome = 0
    operation1 = 0
    operation2 = 0
    for i in range(10, 100):
        for j in range(i, 100):
            product = i * j
        if str(product) == str(product)[::-1]:
            maxPalindrome = max(maxPalindrome, product)
            operation1 = i
            operation2 = j
    print(f"The largest palindrome made from the product of two 2-digit numbers is: {maxPalindrome} --> product is {operation1} x {operation2}")

bigPalindromic()

#19) 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallestMultiple(n):
    result = 1  

    for i in range(2, n + 1): 
        #Calculamos el MCM de result y i
        a = result
        b = i
        
        #Calcular el MCD usando el algoritmo de Euclides
        while b:
            a, b = b, a % b
        
        #MCM = (result * i) / MCD
        result = (result * i) // a  
    print(f"The smallest positive number that is evenly divisible by all the numbers from 1 to 20 is: {result}")

smallestMultiple(20)

#**20) The sum of the squares of the first ten natural numbers is**
# $1^2+2^2+...+10^2=385.$
# **The square of the sum of the first ten natural numbers is**
# $(1+2+...+10)^2=55^2=3025.$
# **Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is** $3025−385=2640$.
# **Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.**
def squareDifference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    sum_of_numbers = sum(i for i in range(1, n + 1))
    square_of_sum = sum_of_numbers ** 2
    difference = square_of_sum - sum_of_squares
    
    print(f"The difference between the sum of the squares and the square of the sum for the first 100 natural numbers is: {difference}")
squareDifference(100)

#21) By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number?
def nthPrime(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    print(f"The {n}th prime number is: {primes[-1]}")

nthPrime(10001)
