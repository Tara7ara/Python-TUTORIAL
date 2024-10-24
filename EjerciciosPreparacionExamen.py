# List of employees
employee_names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Isaac", "Jack",
    "Karen", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Rachel", "Sam", "Tina",
    "Umar", "Vera", "Wendy", "Xander", "Yara", "Zane", "Adam", "Bella", "Carl", "Daisy",
    "Ethan", "Fiona", "George", "Helen", "Ian", "Julia", "Kevin", "Linda", "Mark", "Nina",
    "Owen", "Penny", "Quincy", "Rita", "Steve", "Tara", "Uma", "Victor", "Will", "Xena",
    "Yasmin", "Zack", "Alex", "Brittany", "Chris", "Dana", "Eric", "Felicity", "Gavin", "Harriet",
    "Ivy", "Jonas", "Kelly", "Leo", "Morgan", "Nate", "Oscar", "Patty", "Quinton", "Rose",
    "Sean", "Tessa", "Ulrich", "Vivian", "Walter", "Ximena", "Yusuf", "Zoey", "Aria", "Ben",
    "Caleb", "Diana", "Elliott", "Faith", "Gary", "Heather", "Ivan", "Jenna", "Kurt", "Laura",
    "Max", "Nora", "Omar", "Peter", "Queenie", "Ray", "Sara", "Tom", "Uri", "Violet"
]

# list of salaries (daily)
salaries = [
    100, 95, 120, 80, 110, 90, 105, 100, 115, 125,
    85, 100, 130, 110, 120, 95, 105, 115, 130, 90,
    100, 110, 95, 125, 115, 120, 100, 105, 90, 110,
    125, 95, 100, 120, 110, 130, 85, 100, 90, 115,
    105, 125, 100, 95, 120, 110, 115, 100, 125, 90,
    100, 105, 120, 110, 130, 95, 100, 85, 105, 125,
    110, 90, 115, 100, 120, 95, 125, 100, 110, 85,
    100, 120, 105, 90, 110, 125, 130, 95, 100, 110,
    120, 100, 90, 115, 125, 110, 95, 100, 130, 120,
    100, 115, 105, 110, 95, 120, 125, 90, 100, 110
]

attendance = [22, 24, 23, 19, 16, 15, 17, 15, 23, 17, 15, 25, 17, 25, 17, 19, 23, 20, 19, 15, 25, 21, 20, 16, 24, 25, 22, 23, 21, 20, 20, 22, 17, 15, 18, 21, 24, 25, 24, 15, 24, 16, 17, 20, 21, 24, 17, 15, 21, 15, 23, 19, 16, 18, 16, 16, 15, 25, 15, 25, 20, 22, 16, 22, 20, 22, 24, 23, 25, 21, 15, 18, 21, 22, 24, 25, 17, 16, 20, 21, 23, 21, 22, 22, 20, 19, 16, 22, 17, 20, 15, 22, 21, 19, 24, 16, 24, 23, 22, 19]
secondMonth = [25, 19, 16, 18, 25, 24, 15, 21, 20, 25, 17, 18, 24, 24, 22, 21, 16, 20, 20, 24, 23, 15, 15, 25, 15, 20, 18, 25, 19, 19, 24, 16, 16, 25, 22, 23, 16, 16, 21, 24, 15, 24, 22, 23, 16, 15, 25, 15, 23, 22, 22, 16, 18, 15, 16, 20, 20, 16, 23, 17, 17, 24, 25, 20, 23, 21, 22, 21, 19, 17, 19, 23, 23, 21, 19, 18, 25, 24, 24, 21, 23, 23, 18, 18, 17, 19, 24, 22, 25, 25, 19, 18, 18, 16, 23, 25, 21, 19, 23, 18]
thirdMonth = [15, 19, 25, 24, 15, 19, 15, 25, 16, 17, 23, 24, 23, 24, 22, 20, 22, 18, 25, 20, 20, 24, 22, 22, 16, 25, 20, 17, 20, 24, 23, 22, 18, 20, 24, 17, 21, 17, 21, 17, 19, 20, 22, 22, 17, 17, 22, 24, 23, 21, 24, 16, 17, 15, 24, 20, 20, 17, 21, 24, 24, 20, 16, 22, 20, 19, 18, 20, 20, 19, 23, 19, 21, 24, 25, 16, 24, 24, 21, 18, 21, 16, 24, 20, 21, 25, 24, 20, 20, 22, 20, 17, 15, 25, 20, 19, 15, 21, 15, 16]
forthMonth = [25, 23, 25, 15, 15, 17, 21, 15, 19, 17, 18, 25, 22, 15, 15, 18, 17, 24, 18, 19, 24, 20, 18, 15, 16, 15, 25, 25, 15, 16, 23, 17, 17, 20, 22, 17, 22, 20, 20, 21, 15, 25, 15, 18, 25, 18, 15, 17, 21, 21, 15, 23, 19, 17, 19, 19, 18, 17, 25, 24, 16, 22, 21, 22, 23, 20, 19, 17, 18, 20, 19, 20, 22, 25, 19, 23, 25, 22, 23, 15, 17, 22, 20, 20, 23, 19, 21, 25, 22, 23, 22, 15, 15, 18, 20, 18, 18, 19, 24, 25]
fifthMonth = [21, 22, 25, 18, 23, 16, 19, 19, 19, 24, 15, 19, 23, 24, 24, 18, 21, 18, 22, 23, 17, 15, 25, 25, 20, 16, 24, 19, 25, 18, 15, 22, 19, 15, 16, 24, 23, 21, 16, 16, 15, 15, 24, 19, 18, 17, 16, 17, 25, 15, 18, 15, 25, 16, 22, 22, 16, 23, 21, 17, 15, 24, 16, 23, 24, 21, 21, 22, 20, 25, 22, 22, 18, 20, 19, 20, 22, 21, 23, 19, 21, 15, 24, 22, 19, 25, 15, 15, 21, 15, 15, 19, 18, 25, 21, 18, 15, 20, 25, 22]
sixthMonth = [25, 23, 17, 16, 21, 20, 20, 17, 19, 21, 23, 17, 15, 24, 21, 17, 23, 21, 21, 17, 19, 21, 25, 24, 17, 24, 19, 19, 15, 20, 20, 16, 21, 17, 17, 20, 25, 25, 16, 19, 21, 25, 15, 24, 25, 24, 16, 23, 15, 17, 18, 21, 25, 17, 19, 25, 25, 20, 20, 20, 18, 19, 19, 18, 23, 21, 17, 23, 24, 16, 16, 22, 20, 16, 22, 16, 22, 20, 23, 18, 22, 22, 18, 16, 20, 16, 21, 24, 23, 25, 23, 16, 18, 19, 20, 17, 15, 16, 18, 24]
seventhMonth = [21, 24, 24, 18, 22, 23, 15, 22, 24, 22, 23, 24, 21, 25, 19, 25, 24, 15, 15, 21, 21, 22, 21, 22, 19, 16, 15, 19, 22, 17, 18, 25, 24, 23, 24, 21, 19, 17, 23, 15, 23, 16, 16, 20, 16, 24, 24, 18, 16, 24, 25, 20, 23, 24, 25, 17, 19, 15, 19, 24, 15, 19, 23, 20, 20, 24, 16, 16, 23, 17, 25, 22, 23, 18, 18, 22, 15, 19, 21, 19, 18, 24, 20, 16, 16, 19, 23, 16, 25, 24, 18, 23, 22, 22, 19, 24, 15, 24, 16, 23]
eighthMonth = [25, 21, 18, 19, 21, 19, 18, 20, 16, 18, 22, 17, 23, 22, 25, 18, 16, 15, 19, 18, 20, 23, 19, 24, 25, 18, 19, 19, 15, 23, 16, 16, 15, 16, 25, 18, 22, 23, 20, 17, 22, 22, 23, 21, 25, 15, 17, 21, 25, 17, 22, 16, 15, 20, 25, 25, 20, 23, 21, 24, 19, 17, 21, 23, 25, 16, 23, 22, 15, 23, 25, 20, 21, 16, 16, 21, 25, 19, 20, 19, 17, 23, 24, 17, 17, 21, 24, 17, 17, 20, 24, 23, 16, 15, 22, 20, 16, 21, 25, 20]
ninthMonth = [25, 17, 23, 24, 20, 16, 16, 20, 23, 24, 15, 18, 20, 25, 23, 25, 23, 21, 25, 19, 15, 18, 21, 24, 23, 20, 19, 21, 20, 17, 25, 16, 16, 23, 15, 24, 20, 20, 19, 19, 19, 20, 19, 19, 22, 25, 21, 15, 18, 24, 24, 15, 21, 16, 24, 17, 19, 23, 19, 18, 16, 21, 20, 18, 23, 22, 16, 19, 18, 24, 16, 15, 19, 21, 22, 15, 19, 17, 18, 20, 20, 24, 25, 16, 22, 19, 22, 15, 15, 17, 17, 16, 24, 21, 16, 15, 17, 20, 21, 20]
tenthMonth = [25, 24, 17, 16, 18, 16, 18, 24, 20, 17, 21, 17, 21, 24, 23, 21, 25, 20, 18, 17, 19, 25, 23, 15, 23, 19, 24, 20, 21, 25, 24, 22, 18, 22, 17, 19, 18, 18, 19, 17, 18, 17, 18, 18, 16, 24, 21, 18, 21, 22, 21, 16, 17, 24, 18, 20, 22, 16, 22, 20, 25, 17, 21, 23, 23, 20, 20, 15, 24, 20, 22, 20, 15, 25, 23, 21, 23, 25, 17, 21, 20, 23, 16, 18, 23, 25, 22, 17, 15, 20, 25, 22, 25, 16, 23, 15, 24, 25, 25, 15]
eleventhMonth = [24, 17, 18, 18, 19, 21, 22, 25, 22, 19, 23, 25, 15, 16, 21, 25, 19, 18, 15, 21, 25, 20, 22, 15, 17, 20, 18, 24, 16, 24, 18, 18, 21, 19, 15, 24, 25, 24, 24, 21, 24, 20, 17, 17, 19, 19, 23, 17, 22, 24, 25, 15, 17, 15, 22, 20, 25, 21, 19, 23, 21, 24, 19, 21, 16, 18, 19, 18, 24, 20, 19, 25, 24, 19, 24, 16, 20, 18, 18, 20, 16, 23, 22, 25, 20, 18, 19, 15, 19, 15, 21, 20, 20, 16, 16, 24, 21, 15, 23, 24]
twelthMonth = [24, 25, 17, 19, 19, 18, 20, 19, 21, 15, 15, 18, 23, 19, 19, 25, 18, 17, 24, 25, 18, 24, 19, 19, 25, 17, 20, 18, 15, 16, 23, 24, 15, 23, 16, 18, 19, 22, 23, 20, 23, 15, 17, 20, 20, 23, 24, 17, 19, 15, 17, 16, 20, 16, 23, 16, 24, 21, 20, 24, 21, 16, 20, 20, 22, 24, 18, 19, 15, 16, 24, 20, 16, 23, 17, 20, 24, 17, 25, 21, 20, 21, 19, 16, 20, 16, 21, 16, 19, 15, 18, 25, 17, 20, 18, 23, 21, 15, 22, 20]


#Ejercicio 1
dictionariGen = {}
count = 0
for bucleEmploye in employee_names:
    dictionariGen[bucleEmploye] = salaries[count]
    count += 1
def ejercicio1():
    print(dictionariGen)

#Ejercicio 2 --> 22 dias
def ejercicio2():
    for bucleMonth in dictionariGen:
        dictionariGen[bucleMonth] = ["22", 22*dictionariGen[bucleMonth]]
    print(dictionariGen)

#Ejercicio 3 --> dias reales
def ejercicio3():
    count = 0 
    for bucleMonth2 in dictionariGen:
        dictionariGen[bucleMonth2] = [attendance[count], attendance[count] * dictionariGen[bucleMonth2]]
        count += 1
    print(dictionariGen)

#Ejercicio 4 --> 
def ejercicio4():
    count = 0
    for bucleWorked in dictionariGen:
        diasTrabajado = dictionariGen[bucleWorked][0]
        
        if diasTrabajado < 18:
            dictionariGen[bucleWorked] = [attendance[count], "Under"]
        elif diasTrabajado > 22:
            dictionariGen[bucleWorked] = [attendance[count], "Overtime"]
        else:
            dictionariGen[bucleWorked] = [attendance[count], "NormalEmployee"]
        count += 1
    print(dictionariGen)

#Ejercicio 5 --> calculate_salary()
def calculate_salary(daylySalary, actualWorkdays, normalWorkdays):
    if actualWorkdays < 18:
        return daylySalary * actualWorkdays - (0.1 * (daylySalary * actualWorkdays)) #*0.9
    elif actualWorkdays > normalWorkdays:
        return daylySalary * actualWorkdays + (0.1 * (daylySalary * actualWorkdays)) #*1.1
    else:
        return daylySalary * actualWorkdays

#Ejercicio 6
months = [attendance, secondMonth, thirdMonth, forthMonth, fifthMonth, sixthMonth, seventhMonth, eighthMonth, ninthMonth, tenthMonth, eleventhMonth, twelthMonth]


ejercicio3()
ejercicio4()
countA = 0
for bucle in dictionariGen:
    dictionariGen[bucle][1] = calculate_salary(salaries[countA], attendance[countA], 22)
    countA +=1
print(dictionariGen)