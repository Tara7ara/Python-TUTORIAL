#Ejercicio 1
'''
# Inputs for password and verification code
password =  '@enti.cat'
verification_code ='52'  ## write some value here to test your code

# correct information conditions
correct_password = "securePass123"
correct_code = "42"

#Input
password = input("Write your password: ")
#verification_code = input("Write your code: ")

# Implement here if-elif-else logic
if password == correct_password:
    print("Password is correct!")
    verification_code = input("Write your code: ")
    if verification_code == correct_code:
     print("Code is correct!")
    else:
        print("Code incorrecte")
else:
    print("Password incorrecto")
'''
'''
if password == correct_password and verification_code == correct_code:
    print("Password and code is correct!")
else:
    print("Password o Codigo incorrecto")
'''

#Ejercicio 2

#Store information about the user here
user_data = {'ze_pqn': {'File1': 'r', 'File2':'r'}}
permission = {'File1':'r', 'File2':['w', 'x']}

# information given by user
username = "ze_pqn"
file_to_access ='File2' 
#print(user_data[username][file_to_access]) = r

x = input("yes = File2, otra cosa es File1, Qual quieres acceder: ")
if x == "yes":
    file_to_access = 'File2' 
else:
   file_to_access = 'File1' 
#write your program here
if user_data[username][file_to_access] == permission[file_to_access]:
   print("Has podido acceder al", file_to_access)
else:
   print("No has podido acceder al", file_to_access)