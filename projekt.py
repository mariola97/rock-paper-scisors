import random

scoreBota = 0
scoreKorisnika = 0
izborBota = random.randint(1,3)
#1 = kamen
#2 = papir
#3 = skare

print("Unesite 1 za kamen, 2 za papir i 3 za makaze")
izborKorisnika = int(input())
if(izborBota==izborKorisnika):
    print("Nitko nije pobjedio")
if((izborBota==1) and (izborKorisnika==2)):
    print("Izgubio si")
    scoreBota +=1
if(izborBota==1 and izborKorisnika==3):
    print("Pobjedio si")
    scoreKorisnika += 1
if(izborBota==2 and izborKorisnika==3):
    print("Pobjedio si")
    scoreKorisnika += 1
if(izborBota==2 and izborKorisnika==1):
    print("Izgubio si")
    scoreBota+=0
if(izborBota==3 and izborKorisnika==1):
    print("Pobjedio si")
    scoreKorisnika+=1
if(izborBota==3 and izborKorisnika==2):
    print("Izgubio si")
    scoreBota +=1

