#Mates

#1
t = 2.5
a = 9.8
vf= 0 + a * t
v= (vf +0) / 2
d = v * t
print("distance =", d)

#2
g = a
m = 24.5
a = 4.5
N = 150
F = N * m * g + m * a
print ("Friction = ", F)

#3
x1 = 4.5
y1 = -5.5
x2 = 6.6
y2 = -6.5
point = (y2 -y1) / (x2 -x1)
print ("The conexion in this 2 lines = ", point)

#4
write = "123456789" 
reverseWrite = write [::-1]
print(write, "=/= ", reverseWrite)


#TUPLAS

#1. Create a tuple named admin_credentials that holds the values "admin", "root", and "P@ssw0rd". Print the tuple and its length.
admin_credentials = ("admin", "root", "P@ssw0rd")
print(admin_credentials, len(admin_credentials))

#2. Given the tuple ports = (22, 443, 80, 21, 8080), print the first and last port. Check if port 22 is in the tuple.
ports = (22, 443, 80, 21, 8080)
print(ports[0], ports[4])
for x in ports:
    if x == 22:
        print ("Port 22 is here")
        break

#3. Try to modify the second value in the tuple user_roles = ("admin", "user", "guest") to "superuser". What error do you get?
user_roles = ("admin", "user", "guest")
user_roles["superuser"] #TypeError: tuple indices must be integers or slices, not str

#4. Given the tuple server_info = ("192.168.1.10", "web_server", "active"), unpack it into three variables: ip, role, and status, then print each variable.
server_info = ("192.168.1.10", "web_server", "active")
ip, role, status = server_info
print(ip, role, status)

#Diccionarios

#5. Create a dictionary firewall_rules where: "inbound" key maps to the list ["SSH", "HTTPS"]. "outbound" key maps to the list ["DNS", "SMTP"]. Print the dictionary.
firewall_rules = {
    "inbound": ["SSH", "HTTPS"],
    "outbound": ["DNS", "SMTP"],}
print(firewall_rules)

#6. Using the firewall_rules dictionary from the previous exercise, print all the inbound and outbound rules. Also, use the .get() method to safely access a non-existing key "blocked".
print(firewall_rules.get("inbound"), firewall_rules.get("outbound"), firewall_rules.get("blocked"))

#7. Add a new key "blocked" to the firewall_rules dictionary with the value ["FTP", "Telnet"] . Then, print the updated dictionary.
firewall_rules["blocked"] = ["FTP", "Telnet"]
print(firewall_rules)

#8. Create a dictionary attack_signatures where each attack type ("SQL Injection", "Cross-Site Script- ing (XSS)", "Denial of Service (DoS)") maps to a corresponding signature (SQL query, JavaScript code, traffic overload). Add a new attack signature for "Brute Force".
attack_signatures = {
   "SQL query" : ["SQL Injection"],
   "JavaScript code" : ["Cross-Site Script- ing (XSS)"],
   "traffic overload" : ["Denial of Service (DoS)"]
   }
attack_signatures ["Brute Force"] = ["passwordrack"]
print(attack_signatures)

#SETS

#9. Create a set called detected_ips that contains three IP addresses: "192.168.1.1", "10.0.0.2", "192.168.1.1". Print the set and observe the uniqueness property.
detected_ips = {"192.168.1.1", "10.0.0.2", "192.168.1.1"}
print(detected_ips) # {'192.168.1.1', '10.0.0.2'}

#10. Create two sets: secure_ips = {"192.168.1.1", "10.0.0.2"} insecure_ips = {"10.0.0.2", "172.16.0.1"} Perform a union and intersection of the two sets. Print the results.
secure_ips = {"192.168.1.1", "10.0.0.2"} 
insecure_ips = {"10.0.0.2", "172.16.0.1"}
intersection = secure_ips | insecure_ips
union = secure_ips & insecure_ips
print(union, intersection)

#11. Using the secure_ips and insecure_ips sets from the previous exercise, find the difference between secure_ips and insecure_ips (i.e., IPs in secure_ips but not in insecure_ips).
print(secure_ips - insecure_ips)

#12. You have two sets of hashes: known_hashes = {"abc123", "def456", "ghi789"}. suspicious_hashes = {"ghi789", "xyz123", "abc123"}. Find the common hashes and the hashes that are in suspicious_hashes but not in known_hashes.
known_hashes = {"abc123", "def456", "ghi789"}
suspicious_hashes = {"ghi789", "xyz123", "abc123"}
print(known_hashes & suspicious_hashes)
print(suspicious_hashes - known_hashes)




# Hardcoded lists
allowed_ips = ["192.168.0.1", "10.0.0.1", "172.16.0.1"]
suspicious_activity = [
    {"ip": "192.168.0.2", "suspicious_packets": 5},
    {"ip": "10.0.0.1", "suspicious_packets": 2},
    {"ip": "192.168.0.3", "suspicious_packets": 4},
    {"ip": "172.16.0.1", "suspicious_packets": 1},
    {"ip": "203.0.113.5", "suspicious_packets": 7}
]

for bucleIp in suspicious_activity:
    ip = bucleIp.get("ip")
    suspiciousPackets = bucleIp.get("suspicious_packets")
    if ip not in allowed_ips:
        print("IP",ip,"needs further investigation:", suspiciousPackets, "suspicious packets.")

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


#PROFE
dangerous_words=["malware","attack"]
for packet in packet_log:
    to_block= False
    for word in dangerous_words:
        to_block=True
    if to_block:
        print("Packet", packet, "was bloqued")
    else:
        print("Packet", packet, "was allowed")

# Hardcoded log of access attempts
access_attempts = ["192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
                   "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.2"]

maxAcces = 3
contadorNoSpam = 0
for x in set(access_attempts):
    if access_attempts.count(x) > maxAcces:
        contadorNoSpam += 1
print("Number of flagged IPs:", contadorNoSpam)

'''
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

# Hardcoded list of passwords
passwords = ["123", "password", "strongpassword123", "qwerty", "admin", "ilovecoding12345"]
weak = 0
medium = 0
strong = 0
for buclePassword in passwords:
    if len(buclePassword) < 6:
        print("MIERDACA")
        weak += 1
    elif len(buclePassword) < 10:
        print("TABUEN")
        medium += 1
    else:
        print("SEGURATED")
        strong += 1
print ("Weak passwords:", weak,"\nMedium passwords:", medium,"\nStrong passwords:", strong)

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


# Hardcoded lists
allowed_ips = ["192.168.0.1", "10.0.0.1", "172.16.0.1"]
suspicious_activity = [
    {"ip": "192.168.0.2", "suspicious_packets": 5},
    {"ip": "10.0.0.1", "suspicious_packets": 2},
    {"ip": "192.168.0.3", "suspicious_packets": 4},
    {"ip": "172.16.0.1", "suspicious_packets": 1},
    {"ip": "203.0.113.5", "suspicious_packets": 7}
]

for bucleIp in suspicious_activity:
    ip = bucleIp.get("ip")
    suspiciousPackets = bucleIp.get("suspicious_packets")
    if ip not in allowed_ips:
        print("IP",ip,"needs further investigation:", suspiciousPackets, "suspicious packets.")

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


#PROFE
dangerous_words=["malware","attack"]
for packet in packet_log:
    to_block= False
    for word in dangerous_words:
        to_block=True
    if to_block:
        print("Packet", packet, "was bloqued")
    else:
        print("Packet", packet, "was allowed")

# Hardcoded log of access attempts
access_attempts = ["192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
                   "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.2"]

maxAcces = 3
contadorNoSpam = 0
for x in set(access_attempts):
    if access_attempts.count(x) > maxAcces:
        contadorNoSpam += 1
print("Number of flagged IPs:", contadorNoSpam)

'''
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

# Hardcoded list of passwords
passwords = ["123", "password", "strongpassword123", "qwerty", "admin", "ilovecoding12345"]
weak = 0
medium = 0
strong = 0
for buclePassword in passwords:
    if len(buclePassword) < 6:
        print("MIERDACA")
        weak += 1
    elif len(buclePassword) < 10:
        print("TABUEN")
        medium += 1
    else:
        print("SEGURATED")
        strong += 1
print ("Weak passwords:", weak,"\nMedium passwords:", medium,"\nStrong passwords:", strong)

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





#CONTROL FLOW

#Ejercicio 1
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

def nombreFuncion(number): #se crea la funcion con x parametros
    result = number+2
    return result

print(nombreFuncion(10))


suspicious_ips = ["192.168.1.100", "10.0.0.5", "203.0.113.50"]
def is_suspicious_ip(ip):
    if ip in suspicious_ips:
        return True
    return False

# Call the function to check
ip_to_check = "10.0.0.5"
result = is_suspicious_ip(ip_to_check)
print(f"Is {ip_to_check} a suspicious IP? {result}")

# Define a function to log security alerts
def log_security_alert(log_entry):
    if "malware" in log_entry or "attack" in log_entry:
        print(f"Security Alert: Detected threat in log - {log_entry}")
    else:
        print("Log entry is safe.")

log_security_alert("malware detected in network traffic")

#EJERCICIOS
#Write a function block_ip(ip) that takes an IP address as input and prints "IP Blocked" if the IP is in the blocklist, 
# otherwise print "IP Safe". Use this list of blocked IPs: ["192.168.1.5", "10.0.0.2", "203.0.113.7"].
def block_ip(ip):
    badIps = ["192.168.1.5", "10.0.0.2", "203.0.113.7"]
    if ip in badIps:
        print("Ip", ip, "es maliciosa")
    else:
        print("Ip", ip, "es BUENARDA")

block_ip("192.168.1.3")

#Define a function check_vulnerability(log_entry) that checks if a log entry contains the word "vulnerability". 
# If so, it should return "Vulnerability Found", otherwise it should return "No Vulnerability".
def check_vulnerability(log_entry):
    if "vulnerability" in log_entry:
        print("Vulnerability Found")
    else:
        print("No Vulnerability")

check_vulnerability("vulnerability")

#Create a function has_sql_injection(query) that checks if a given SQL query contains an SQL injection attempt (e.g., ' OR '1'='1). 
# It should return True if an injection is found, otherwise return False.
def has_sql_injection(query):
    inyection = ["' OR '1'='1"]

    if query in inyection:
        print("SQL DETECTED")
        return True
    else:
        print("NO SQL INJECTION DETECTED")
        return False
    
has_sql_injection("' OR '1'='1")

#Write a function detect_ddos(ip, traffic) that takes an IP address and the amount of traffic (in bytes). If the traffic is greater than 1000 bytes, 
# print "Potential DDoS attack from {ip}", otherwise print "Normal traffic from {ip}".

def detect_ddos(ip, traffic):
    if traffic > 1000:
        print(f"Potential DDoS attack from {ip}")
    else:
        print(f"Normal traffic from {ip}")
detect_ddos("10.65.32.0",10)

#Define a function xor_encrypt(text, key) that takes a string text and an integer key, and returns the XOR-encrypted result of the text 
# (you can use ord() and chr() for character manipulation).
def xor_encrypt(text, key):
    encripted = [chr(ord(x) + key) for x in text]
    print(encripted)
    decript = [chr(ord(x) - key) for x in encripted]
    print(decript)

xor_encrypt("prueba", 123)
#Create a function password_strength(password) that takes a password as a parameter and returns:
# "Weak" if the password is less than 6 characters.
# "Medium" if the password is between 6 and 10 characters.
# "Strong" if the password is more than 10 characters.
def password_strength(password):
    if len(password) < 6:
        print(f"PASSWORD VERY BAD: {password}")
    elif len(password) < 10:
        print(f"GOOD PASSWORD: {password}")
    else:
        print(f"PERFECT, IT'S A  PERFECT PASSWORD: {password}, I TAKED TIS PASWORD BECAUSE IM INDIAN SCAMEEEEEEEEEEER")

password_strength("Hola")


# List of 100 logged IP addresses (simulating a log file)
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

# Write the code here
suspiciousIP = "203.0.113.5"

for x in ip_log:
    if x == suspiciousIP:
        print("The suspicius IP is here")
        break
    else:
        print("The suspicius IP is not here")
# Manera del profesor
Logged = False
for logged_IPs in ip_log:
    if logged_IPs == suspiciousIP:
        Logged = True
        print("SuspiciusIP was logged in")
        break
if Logged == False:
    print("suspiciusIP did not log in")

#Ejercicio 2

#Password to check
password = 'B49Dh2qyRwXnn!8e75Z4SAd!'

#Initializing flags for each condition
uppercase = False
lowercase = False
digitcase = False
specialcase = False

#List of special characters
special_characters = ["!","@","#","$","%","^","&","*","(",")"]

#Check the length of the password
if len(password) >= 8:
    for secur in password:
        if secur.isupper():
            uppercase = True
        elif secur.islower():
            lowercase = True
        elif secur.isdigit():
            digitcase = True
        elif secur in special_characters:
            specialcase = True

    if uppercase and lowercase and digitcase and specialcase == True:
        print("The password is strong.")
    else:
        print("The password does not meet the security requirements.")
else:
    print("The password is too short. It must be at least 8 characters long.")


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
diagonal = ((width ** 2) + (height ** 2)) ** (1 / 2)

print("Perimetro:", perimeter,"\nArea:", area, "\nDiagonal:", diagonal)

#Ejercicio de interes anual

amountFinal = 1000
annualInterest = 4.25 * 0.01
monthInterest = annualInterest / 12 
totaMonth = 12 * 5
amountInitial = amountFinal / ((1 + monthInterest) ** totaMonth)
print ("The initial deposit is: ", amountInitial) 
#vf = (v1 * (1 + im) ** m)

#Ejemplos
precio = 2
print("Cuesta:", precio) #--> string K
print(f"Cuesta: {precio}") #--> string f

#Cosas de clases
name = 'John'
age = 18
height = 1.78
city = 'Barcelona'
studiant = list([name, age, city, height])
print(studiant)
print(studiant[2:5])




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