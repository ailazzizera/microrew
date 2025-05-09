#importa le librerie necessarie
import pyautogui
import random
import time
import requests
import math
import winsound

# registra il tempo di inizio
primo = time.time()

# ottiene la dimensione dello schermo
w = pyautogui.size()

# URL di una lista di parole italiane (ad esempio, da un repository GitHub)
url = "https://raw.githubusercontent.com/napolux/paroleitaliane/main/paroleitaliane/110000_parole_italiane_con_nomi_propri.txt"  # Valid URL for Italian words


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

# definisce una funzione per cliccare e scrivere una parola
def clicca_e_scrivere(x, y, parola):
    pyautogui.moveTo(x, y)
    pyautogui.click(button = "left")
    for lettera in parola:
        interval = random.uniform(0.09, 0.5)
        pyautogui.write(lettera, interval=interval)

# muove il cursore e clicca in una posizione specifica
durata = random.uniform(0.4, 0.5)  # Durata casuale
pyautogui.moveTo(1000,1050, duration=durata)
pyautogui.click(button ='left')
pyautogui.moveTo(500,55, duration=0.7)
x, y = 500, 60  #modifica le coordinate x e y per posizionare il cursore dove vuoi
time.sleep(2)

# ciclo per scrivere parole casuali
for i in range(40):
    parola_casuale = random.choice(parole_selezionate)
    pyautogui.press('backspace')
    clicca_e_scrivere(x, y, parola_casuale)
    pyautogui.press('enter')
    print(f"Scritto: {parola_casuale}")
    parole_selezionate.remove(parola_casuale)  # Rimuove la parola selezionata dal dataset
    print(f"Parole rimanenti: {len(parole_selezionate)}")  # Stampa il numero di parole rimanenti
    r = random.randint(1, 8) # Genera un numero casuale tra 1 e 8
    print(f"Attesa di {r} secondi")
    time.sleep(r) # Pausa casuale (accetta solo interi)

# registra il tempo di fine e calcola il tempo di esecuzione')
ultimo=time.time()
result= (ultimo-primo)
for i in range (3):
    winsound.Beep(400,100)  # Beep at 440 Hz for 1 second
winsound.Beep(400,450)

# tronca il risultato e lo stampa
result=math.trunc(result)
print('Exec:' + str(result) + ' sec')

