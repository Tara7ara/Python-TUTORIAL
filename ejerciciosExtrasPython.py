# Hardcoded lists
allowed_ips = ["192.168.0.1", "10.0.0.1", "172.16.0.1"]
suspicious_activity = [
    {"ip": "192.168.0.2", "suspicious_packets": 5},
    {"ip": "10.0.0.1", "suspicious_packets": 2},
    {"ip": "192.168.0.3", "suspicious_packets": 4},
    {"ip": "172.16.0.1", "suspicious_packets": 1},
    {"ip": "203.0.113.5", "suspicious_packets": 7}
]

#Solution
for bucle in suspicious_activity:
    ip = bucle.get("ip")
    suspicious_packets = bucle.get("suspicious_packets")
    if ip not in allowed_ips:
        print("IP",ip,"needs further investigation:", suspicious_packets, "suspicious packets.")


#Result
'''
IP 192.168.0.2 needs further investigation: 5 suspicious packets.
IP 192.168.0.3 needs further investigation: 4 suspicious packets.
IP 203.0.113.5 needs further investigation: 7 suspicious packets.
'''

# Hardcoded login attempts: 0 = fail, 1 = success
login_attempts = [
    [1, 0, 0, 1, 0, 0, 0],  # User 1
    [0, 1, 1],              # User 2
    [0, 0, 0, 0],           # User 3
    [0, 1, 0, 0],           # User 4
]

# Solution
#> mayor que
contadorTry = 0

while contadorTry < len(login_attempts):
    zerouno = login_attempts[contadorTry]
    tryFailed = zerouno.count(0)#Cuenta todos los zeros de la linea de la lista

    if tryFailed < 3:
        print("Number of flagged users:", contadorTry +1)#+1 es porque la lista cuenta desde el 0, y queremos que sea desde el 1

    contadorTry +=1

'''
Number of flagged users: 2
'''

# Packet data
packet_log = [
    "GET /index.html",
    "malware detected in POST request",
    "Checking for updates",
    "Potential attack detected in payload",
    "Normal traffic"
]

# Solution
number = 0
for buclePacket in packet_log:
    #print(packet_log[number])
    if "attack" in packet_log[number]: #comrpuebo la palabra si esta en alguna cadena del packet log
        print("Packet block:", packet_log[number])
    elif "malware" in packet_log[number]: 
        print("Packet block:", packet_log[number])
    else:
        print("Packet allowed:", packet_log[number])
    number+=1

'''
Packet allowed: GET /index.html
Packet blocked: malware detected in POST request
Packet allowed: Checking for updates
Packet blocked: Potential attack detected in payload
Packet allowed: Normal traffic
'''

# Hardcoded log of access attempts
access_attempts = ["192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
                   "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.2"]

# Solution
maxRepeticion = 3
nonSpamCount = 0
for bucleIpUnique in set(access_attempts): #set para contar las no repetidas (elemento unico de set)
    countIp = access_attempts.count(bucleIpUnique)
    if countIp >= maxRepeticion:
        print(bucleIpUnique, "This IP appears more", maxRepeticion, "times")
    else:
        nonSpamCount += 1
        print("This IP is not SPAM", bucleIpUnique)
print("Number of flagged IPs:", nonSpamCount)


'''
Number of flagged IPs: 1            
'''


# Hardcoded list of passwords
passwords = ["123", "password", "strongpassword123", "qwerty", "admin", "ilovecoding12345"]
weak = 0
medium = 0
strong = 0
for buclePassword in passwords:
    if len(buclePassword) < 6:
        print("MIERDACA")
        weak += 1
    elif 6 >= len(buclePassword) <= 10:
        print("TABUEN")
        medium += 1
    else:
        print("SEGURATED")
        strong += 1
print ("Weak passwords:", weak,"\nMedium passwords:", medium,"\nStrong passwords:", strong)

'''
Expected output 
Weak passwords: 2
Medium passwords: 2
Strong passwords: 2
'''

# Hardcoded network logs
logs = [
    "User login successful",
    "Access denied on port 22",
    "System error: disk full",
    "User login failure",
    "Normal activity detected",
    "Permission denied for user"
]

badWords = ["error", "failure","denied"]
contadorBad = 0
for bucleLog in logs:
    for bucleWords in badWords:
        if bucleWords in bucleLog:
            contadorBad += 1
        else:
            pass
print("Number of logs flagged for review:", contadorBad)


'''
Number of logs flagged for review: 4
'''
# Hardcoded list of login attempts (each list represents one user's attempts)
user_attempts = [
    [1, 0, 0, 1],      # User 1
    [0, 1, 1],         # User 2
    [0, 0, 1, 0],      # User 3
    [1, 1, 1, 0],      # User 4
]
suspiciusCount = 0

for bucleUser in user_attempts:
    indiceLista = 0
    while indiceLista < len(bucleUser) - 2:
        if bucleUser[indiceLista] == 0 and bucleUser [indiceLista + 1] == 0 and bucleUser [indiceLista + 2] == 1:
            suspiciusCount += 1
            break
        indiceLista += 1
print("Number of users with suspicious login behavior:", suspiciusCount)

'''
Number of users with suspicious login behavior: 2
'''