"""
Programming opdracht Prog : NS functies
(c) 2024 Hogeschool Utrecht,
Tufan Atalay (tufan.atalay@student.hu.nl)
"""

naam = input('Wat is je naam? : ')
leeftijd = int (input('Wat is je leeftijd? :'))
dag = input("Welke dag reis je: ").lower()
afstand = int(input('Hoeveel km ga je reizen? :'))
weekend = ['Zaterdag' , 'Zondag']
weekendrit = dag in weekend

def standaardprijs(afstandKm):
    if afstandKm < 0:
        afstandKm = 0
        # Als een negatieve afstandswaarde wordt ingevoerd, wordt deze als 0 geteld

    if afstandKm > 50:
        prijs = 15 + (afstandKm - 50) * 0.60
    #15 euro voor de eerste 50 km, en 60 cent extra voor de elke km.
    else:
        prijs = afstandKm * 0.80
    # 0.80 cent per km tot 50km afstand.


    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    # Deze functie berekent de standaardprijs voor een rit op basis van de afgelegde afstand in kilometers.

    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            korting = prijs * 0.65
            # Dan 35% korting berekenen(voor jonger dan 12 of 65+)
        else:
            korting = prijs * 0.60
            # 40% korting (voor andere leeftijdsgroepen)
    else:
        # Als het geen weekend is:
        if leeftijd < 12 or leeftijd >= 65:
            korting = prijs * 0.70
            # 30% korting (voor jonger dan 12 of 65+).
        else:
            korting = prijs
            # Geen korting voor andere leeftijdsgroepen.

    return korting
leeftijd = 30
weekendrit = True
afstand = 60

print('De rit gaat €', ritprijs(leeftijd, weekendrit, afstand), 'kosten')   # De uiteindelijke ritprijs wordt afgedrukt.





