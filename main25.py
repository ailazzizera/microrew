import pyautogui
import random
import time
import requests
import math
primo = time.time()

w = pyautogui.size()

# URL di una lista di parole italiane (ad esempio, da un repository GitHub)
url = "https://raw.githubusercontent.com/napolux/paroleitaliane/refs/heads/master/paroleitaliane/280000_parole_italiane.txt"

# Scarica la lista di parole
response = requests.get(url)
if response.status_code != 200:
    print("Errore nel download della lista di parole.")
    exit()

# Estrae le parole dal testo
tutte_le_parole = response.text.splitlines()

# Filtra le parole per rimuovere duplicati e seleziona 100 parole casuali
parole_uniche = list(set(tutte_le_parole))  # Rimuove duplicati
parole_selezionate = random.sample(parole_uniche, 100)  # Seleziona 100 parole casuali

def clicca_e_scrivere(x, y, parola):
    pyautogui.moveTo(x, y)
    pyautogui.click(button = "left")
    for lettera in parola:
        pyautogui.write(lettera, interval=0.2)

pyautogui.moveTo(1000,1050)
pyautogui.click(button ='left')
pyautogui.moveTo(500,60)
x, y = 500, 60  #modifica le coordinate x e y per posizionare il cursore dove vuoi
time.sleep(2)

for i in range(40):
    parola_casuale = random.choice(parole_selezionate)
    pyautogui.press('backspace')
    clicca_e_scrivere(x, y, parola_casuale)
    pyautogui.press('enter')
    print(f"Scritto: {parola_casuale}")
    r = random.randint(1, 8)
    print(f"Attesa di {r} secondi")
    time.sleep(r)
pyautogui.write('https://rewards.bing.com/', interval=0.21)
pyautogui.press('enter')
ultimo=time.time()
result= (ultimo-primo)

result=math.trunc(result)
print('Exec:' + str(result) + ' sec')

