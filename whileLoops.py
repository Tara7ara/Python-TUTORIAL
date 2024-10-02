'''
# Correct password (hardcoded for this exercise)
correct_password = "secure123"

# Simulated list of password attempts (in a real scenario, these would be user inputs)
attempts = ["password", "12345", "secure123"]

x = 0  #Inicia el contador en 0
while x != len(attempts):  #Mientras x sea diferente al tamaño de la lista 
    if correct_password in attempts:  
        print("Correct Password!")
        break  
    else:
        print("Wrong password")
        x += 1  

if x >= len(attempts):  #Si se ha excedido el número de intentos permitidos
    print("Too many attempts") 


# Simulated login attempts: 0 indicates failure, 1 indicates success
login_attempts = [0, 0, 1, 1, 0, 0, 0, 0, 1]

maxintentos = 0
contadorlista = 0
\''' COSA DEL PROFE
while contadorlista < len(login_attempts):
    attemps = login_attempts[contadorlista]
    if attemps == 0:
        maxintentos +=1
        print("Failed")
    else:
        maxintentos = 0
        print("Acces")

    if maxintentos == 3:
        print("To many intents")
        break

    contadorlista +=1
\'''
while contadorlista != len(login_attempts):
    intentos = login_attempts[contadorlista] #es para leer el numero de la lista
    if intentos == 0:
        print("FAIL")
        maxintentos+=1
    else:
        print("Succes")
        maxintentos = 0
    if maxintentos == 3:
            print("To many acces")
            break

    contadorlista+=1
'''
# Simulated blocklist of malicious IP addresses
blocklist = ["192.168.1.100", "10.0.0.5", "203.0.113.50", "172.16.0.2"]

# Incoming traffic data: each entry contains an IP and a list of packets (as strings)
traffic_log = [
    {"ip": "192.168.0.1", "packets": ["GET /index.html", "Host: example.com", "Data: harmless"]},
    {"ip": "10.0.0.5", "packets": ["attack on port 22", "Host: compromised.com"]},
    {"ip": "172.16.0.2", "packets": ["Data: normal traffic", "Host: normal.com"]},
    {"ip": "203.0.113.5", "packets": ["Data: harmless", "phishing attempt detected", "Host: phishing.com"]},
    {"ip": "192.168.1.10", "packets": ["GET /admin", "malware detected", "Host: danger.com"]},
    {"ip": "192.168.0.15", "packets": ["POST /upload", "Data: user login", "Host: safe.com"]}
]

# Keywords considered suspicious
suspicious_keywords = ["attack", "malware", "phishing"]

'''
#> mayor que
bucleIP = 0
for bucleIP in traffic_log:
    packets = bucleIP["packets"]
    attemps = traffic_log[bucleIP].get("ip")
    if attemps in blocklist:
        print("IP", attemps, "BLOQUED (IP BLOQUED)")
    else:
        for packet in packets:
            for keyword in suspicious_keywords:
                if keyword in packet:
                    print("IP", attemps, "BLOQUED (IP SUSPICIUS)")
                else:
                     print("IP", attemps, "CORRECT")
    bucleIP +=1
'''
#Revisar la palabra --> si lo tiene marcar como sospechosa
#Imprimir todo mientras pasa el control 

contador = 0 #Creo la variable para saber quantas ip he mirado
for bucle in traffic_log: #Entro en el bucle siempre que se cumpla "bucle" este dentro de traffic_log (en este caso 6)
    ip = bucle.get("ip") #Para sacar la ip, tengo que decir que numero del bucle estoy, saco la ip. No hace falta el traffic_log porque ya esta en el for
    packets = bucle.get("packets") #Sacar los paquetes
    ip_investigated = False
    if ip in blocklist:
        print("IP:",ip,"= Denied (BlockList)")
    else:
        for buclePackets in packets: #bucle de los packetes (en este caso 3)
            for bucleKeywords in suspicious_keywords: #bucle de las palabras (en este caso 3)
                if bucleKeywords in buclePackets: #si la palaba esta en suspicius:keywords, salta el denied
                    print("IP:",ip,"= Denied (Suspicius packets)")
                    ip_investigated = True #Si ya es true, sale del bucle 
                    break
            if ip_investigated == True: #Si ya es true, sale del bucle 
                break
        if ip_investigated == False:
            print("IP:",ip, "= Permited")

    contador += 1
print("Total ip revised", contador)
