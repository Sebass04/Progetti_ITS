import random
import os 
from dotenv import load_dotenv
load_dotenv()

def play_game():
    print(os.getenv("Numero_tentativi"))