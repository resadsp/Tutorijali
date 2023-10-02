varijabla1 = "tekstualna varijabla"
varijabla2 = 30
print(type(varijabla1))
print(type(varijabla2))
x = 7
y = 10.9
z = 2j
print(type(x))
print(type(y))
print(type(z))
a = float(x)
print(a)
b = int(y)
print(b)
c = complex(x)
print(c)
jednostruki = 'RESAD'
dvostruki = "RESAD"
print(jednostruki)
print(dvostruki)
print("Ja idem u skolu \"DESANKA MAKSIMOVIC\" u Beogradu")
A, B, C = "resad", "maida", "atija" #treba da se vodi racuna da su jednaki broj promenjivih i broj vrednosti koje dodeljujemo promenljivim
print(A)
print(B)
print(C)
X = Y = Z = "porodica"
print(X)
print(Y)
print(Z)
porodica = ["otac", "majka", "deca"]
e, f, g = porodica #a moglo je da pise e, f, g = "otac", "majka", "deca"
print(e)
print(f)
print(g)
E = "RESAD"
F = "MAIDA"
G = "ATIJA"
print(E+" "+F+" "+G) #POSTOJI I DRUGI, LAKSI NACIN GDE BI SMO PISALI "RESAD " "MAIDA " "ATIJA"
print(E,F,G) #AUTOMATSKI PRAVI RAZMAK IZMEDU VREDNOSTI PROMENLJIVIH
rec = "rec"
broj = 5
#print(rec+broj), ovo nece da radi
print(rec, broj) #ovo radi i automatski pravi razmak izmedju vrednosti promenljivih na izlazu
globalna = "ovo je jedna globalna varijabla"
def myfunc():
    print("Napravili smo jednu globalnu promenljivu. "+globalna)
myfunc()
def funkcija():
    global lokalna
    lokalna = "Ovo je jedna lokalna promenljiva"
funkcija()
print(lokalna)
g = 10
print(type(g))
g = float(10)
print(g)
print(type(g))
f = 10.9
print(f)
f = int(10.9)
print(f)
print(type(f))
import random
print(random.randrange(1,20))
l = str(2)
print(type(l))
k = "2"
print(type(k))
niz = "ovo je jedan niz" #pocetni elemenat je na nultoj poziciji
print(niz[0])
print(niz[10]) #racunaju se i razmaci, tj space
print(len(niz))
for x in niz:
    print(x)
print("edan" in niz) #vraca booleon vrijednost, true ili false
if "edan" in niz:
    print("postoji rec edan u nizu niz")
if "edana" not in niz:
    print("rec edana ne postoji u nizu")
rezanje = " Ovo je Tekst koji treba izrezati"
print(rezanje[1:5]) #pocetni indeks je ukljucen, krajnji indeks nije ukljucen u rezanje
print(rezanje[:5])
print(rezanje[5:])
print(rezanje.upper()) #vraca sve velika slova
print(rezanje.lower()) #vraca sve mala slova
print(rezanje.strip()) #uklanja razmak od pocetka navodnika do pocetka teksta
print(rezanje.replace("O","J")) #menja slovo O sa slovom J. pravi razliku izmedju velikog i malog slova
print(rezanje.replace("koji","KOJI")) #pravi razliku izmedju velikih i malih slova
print(rezanje.split(","))
spa = "Zdravo"
janje = "svijete"
print(spa+janje)
spa = "Zdravo " #prvi nacin pravljenje razmaka izmedju spojenih rijeci
janje = "svijete"
print(spa+janje)
print(spa+""+janje) #drugi nacin pravljenja razmaka izmedju spojenih rijeci
god = 29 #0
dete = 1 #1
broj = 3 #2
tekst = "Ja sam Resad, imam {} godina, imam {} dijete i moja porodica ima {} clana." #{}-cuvar mesta za vrednost
print(tekst.format(god, dete, broj)) #mozemo imati neogranicen broj argumenata koji se stavljaju u odgovarajuca mesta koja nam cuvaju cuvari mesta
tekst2 = "Ja sam Resad, imam {} dijete, moja porodica ima {} clana i imam {} godina." #ovo nije u redu
print(tekst2.format(god, dete, broj))
tekst3 = "Ja sam Resad, imam {1} dijete, moja porodica ima {2} clana i imam {0} godina." #ovo je u redu
print(tekst3.format(god, dete, broj))
print('Navijam za fudbalski klub "Man.Utd" iz Engleske') #ovo je prvi nacin
print("Navijam za fudbalski klub \"Man.Utd\" iz Engleske") #ovo je drugi nacin koji se cesce koristi
#NAPOMENA: SVE METODE STRING VRACAJU NOVE VRIJEDNOSTI, ONE NE MIJENJAJU ORIGINALNI STRING NIZ
print(bool("tacno"))
print(bool(-1123))
print(bool(True))
print(bool(["tacno","netacno"]))
print(bool(""))
print(bool())
print(bool([]))
print(bool(False))
print(bool(0))
#funkcija koja vraca 0 ili False je false, a funkcija koja vraca bilo koji broj razlicit od 0 ili True je true
def funkcija():
    return 1  #i u funkciji vazi isto kao i van nje. vraca false ako je return ili 0 ili False ili "" ili [] ili {} ili None....
print(bool(funkcija()))
def funkcija():
    return "abc" #vraca true kao i kad je true van funkcije
print(bool(funkcija()))
def funkcija():
    return ""
print(bool(funkcija()))
def funkcija():
    return False
print(bool(funkcija()))
def funkcija():
    return 0
print(bool(funkcija()))
provera = 120
print(isinstance(provera, int)) #ako je vrednost int vrati true
provera2 = 120.3
print(isinstance(provera2, float)) #ako je vrednost2 float vratice true a ako nije onda false
vrednost3 = 1234.12345
if isinstance(vrednost3, int): #ako je vreijednost celobrojna odradi if petlju
    print("data vrednost je celobrojna")
else:  #ako nije onda je napravi da jeste celobrojna i istampaj tekst kao i nju
    vrednost3 = int(vrednost3)
    print("Napravili smo celobrojnu vrijednost")
    print(vrednost3)
#OPERATORI
print(5+2) #sabiranje
print(5-25) #oduzimanje
print(5*2) #mnozenje
print(5/2) #dijenje sa decimalom
print(5**3)#5 na 3 (5*5*5)
print(5%3) #ostatak pri celobrojnom dijeljenju
print(17//2) #koliko se puta celobrojno drugi broj sadrzi u prvi broj
print(17//24) #koliko se puta celobrojno drugi broj sadrzi u prvi broj. ako je drugi broj veci od prvog onda je izlazna vrijednost nula
d = 2 #2
d +=20 # d = d + 20 = 22
d -=20 # d = d - 20, isto vazi  i za *=, /=, //=, **=, %=...
#operator poredjenja daje kao vrednost ili true ili false
n = 7
m = 11
print(n==m) #jednakost
print(n!=m) #nejednakost
print(n>m) #vece
print(n<m) #manje
print(7>=7) #vece ili jednako, vraca true
print(7<=6) #manje ili jednako, vraca false u ovom slucaju
#logicki operatori takodje imaju true ili false kao izlaz
p = 5
print(p>3 and p<10) #moraju da su ispunjeni svi uslovi
print(p>3 or p<10) #treba da je ispuunjen samo jedan od svih zadatih uslova
print(p>1 and p>2 and p>10) #vratice false jer nisu ispunjeni svi zadati uslovi
print(p>10 or p>20 or p>100 or p>2) #vratice true jer ispunjen jedan uslov, jedan ili vise
print(not(p>3 and p<10)) #obrunti rezultat. Vraca false ako je true i vraca true ako je false
print(not(p>10 or p>20 or p>100 or p>2)) #iako je uslov true vratice false zbog kljucne rijeci not
 



