from fonctions import *
import random
from p1 import *

# fonction de chiffrement pour un message décimal code ASCII avec clé publique

def chiffrement_v1(message : int ,clef_publique: int,module_rsa : int)->int:

    c = expo_modulaire(message,clef_publique,module_rsa)

    #c = m^e mod n -> chiffrement c  = Kp(m) mod n = m^e mod n

    return c


def dechiffrement_v1(msg_ch : int,clef_prive,module_rsa:int)->int:

    m = expo_modulaire(msg_ch,clef_prive,module_rsa)

    return m


def dechiffrement_reste_chinois(c : int, d : int, p : int, q : int)->int:

    print("Réduction des puissances si d > 100")
    M = p*q
    
    #p_r et q_r sont nos p et q réduits mod (p-1) et (q-1) respectivement
    p_r = d % (p-1)
    q_r = d % (q-1)
    c1 = c %  M
        
    mp = expo_modulaire(c1,p_r,p)
    mq = expo_modulaire(c1,q_r,q)

    print(f"\n mp = {mp}, mq = {mq} \n")

    inverse_q = inverse_mod(q,p)
    inverse_p = inverse_mod(p,q)
        
    sol_p = (mp*q*inverse_q)%M
    sol_q = (mq*p*inverse_p)%M
    solution = (sol_p + sol_q) % M
    print(f"\nSolution {solution}\n")
    

    return solution

'''
c. Utilisez le codage approprié pour transformer le texte en chiffres.
d. Chiffrer le message obtenu par la clé publique.
e. Transformer le message obtenu en texte alphabet (fait attention à la taille du
bloc pour le message chiffré).

'''

def convert_msg_to_int(msg: str,taille_alphabet : int,taille_bloc:int,alphabet : dict):

    text_to_chiffre = []
    N = taille_alphabet
    for i in range(0,len(msg),taille_bloc):
        block = msg[i:i+taille_bloc]
        entier = 0

        for k in range(len(block)):
            print(f"{block[k]},{alphabet[(block[k])]}")
            entier += alphabet[(block[k])]* (N**(taille_bloc-k-1))

        text_to_chiffre.append(entier)    
    

    return text_to_chiffre


def chiffre_text(msg,clef_publique:int,module_rsa : int):

    message_chiffre = []
    for i in range(len(msg)):
       cf = chiffrement_v1(msg[i],clef_publique,module_rsa)
       message_chiffre.append(cf)

    return message_chiffre

def convert_int_msg(msg: int,taille_alphabet: int,taille_bloc:int ,v_salphabet:dict):
    chiffre_to_msg = []  # Liste pour stocker les blocs convertis

    for block in msg:  # Chaque entier représente un bloc de `taille_bloc` caractères
        conversion = ""

        for k in range(taille_bloc, -1, -1):  
            valeur = block // (taille_alphabet ** k)  
            block = block % (taille_alphabet ** k)  
            conversion += v_salphabet[valeur]  
        chiffre_to_msg.append(conversion)  
    
    return "".join(chiffre_to_msg) 


#Le message : [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523,
# 9862, 356, 5356, 1159, 10280, 12523, 7506, 6311] a été crypté avec la clé
# publique (e= 12413 ; n=13289).
# Rappel : Il faut faire la factorisation pour trouver q et p et calculer l’inverse de e
# modulo phi(n).
p,q = factorisation_n(13289)
phi = (p-1)*(q-1)
e = 12413
d,_ = bezout(e,phi)
if (d*e)%phi == 1:
    print("inverse correcte\n")
else:
    print("inverse incorrecte\n")
exo = [9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523,9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]


'''
print()
dech = []
for i in range(len(exo)):
    print(f"Déchiffrement de {exo[i]}\n")
    dec = dechiffrement_reste_chinois(exo[i],d,p,q)
    dech.append(dec)
    print(f"Résultat déchiffrement {dec}")
print("\nrechiffremment")
chif = []
for k in range(len(exo)):
    chiffrement_v1(exo[k],e,p*q)
    chif.append(exo[k])
print(dech)
print()
print(exo)
print()
print(chif)
'''

'''
print("\n nouveau test \n")
print("Déchiffrement de 9197\n")
print(dechiffrement_reste_chinois(9197,d,p,q))
print("\n voici")
print("Et si l'on chiffrait ? \n")
m = p*q
print(chiffrement_v1(5424,12413,m))
'''

''''
c. Attention, celui-ci est ardu. Clé publique: (e=163119273;n=755918011); message
crypté : [671828605, 407505023, 288441355, 679172842, 180261802]
'''

n=755918011
p,q = factorisation_n(n)
e=163119273
phi = (p-1)*(q-1)
d,_ = bezout(e,phi)
if (d*e)%phi == 1:
    print("Inverse modulaire correcte")
else:
    print("Inverse modulaire incorrecte")

exo2 = [671828605, 407505023, 288441355, 679172842, 180261802]


dech = []
for i in range(len(exo2)):
    print(f"Déchiffrement de {exo2[i]}\n")
    dec = dechiffrement_reste_chinois(exo2[i],d,p,q)
    dech.append(dec)
    print(f"Résultat déchiffrement {dec}")
print("\nrechiffremment")
chif = []
for k in range(len(exo2)):
    chiffrement_v1(exo2[k],e,p*q)
    chif.append(exo2[k])
print(dech)
print()
print(exo2)
print()
print(chif)


chif_f = convert_msg_to_int("ENVOYEZ_2500€A",40,2,alphabet)
print(chif_f)
finallement = chiffre_text(chif_f,179,2047)
correcte = convert_int_msg(finallement,40,2,alpha_verlan)
print(f"\n{correcte}")
print()

com = convert_msg_to_int(correcte,40,3,alphabet)
print(com)

dec = []
for i in range(len(com)):
    dec.append(dechiffrement_reste_chinois(com[i],411,23,89))
    
print(f"voici le message déchiffré {dec} ")

print(type(dec))
dech = []

print(convert_int_msg(dec,40,1,alpha_verlan))


