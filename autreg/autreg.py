from random import*
from Omamoodul import*
n=["kika"]
p=["kik123"]
while True:
    print("1- registreerimine ")
    print("2- autoriseerimine ")
    print("3- välja ")
    print("4- muuta nimi või parool")
    print("5- unustanud parooli taastamine ")
    v=input("vali number: ")
    if v=="1":
         print("Registreerimine")
         nimi,parool=kasutaja(n,p)
         print(f" nimi ({nimi}) ja password ({p})")
    elif v=="2":
        print("autoriseerimine") 
        nimi,par_=aut(n,p)
    elif v=="3":
        print("lõpp")
        break
    elif v=="4":
        vananim=input("Kirjuta teie vana nimi: ")
        uusnimi=input("Kirjuta uue nimi, mida sa sooid: ")
        uss_nimi(n,vananim,uusnimi)
    elif v=="5":
        nimi=input("Krjuta teie login: ")
        vanasalasõna=input("Kirjuta teie vana salasõna: ")
        uussalasõna=input("Kirjuta uus salasõna: ")
        uss_salasõna(n,p,nimi,vanasalasõna,uussalasõna)
