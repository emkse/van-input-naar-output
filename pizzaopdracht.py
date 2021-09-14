

import time

#Het menu
print("Keuzemenu:") 
print("Small")
print("Medium")
print("Large")

time.sleep(2)

aantal = int(input("Aantal pizza's: ")) #Hier kan de klant aangeven hoeveel pizza's hij/zij wilt
keuze = input("Uw keuze: ") #Hier kan de klant aangeven welke soort's hij/zij wilt

#Prijzen

Small = float(7.99)
Medium = float(12.99)
Large = float(15.00)

#Berekend hier de kosten
print("Kosten aan het bereken. Even geduld aub...")
time.sleep(4)

print(Small+Medium+Large*aantal)
time.sleep(4)


#Hier kan de klant betalen
print("Hoe wilt u betalen")
time.sleep(2)
print("IDeal")
print("Paypal")
time.sleep(2)
Betalen = input("Betaalmethode: ")
print("U word verzonden naar uw aanbieder...")