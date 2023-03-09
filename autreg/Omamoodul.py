from random import*

def kasutaja(n:list,p:list):
    """siin on registreerimine
    """
    print("sisestada andmeid või sa tahad juhuslikult?")
    b=input("vastus: ")
    if b=="sisetage":
        nimi=input("sisetage nimi: ")       
    print("Kas sa tahad sisetada parool või random?")
    b=input("vastus:")
    if b=="sisetage":
        nimi=input("sisetage nimi: ")      
        parool=input("sisetage  parool maksimalselt 8 värtused: ")
        n=len(parool)
        while n<8:
            parool=input("parool on lühike. Palun kirjuta veel: ")
            n=len(parool)
    elif b=="random":
        login=input("Kirjutage teie nimi: ")
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        #print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        #print(str4)
        ls = list(str4)
        #print(ls)
        shuffle(ls)
        #print(ls)
        # Извлекаем из списка 8 произвольных значений
        parool= "".join([choice(ls) for x in range(8)])
    
    n.append(nimi)
    p.append(parool)
    return nimi,parool
def aut(n:list,p:list):
    """siin on autoriseerimine 
    """
    print("sisetage nimi salasõna")
    nim=input("nimi: ")
    par=input("parool: ")
    if nim in n and par in p:
        print("Tere tulemast!")
    else: 
        print("Ebaõiged andmed")
    return nim, par

def uss_nimi(n:list,vananim:list,uusnimi:list):
    """Siin saab oma nimi kustutada.
    """
    if vananim in n:
        index=n.index(vananim)
        n[index]=uusnimi
        print("nimi on muudetud.")
    else:
        print("viga!")

def uss_salasõna(n,p,nimi,vanasalasõna,uussalasõna):
    """Siin saab oma parooli kustutada.
    """
    if nimi in n and vanasalasõna in p:
        index=n.index(nimi)
        p[index]=uussalasõna
        print("salasõna on muudetud")
    else:
        print("viga!")
        
def nimii(n,p,nimo):
    """Siin saab vaadata oma vana parooli.
    """
    if nimo in n:
        index=n.index(nimo)
        print(f"vana salasõna on:",p[index])
    else: 
        print("viga!")





