import random
from fonctions import *
import math
#from chiffrement import *

#utilisation d'un dictionnaire pour faciliter la recherche O(1)
Sigma : str ="ABCDEFGHIJKLMNOPQRSTUVWXYZ_.?€0123456789" 


alphabet = {}
alpha_verlan = {}

for i in range(len(Sigma)):
    char = Sigma[i]
    alphabet[char] = i
    alpha_verlan[i] = char

#alpha_verlan pour la recherche inversé


print(pgcd(3,5),sep="\n",end="\n")
print(expo_modulaire(88,173,323))
#test de nombres premiers jusqu'à 31
#
#for i in range(2,31): print(test_primalite(i))	

print()
genere_clefs(16)
print(factorisation_n(323))
print()
print()
print(expo_modulaire(88,173,323))
print("faisons l'inverse maintenant")
print("\n calcul de d")
d,_ = bezout(173,288)

if (d*173)%288 == 1:
    print("INverse correcte")
else:
    print("Inverse incorrecte")
print(f"voici e: {d}")
print("On chiffre avec e = 15\n")
print(expo_modulaire(46,2,323))



#calcul de bloc
n = 2047
t_a = len(alphabet)
print(f"taille de l'alphabet {t_a}\n")
print("\n taille du bloc k")
k =  math.floor(math.log(n)/math.log(t_a))
print(f"\n taille du bloc {k} \n")



