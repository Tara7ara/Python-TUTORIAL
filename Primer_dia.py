print("hello word")
#Para compilar el programa, usar la flecha de arriba a la derecha (visual code)

#Ejercicios de operaciones de clase
print (9 // 5) #1
print (695 % 20) #15
print (7 + 6 * 5) #37
print (7 * 6 + 5) #47
print (248 % 100 / 5) #9.6
print (6 * 3 - 9 // 4) #16
print ((5 - 7) * 2 ** 2) #-8
print (6 + (18 % (17 - 12))) #9

#Ejercicio The formula for computing the discriminant of a quadratic equation $ax^2 + bx +c = 0$ is $b^2 -4ac$. Write a program that computes the discriminant for the equation $3x^2 +4x + 5= 0$.
a = 3
b = 4
c = 5
result = ((b ** 2) - 4 * a * c)
print(result)

#Ejercicio de la aceleración
v0 = 5.6
v1 = 10.5
t = 0.5

resultacceleration = ((v1- v0) / t)
print(resultacceleration)

#Ejercicio del perimetro
width = 4.25 #ancho
height = 7.26 #altura

perimeter = width * 2 + height * 2
area = width * height
diagonal = (width ** 2) + (height ** 2) ** (1 / 2)

print("Perimetro:", perimeter,"\nArea:", area, "\nDiagonal:", diagonal)

