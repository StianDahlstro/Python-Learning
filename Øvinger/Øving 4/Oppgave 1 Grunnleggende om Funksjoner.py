# Oppgave 1
# Grunnleggende om funksjoner

# A)
def siksak():
    print()                                         
    print("**  **  **  **  **  **  **  **  **")     
    print("  **  **  **  **  **  **  **  **")       
    print()            
                      
print("Data fra spørreundersøkelse")
siksak()   
print("Del 1: ... div. data her, ikke vist")
siksak()                                       
print("Del 2: ... mer data ...")
siksak()                                        
print("Del 3: ... enda mer data ...")
siksak()                                     
print("Del 4: ... ytterligere data ...")

# B) & C)
def komparativ(adj):
    if len(adj) >= 8:
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
  
def superlativ(adj):
    if len(adj) >= 8:
        svar = "mest " + adj
    else:
        svar = adj + "est"
    return svar

def main():
    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")
    print("Jeg er faktisk", superlativ(adj), "i hele verden.")
 
    adj = input("Skriv inn et adjektiv: ")
    svar = input("Hva er komparativ for " + adj + "? ")
    fasit = komparativ(adj)
    if svar == fasit:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit)
  
    sup_adj = input(f'Hva er superlativet for {adj}? ')
    sup_fasit = superlativ(adj)
    if sup_adj == sup_fasit:
        print('Korrekt!')
    else:
        print('Desverre er det feil.')

main()