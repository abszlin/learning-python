print("Ile wynosi twoja masa ciała?")
masa=input()
print("Jaki masz wzrost w cm?")
wzrost=input()
print("Ile masz lat?")
wiek=input()
print("Ile wynosi twoja podstawa, gdzie: \n"
"Praca siedząca, brak dodatkowej aktywności fizycznej	1,2 \n"
"Praca niefizyczna, mało aktywny tryb życia	1,4 \n"
"Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu	1,6 \n"
"Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	1,8 \n"
"Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu	2,0")
podstawa=input()
KK=10*float(masa)+6.25*float(wzrost)-5*float(wiek)
print("Twoje zapotrzebowanie wynosi",KK)
