print("Hello World!")
values =[1,2,3,4]
resultat = []

for number in values:
    resultat.append(number + 10)
print(resultat)

def sum10(number): return number +10
list(map(sum10, values))

for num in map (sum10, values):
    print(num)

def power2 (x): return x ** 2

result = list(map(power2, values))
print(result)

def eventNumber (x): return x%2 == 0
result = list(map(eventNumber, values))
print (result)

positiveNumber = []
for number in range (-5, 6):
    if number > 0:
        positiveNumber.append(number)
print (positiveNumber)

positiveNumber = [number for number in values if number < 0]
print(positiveNumber)

def positive(number): return number>0
def even(number):return number%2 == 0
list(filter(positive, filter( even, range(-5,6))))


def weakPassword(password): return 'password' not in password
password = ['password', '123', 'asdasdasd']
list(filter(weakPassword,password))

list= [1,2,3]