#Ejercicio de Encriptar

list = [3, 5, 7]
squareNumbers = [x**2 for x in list]
secretKey = sum (squareNumbers)
print(secretKey)

#Ejercicio dos de encriptar
#who are you? == 119 104 111 32 97 114 101 32 121 111 117 63 
message = "who are you?"
encriptedList = []
desencriptedList = []
for translateMessage in message:
    encriptedList.append(ord(translateMessage) + secretKey) #El append es para sumar en la lista (guardado literal), ord es para traducirlo a asci a binario
print(encriptedList)

for transaleAscii in encriptedList:
   desencriptedList.append(chr(transaleAscii))#El chr es para traducir de binario a asci
print(desencriptedList)
result = "".join(desencriptedList) #Es para que se guarde la lista en una string
print(result)

#Como lo hace el professor
#encryptation = [ord(x) + secretKey for x in message]
#encryptation_second_step = [chr(x) for x in encryptation]
#encrypted_message = "".join(encryptation_second_step)
#encrypted_message

#Ejercicio tres de encriptar
encryptedMessage = "\x95ÂÁ·\x7fs\x9d´À¸Æs\x95ÂÁ·"
descencrypt = [chr(ord(x) - secretKey) for x in encryptedMessage]
desencrypted_message = "".join(descencrypt)
print(desencrypted_message)