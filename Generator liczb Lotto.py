import random

def generuj_liczby_lotto():
    liczby = random.sample(range(1, 50), 6)
    liczby.sort()
    return liczby

print("Witaj w generatorze liczb Lotto!")
wylosowane = generuj_liczby_lotto()
print("Twoje szczęśliwe liczby to:", wylosowane)
