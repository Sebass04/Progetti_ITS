import os
from dotenv import load_dotenv
load_dotenv()

CSV_PATH = os.getenv("CSV_PATHA", "ciao")

def function():
    print(CSV_PATH)

function()