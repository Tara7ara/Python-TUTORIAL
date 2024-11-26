access_attempts = ["192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
                   "192.168.0.2", "192.168.0.2", "192.168.0.3", "192.168.0.3", "192.168.0.2"]

maxAcces = 3
contadorNoSpam = 0
for x in set(access_attempts):
    if access_attempts.count(x) > maxAcces:
        contadorNoSpam += 1
print("Number of flagged IPs:", contadorNoSpam)
