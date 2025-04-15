import random
import math
def pgcd(a : int,b : int) -> int:

	while a%b != 0:
		temp = b
		b = a%b
		a = temp		
	return b


def expo_modulaire(base : int , expo: int, mod : int) -> int:
	
	res = 1
	while expo != 0:
		if expo%2 != 0:
			res = (base*res)%mod
		base = (base*base)%mod
		expo = expo>>1
	return res

def bezout(a : int,b : int):
	#calcul des coefs de bezout tq: pgcd(a,b) == 1 alors il existe (u,v) dans Z² tq: au+bv = 1
	u = 1
	v = 0
	u1 = 0
	v1 = 1
	
	while b != 0:
		#j'ai besoin de sauvegarder le quotient pour la mise à jour des coefs de bézout

		q = a//b
		#je fais l'algorithme d'euclide normalement
		temp = b
		b = a%b
		a = temp
		
		
		#ici c'est la partie mise à jour des coefs de bezout
		tempu0 = u
		tempv0 = v

		u = u1
		v = v1

		u1 = (tempu0-(u1*q))
		v1 = (tempv0+(v1*q))

		

	return (u,v)


def inverse_mod(a : int, b : int)->int:

	i,_ = bezout(a,b)
		
	return (i%b + b)%b



def test_primalite(x : int):
	print("\n")
	#calculons d
	print("Nombre à tester:",x,end="\n")
	if x == 2 or x == 3:
		return True	
	if x % 2 == 0 or x < 2:
		return False


	reste = x -1
	cpt = 0
	
	while reste % 2 == 0:

		reste //= 2
		cpt += 1
		print("c'est le quotient:","sep=\t",reste) #message de débogage

	
	d = (x-1)//(2**cpt)

	print("voici d:",d,end="\n")	
	
	for _ in range(10):
		a = random.randint(2,x-1) 
		
		if expo_modulaire(a,d,x) == 1:
			continue
		
		fl = False
		for r in range(cpt):
				if expo_modulaire(a, (2**r) * d, x) == x - 1:
					fl = True
					break
		if not fl:
			return False
			
	
	return True
	            

def genere_clefs(k : int) -> int:

	#je génère un p et un q
	#je teste la primalité des deux
	#je génère un module RSA avec les deux
	#je fais phi(n) = (p-1)(q-1)
	nb = []

	while len(nb) < 2:
		ra = random.getrandbits(k//2) | (1<<( (k//2) - 1)) | 1
		if test_primalite(ra) and (len(nb) == 0 or ra != nb[0]):
			nb.append(ra)
			
	print("\n P et Q pour le module RSA",end="\n")	
	for j in range(len(nb)):
		print(nb[j])
	
	p = nb[0]
	q = nb[1]

	n = p*q # calcul du module RSA tq: n = pxq
	print(f"Module RSA:{n}\n")
	phi = (p-1)*(q-1) # calcul de Phi(n) tq: (p-1)(q-1)
	print(f"PHI DE N:{phi}\n")
	
	#on génère un 1<e<phi(n) tq: pgcd(e,phi(n)) = 1
	e = random.randint(2, phi - 1 )
	while pgcd(e,phi) != 1:
		e = random.randint(2, phi - 1 )
	print(f"e:{e} car pgcd({e},{phi}) = {pgcd(e,phi)}\n")
	

	#on calcul notre clef privé d

	d,_ = bezout(e,phi)
	d = d % phi
	if d < 1: 
		d += phi  # si d négatif alors application du mod pour le repasser en positive; ex d = -33 et phi = 220 alors d = 220 + (-33) = 87
		
	#maintenant j'ai généré un nb grand avec MSB = 1 et impair LSB = 1
	print(f"\n l'inverse modulaire de {e} mod {n} = {d}\n")

	return (e,n),(d,n),p,q



def factorisation_n(n : int)->int:

	#premièrement calculons combien de nombres premiers existent jusqu'à n
	
	print(f"\n il existe {int(n/math.log(n))} nombres premiers jusqu'à {n} \n")

	print("Puis nous devons utiliser le cribble d'erathosthène en générant tous les premiers jusqu'à racine carré de n\n")
	print(f"\n racine carré de n {math.sqrt(n)}\n")

	#cribble d'erathosthène
	taille = int(math.sqrt(n))

	li = [True] * (taille+1)
	ni = n
	for i in (0,1):
		li[i] = False

	print(f"taille {n} racine: {taille} ")
	for i in range(2,taille):
		if li[i] == True:
			for j in range(i*i,taille + 1,i):
				li[j] = False
		
	premiers = []
	#insertion des nombres premiers jusqu'à racine carré de n
	for i in range(2,taille+1):
		if li[i] == True:
			premiers.append(i)

	#factorisation
	for k in range(len(premiers)):
		if n%premiers[k] == 0:
			p = premiers[k]
			break 
	else:
		return None


	q = int(n/p)
	print(f"\n P trouvé {p} \n Q = {q}\n")


	return p,q

