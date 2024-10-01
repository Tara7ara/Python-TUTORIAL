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
'''
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
'''

#Ejercicio 2

# Password to check
password = 'B49Dh2qyRwXnn8e75Z4SAd'

# Initializing flags for each condition
uppercase = False
lowercase = False
digitcase = False
specialcase = False

# List of special characters
special_characters = "!@#$%^&*()"

# Check the length of the password
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

    if uppercase and lowercase and digitcase and specialcase:
        print("The password is strong.")
    else:
        print("The password does not meet the security requirements.")
else:
    print("The password is too short. It must be at least 8 characters long.")