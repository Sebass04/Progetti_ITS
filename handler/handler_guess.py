import random
import os
from dotenv import load_dotenv

load_dotenv()

def play_game():
    print(os.getenv("Numero_tentativi"))

    numero_segreto = random.randint(1, 100)
    tentativi_effettuati = 0
    limite_tentativi = 10
    indovinato = False

    print("Gioco dell'indovina numero!")
    print("Sto pensando a un numero tra 1 e 100. Riuscirai a indovinarlo?")
    print("Hai un numero limitato di tentativi, quindi scegli saggiamente!")

    input("Premi Invio per iniziare...")

    while limite_tentativi > 0:
        try:
            tentativo = int(input("Inserisci il tuo tentativo: "))

            tentativi_effettuati += 1
            limite_tentativi -= 1

            if tentativo < numero_segreto:
                print("Troppo basso! Riprova.")
            elif tentativo > numero_segreto:
                print("Troppo alto! Riprova.")
            else:
                print(
                    f"Congratulazioni! Hai indovinato il numero in {tentativi_effettuati} tentativi."
                )
                indovinato = True
                break

            print(f"Hai {limite_tentativi} tentativi rimasti.")

        except ValueError:
            print("Per favore, inserisci un numero valido.")

    if indovinato:
        print(f"Il numero segreto era: {numero_segreto}. Grazie per aver giocato!")
    else:
        print(f"Tentativi esauriti! Il numero segreto era {numero_segreto}.")

    input("Premi Invio per uscire...")

play_game()