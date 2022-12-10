import random

def numeroCasuale():
    random.seed()
    return random.randint(0,2)

def elementoCasuale():
    random.seed()
    return random.randint(1,2)

def indovinaIndice(numRiga,numCol, indovinato):    
    rigaIndovinata = False
    colIndovinata = False
    indovinato = False

    while True:

        while True:
            try:
                elementoOutputRiga = int(input("Riga elemento nella matrice: "))
                if elementoOutputRiga == numRiga:
                    print("Riga indovinata con successo")
                    rigaIndovinata = True
                    break
                else:
                    print("Riga non indovinata")
            except ValueError:
                print("Si prega di inserire un numero intero valido per la riga")

        while True:
            try:
                elementoOutputCol = int(input("Colonna elemento nella matrice: "))
                if elementoOutputCol == numCol:
                    print("Colonna indovinata con successo")
                    colIndovinata = True
                    break
                else:
                    print("Colonna non indovinata")
            except ValueError:
                print("Si prega di inserire un numero intero valido per la colonna")

        if rigaIndovinata == True and colIndovinata == True:
            indovinato = True
            break

    return (indovinato)

# Inizializzazione variabili
numRiga = 0
numCol = 0
elemento = 0
indovinato = False

# Assegnazione dei valori casuali alle variabili
numRiga = numeroCasuale()
numCol = numeroCasuale()
elemento = elementoCasuale()


# Crea una lista vuota che rappresenta la matrice
matrice = []

# Aggiungi gli elementi della matrice alla lista come elementi della lista
matrice.append([0, 0, 0])
matrice.append([0, 0, 0])
matrice.append([0, 0, 0])

# Voglio far si che randomicamente in un elemento della matrice compaia un elemento

matrice[numRiga][numCol] = elemento


# Stampa la matrice in formato matriciale
for riga in matrice:
    print(riga)

# Stampa i numRiga e numCol
print("numRiga: " + str(numRiga))
print("numColonna: " + str(numCol))


# Voglio chiedere all'utente dove si trovi l'elemento diverso nella matrice
# Chiedo quindi l'indice dell'elemento

indovinato = indovinaIndice(numRiga, numCol, indovinato)
print("Complimenti, hai indovinato entrambi gli indici")
