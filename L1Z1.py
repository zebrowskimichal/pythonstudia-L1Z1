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

class UlamekZ:

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def skroc(self):
        wynik = math.gcd(self.licznik, self.mianownik)
        self.licznik //= wynik
        self.mianownik //= wynik
        print("Skrocony ulamek: " + str(self.licznik) + "/" + str(self.mianownik))
        print("")

    @staticmethod
    def dodaj(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = ((l1.licznik * l2.mianownik) + (l2.licznik * l1.mianownik))
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print("Wynik dodawania ulamkow: " + str(l1.licznik) + "/" + str(l1.mianownik) + " i " + str(l2.licznik) + "/" + str(l2.mianownik) + " daje wynik: ")
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc()
    
    @staticmethod
    def odejmij(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = ((l1.licznik * l2.mianownik) - (l2.licznik * l1.mianownik))
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print("Wynik odejmowania ulamkow: " + str(l1.licznik) + "/" + str(l1.mianownik) + " i " + str(l2.licznik) + "/" + str(l2.mianownik) + " daje wynik: ")
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc() 

    @staticmethod
    def mnoz(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = l1.licznik * l2.licznik
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print("Wynik mnozenia ulamkow: " + str(l1.licznik) + "/" + str(l1.mianownik) + " i " + str(l2.licznik) + "/" + str(l2.mianownik) + " daje wynik: ")
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc() 

    @staticmethod
    def dziel(l1, l2):
        mianownikWynik = l1.mianownik * l2.licznik
        licznikWynik = l1.licznik * l2.mianownik
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print("Wynik mnozenia ulamkow: " + str(l1.licznik) + "/" + str(l1.mianownik) + " i " + str(l2.licznik) + "/" + str(l2.mianownik) + " daje wynik: ")
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc() 


def main():
    print("Z ktorej klasy chcesz skorzystac?")
    print("1: funkcja kwadratowa")
    print("2: UlamekZ")
    wybor = str(input("Twoj wybor: "))

    while not(wybor == "1" or wybor == "2"):
        print("Zly wybor!")
        wybor = str(input("Twoj wybor: "))

    if(wybor == "1"):
        print("Wybrales funckje kwadratowa")
        print("Wpisz 3 liczby!")
        a1 = float(input("Liczba 1: "))
        b1 = float(input("Liczba 2: "))
        c1 = float(input("Liczba 3: "))
        obiekt = funkcjaKwadratowa(a1, b1 ,c1)
        print(obiekt.rozwiaz())
        main()

    if(wybor == "2"):
        print("Wybrales funckje kwadratowa")
        print("Co chcesz zrobic?")
        print("1: Skrocic ulamek")
        print("2: dzialania na ulamkach")
        wybor2 = str(input("Twoj wybor: "))
        while not(wybor2 == "1" or wybor2 == "2"):
            print("Zly wybor! Twoj wybor 1 czy 2: ")
            wybor2 = str(input())

        if(wybor2 == "1"):
            print("Wybrales skracanie ulamka")
            try: 
                print("Licznik: ")
                licznik = int(input())
                print("Mianownik: ")
                mianownik = int(input())
                obiekt = UlamekZ(licznik, mianownik)
                print(obiekt.skroc())
                main()
            except ValueError:
                print("Wpisz liczby!?")
                print("")
                main()

        if(wybor == "2"):
            print("Wybrales dzialania na ulamkach")
            print("Wybierz dzialanie:")
            print("1: dodawanie")
            print("2: odejmowanie")
            print("3: mnozenie")
            print("4: dzielenie")
            wybor3 = input("Twoj wybor: ")
            while not(wybor3 == "1" or wybor3 == "2" or wybor3 == "3" or wybor3 == "4"):
                print("Zly wybor!")
                wybor3 = input("Twoj wybor: ")
            
            ##dodawanie
            if(wybor3 == "1"):
                print("Wybrales dodawanie ulamkow")
                try: 
                    print("Licznik1: ")
                    licznik1 = int(input())
                    print("Mianownik1: ")
                    mianownik1 = int(input())
                    print("Licznik2: ")
                    licznik2 = int(input())
                    print("Mianownik2: ")
                    mianownik2 = int(input())
                    l1 = UlamekZ(licznik1, mianownik1)
                    l2 = UlamekZ(licznik2, mianownik2)
                    print(UlamekZ.dodaj(l1, l2))
                    main()
                except ValueError:
                    print("Wpisz liczby!?")
                    print("")
                    main()

            ##odejmowanie
            if(wybor3 == "2"):
                print("Wybrales odejmowanie ulamkow")
                try: 
                    print("Licznik1: ")
                    licznik1 = int(input())
                    print("Mianownik1: ")
                    mianownik1 = int(input())
                    print("Licznik2: ")
                    licznik2 = int(input())
                    print("Mianownik2: ")
                    mianownik2 = int(input())
                    l1 = UlamekZ(licznik1, mianownik1)
                    l2 = UlamekZ(licznik2, mianownik2)
                    print(UlamekZ.odejmij(l1, l2))
                    main()
                except ValueError:
                    print("Wpisz liczby!?")
                    print("")
                    main()

            ##mnozenie
            if(wybor3 == "3"):
                print("Wybrales mnozenie ulamkow")
                try: 
                    print("Licznik1: ")
                    licznik1 = int(input())
                    print("Mianownik1: ")
                    mianownik1 = int(input())
                    print("Licznik2: ")
                    licznik2 = int(input())
                    print("Mianownik2: ")
                    mianownik2 = int(input())
                    l1 = UlamekZ(licznik1, mianownik1)
                    l2 = UlamekZ(licznik2, mianownik2)
                    print(UlamekZ.mnoz(l1, l2))
                    main()
                except ValueError:
                    print("Wpisz liczby!?")
                    print("")
                    main()

            ##dzielenie
            if(wybor3 == "4"):
                print("Wybrales dzielenie ulamkow")
                try: 
                    print("Licznik1: ")
                    licznik1 = int(input())
                    print("Mianownik1: ")
                    mianownik1 = int(input())
                    print("Licznik2: ")
                    licznik2 = int(input())
                    print("Mianownik2: ")
                    mianownik2 = int(input())
                    l1 = UlamekZ(licznik1, mianownik1)
                    l2 = UlamekZ(licznik2, mianownik2)
                    print(UlamekZ.dziel(l1, l2))
                    main()
                except ValueError:
                    print("Wpisz liczby!?")
                    print("")
                    main()

##start programu                    
main() 