from chiffrement import *
from fonctions import *
from p1 import *
import hashlib

def lire_fich(fichier : str):

    block = 1024
    
    with open(fichier,"r",encoding="utf-8") as f:
        alloc = f.read(block)
        while alloc:
            yield alloc.encode("utf-8")
            alloc = f.read(block)
            
def hash_fichier(fichier):

    le_hash = hashlib.sha256()
    for morceau in lire_fich("test.txt"):
        le_hash.update(morceau)
    le_digest = le_hash.digest() # l'on a 256 c'est bien trop grand, l'on tronc donc aux 32 bits les plus significatfs
    return int.from_bytes(le_digest[:4],byteorder="big")

def signer_fich(empreinte : int, clef_prive : int):
    
    d, n = clef_prive

    signature = expo_modulaire(empreinte,d,n)


    return signature


def verif_signature(signature: int,hash_fichier,clef_publique):

    e,n = clef_publique
    calcul = expo_modulaire(signature,e,n)
    if calcul == hash_fichier:
        return True
    else:
        return False

clef_pub,clef_priv = genere_clefs(64)
print(clef_pub)
print(clef_priv)

premier_hash = hash_fichier("test.txt")
print(f"Voici le premier hash {premier_hash}")

signature = signer_fich(premier_hash,clef_priv)
print(f"Voici la signature {signature}")

if verif_signature(signature,premier_hash,clef_pub) == True:
    print("Signature correcte")
else:
    print("Signature incorrecte")
