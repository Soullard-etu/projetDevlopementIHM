import socket
import threading

HOST = 'localhost'
PORT = 59007

def handle_client(conn, addr):
    print(f"Connexion établie avec {addr}")

    # Liste des annonces possibles et des couleurs de carte
    annonces = ["80","90","100","110","120","130","140","150","160"]
    couleurs = ["Pique","Coeur","Carreau","Trèfle"]

    try:
        while True:
            # Demander au client de faire une annonce
            conn.sendall(b"Veuillez faire une annonce (80, 90, 100, 110, 120, 130, 140, 150, 160) : ")
            annonce = conn.recv(1024).decode().strip()
            if not annonce:
                break

            # Vérifier si l'annonce est valide
            if annonce not in annonces:
                conn.sendall(b"Annonce invalide. Veuillez reessayer.\n")
                continue

            # Demander au client de choisir une couleur
            conn.sendall(b"Veuillez choisir une couleur (Pique, Coeur, Carreau, Trefle) : ")
            couleur = conn.recv(1024).decode().strip()
            if not couleur:
                break

            # Vérifier si la couleur est valide
            if couleur not in couleurs:
                conn.sendall(b"Couleur invalide. Veuillez ressayer.\n")
                continue

            # Combinaison annonce et couleur
            annonce_couleur = f"{annonce} - {couleur}"
            print(f"Joueur {addr} a choisi : {annonce_couleur}")

            # Traiter l'annonce et la couleur choisies ici, selon les règles de votre jeu

    except Exception as e:
        print(f"Erreur avec la connexion {addr}: {e}")

    finally:
        conn.close()
        print(f"Connexion avec {addr} fermée")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(4)
    print("Serveur prêt à accepter les connexions")

    while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()