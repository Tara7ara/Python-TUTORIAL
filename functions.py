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



#Write a function reset_attempts() that resets the global variable login_attempts to 0, and a function attempt_login() that increments the number of attempts. Simulate a failed login mechanism with a global login_attempts variable.

#Create a function detect_intrusion() that takes a log entry and uses a local variable suspicious to detect the words "unauthorized access" or "intrusion". If detected, return True, otherwise False.

#Write a function track_failed_logins() that tracks the number of failed login attempts globally. Each time the function is called, it increments the count. The function should print the total number of failed attempts.