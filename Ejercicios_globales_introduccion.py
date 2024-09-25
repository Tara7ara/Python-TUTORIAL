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
#user_roles["superuser"] #TypeError: tuple indices must be integers or slices, not str

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

