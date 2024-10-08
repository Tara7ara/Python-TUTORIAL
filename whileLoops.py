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

#> mayor que

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
            print("IP:",ip, "= Save")

    contador += 1
print("Total ip revised", contador)

#Ejercicio extra por mi
#List of 100 logged IP addresses (simulating a log file)
ip_log = [
    "192.168.0.1", "10.0.0.5", "192.168.0.2", "10.0.0.6", "203.0.113.5", "192.168.1.1", 
    "172.16.0.1", "10.0.0.7", "192.168.1.2", "172.16.0.2", "192.168.0.3", "10.0.0.8", 
    "172.16.0.3", "192.168.1.3", "10.0.0.9", "203.0.113.6", "192.168.0.4", "10.0.0.10", 
    "172.16.0.4", "192.168.1.4", "10.0.0.11", "192.168.0.5", "10.0.0.12", "172.16.0.5", 
    "192.168.1.5", "10.0.0.13", "192.168.0.6", "10.0.0.14", "172.16.0.6", "192.168.1.6", 
    "10.0.0.15", "192.168.0.7", "10.0.0.16", "172.16.0.7", "192.168.1.7", "10.0.0.17", 
    "192.168.0.8", "10.0.0.18", "172.16.0.8", "192.168.1.8", "10.0.0.19", "192.168.0.9", 
    "10.0.0.20", "172.16.0.9", "192.168.1.9", "10.0.0.21", "192.168.0.10", "10.0.0.22", 
    "172.16.0.10", "192.168.1.10", "10.0.0.23", "192.168.0.11", "10.0.0.24", "172.16.0.11", 
    "192.168.1.11", "10.0.0.25", "192.168.0.12", "10.0.0.26", "172.16.0.12", "192.168.1.12", 
    "10.0.0.27", "192.168.0.13", "10.0.0.28", "172.16.0.13", "192.168.1.13", "10.0.0.29", 
    "192.168.0.14", "10.0.0.30", "172.16.0.14", "192.168.1.14", "10.0.0.31", "192.168.0.15", 
    "10.0.0.32", "172.16.0.15", "192.168.1.15", "10.0.0.33", "192.168.0.16", "10.0.0.34", 
    "172.16.0.16", "192.168.1.16", "10.0.0.35", "192.168.0.17", "10.0.0.36", "172.16.0.17", 
    "192.168.1.17", "10.0.0.37", "192.168.0.18", "10.0.0.38", "172.16.0.18", "192.168.1.18", 
    "10.0.0.39", "192.168.0.19", "10.0.0.40", "172.16.0.19", "192.168.1.19", "10.0.0.41"
]

suspiciousIP = "203.0.113.5"
suspiciousIPs = False
bucleIpLog = 0
print("EJERCICIO RARO")
while bucleIpLog != len(ip_log):
    if ip_log[bucleIpLog] == suspiciousIP:
        print("The suspicius IP(",suspiciousIP,") is here")
        suspiciousIPs = True
        break
    bucleIpLog += 1
if suspiciousIPs == False:
    print("All ip is OK")
