import socket
import json


HOST = 'localhost'
PORT = 59007

def recevoir_message(conn):
    message = conn.recv(1024).decode()
    return message

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        # Envoyer le nom du joueur au serveur
        nom = input("Rentrez votre nom : ")
        D = {"nom": nom}
        print(D)
        d = json.dumps(D)
        d = d.encode()
        s.sendall(d)

        while True:
            # Recevoir le message du serveur et afficher
            message = recevoir_message(s)
            print(message.strip())

            # Envoyer la réponse du joueur au serveur
            reponse = input()
            s.sendall(reponse.encode())