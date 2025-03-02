# Bot per fare ricerche per Microsoft Reward
Il bot utilizza il modulo *pyautogui* per muovere il mouse e cliccare a determinate coordinate. Queste devono essere configurate rispetto a:
1. Dove si trova l'icona di *Microsoft Edge*;
2. Le altre in corrispondenza della barra degli indirizzi del browser.

## Funzionamento del codice
Il codice permette di creare, a partire da un dataset di n. 280000 parole italiane disponibile su *GitHub* a titolo gratuito, di estrarre casualmente 100 parole e creare una lista (ogni volta che il codice viene eseguito, un nuovo dataset viene creato).
Dopo aver aperto il browser, il codice ciclerà per 40 volte scrivendo lettera per lettera la parola scelta randomicamente presente nella lista imitando la scrittura umana. (In futuro il bot sceglierà parole uniche evitando di scrivere doppioni che non vengono calcolati come *ricerca* dal software di MR)
Al termine della parola, il bot sceglie in modo randomico una tempistica tra 1 e 8 secondi eludendo il cooldown che alla data della pubblicazione è circa 3-5 secondi dopo 3 richerche o simile.  
Al termine, il bot riporterà alla pagina principale di MR
