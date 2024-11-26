def generate_token():
    import random, string
    from datetime import datetime

    #Create dictionary
    generalDictionary = {}

    #Añadimos el token
    generalDictionary["Token"] = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    #añadimos el tiempo
    generalDictionary["Time"] = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    #print(generalDictionary)
    return generalDictionary


def log_token():
    #Diccionario a str
    token = generate_token()
    strToken = str(token)

    #Crear el archivo
    fp = open('Token_logs.txt', 'a')
    fp.write(strToken)
    fp.close()
    print("DOCUMENTO ESCRITO")





#Include Timestamp: The function should return a dictionary containing the token and the current timestamp (using datetime).