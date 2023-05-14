import math

class funkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
   
    def rozwiaz(self):
        if(self.a == 0):
            if(self.b == 0):
                if(self.c == 0):
                    print("Funkcja ma nieskonczenie wiele rozwiazan")
                else:
                    print("Funkcja nie ma rozwiazan")
            else:
                print("Funkcja jest liniowa")
        else:
            print("Funkcja kwadratowa")
        delta = (self.b**2)-(4*self.a*self.c)
        if(delta < 0):
            print("Funkcja nie ma miejsc zerowych!")
        if(delta == 0):
            print("Funkcja ma jedno miejsce zerowe")
            miejsce = (-self.b)/2*self.a
            print("Miejsce zerowe, to: " + miejsce)
        if(delta > 0):
            print("Funkcja ma dwa miejsca zerowe")
            pierwiastek = math.sqrt(delta)
            miejsce1 = float(((-self.b)-pierwiastek)/2*self.a)
            miejsce2 = float(((-self.b)+pierwiastek)/2*self.a)
            print("Pierwsze miejsce zerowe, to: " + str(miejsce1) + ", a drugie miejsce zerowe, to: " + str(miejsce2))


print("test")
test = funkcjaKwadratowa(3, 4, 5)
print("Podaj pierwsza liczbe.")
test.a = float(input())
print("Podaj druga liczbe.")
test.b = float(input())
print("Podaj trzecia liczbe.")
test.c = float(input())
print(test.a)
print(test.rozwiaz())


##class UlamekZ:
##
##    def __init__(self, licznik, mianownik):
##        self.licznik = licznik
##        self.mianownik = mianownik
##
##    def skroc(self):
##        while b > 0:
##            r = a % b
##            a = r
##            b = b
##
##    def dodaj(self):
##       
##    def odejmij(self):
##
##    def mnoz(self):
##
##    def dziel(self):