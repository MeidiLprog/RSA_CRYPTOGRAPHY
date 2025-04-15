import math
import tkinter as tk
from tkinter import messagebox
from chiffrement import *
from fonctions import *
#from hash import *
from p1 import *

import time as CHRONO

#classe pour permettre la création d'un objet tkinteer
class progRSA:
	def __init__(self,fenetre):
		self.fenetre = fenetre
		self.fenetre.title("Programme RSA")
		self.fenetre.geometry("800x800")
		self.clef_publique = None
		self.clef_prive = None
		#Serviront après pour le déchiffrement
		self.p = None
		self.q = None

		self.lancement()

	#fonction d'initialisation de la fenetre
	def lancement(self):
		self.champ_un = tk.Label(self.fenetre,text="Taille de clef(bits), génération rapide jusqu'à 2048 bits :")
		self.champ_un.pack()
		
		self.entree_un = tk.Entry(self.fenetre)
		self.entree_un.pack()

		self.generer_clefs = tk.Button(self.fenetre,text="Générer clefs",command=self.genererClefs)
		self.generer_clefs.pack()

		self.temps = tk.Label(self.fenetre,text="")
		self.temps.pack()	

		self.clefs = tk.Label(self.fenetre,text="")
		self.clefs.pack()

		#partie chiffrement de texte

		self.chiffre_t = tk.Label(self.fenetre,text="Entrer le texte à chiffrer",width=80)
		self.chiffre_t.pack()

		self.entree_text = tk.Entry(self.fenetre)
		self.entree_text.pack()

		self.bouton_ch = tk.Button(self.fenetre,text="Chiffrer",command=self.chiffrerText)
		self.bouton_ch.pack()
	
		self.temps_chif = tk.Label(self.fenetre,text="")
		self.temps_chif.pack()

		#partie déchiffrement
		self.bouton_dech = tk.Button(self.fenetre,text="Déchiffrer le text",command=self.dechiffrerText)
		self.bouton_dech.pack()

		self.affiche_d = tk.Label(self.fenetre,text="")
		self.affiche_d.pack()

		#test rapide
		self.deuqu = tk.Label(text="")
		self.deuqu.pack()


		self.quitter = tk.Button(self.fenetre,text="Quitter",command=self.fenetre.destroy)
		self.quitter.pack()

	#fonction de génération de clefs
	def genererClefs(self):
		#je récupère ici la valeur entrée par l'utilisateur dans le entree_un avec get
		#je convertis cela en int pour etre certain de ne pas avoir de soucis
		try:
			k = int(self.entree_un.get())
		
		except:
			messagebox.showerror("erreur","Une erreur est survenue lors de la génération des clefs")
			return
		debut_chrono = CHRONO.time()
		self.clef_publique,self.clef_prive,self.p,self.q = genere_clefs(k)
		fin_chrono = CHRONO.time()

		self.temps.config(text=f"Génération:{fin_chrono-debut_chrono:.5f} secondes\n")
		self.clefs.config(text=f"génération des clefs, clef publique: {self.clef_publique[0]}, \nClef privée : {self.clef_prive[0]},\nModule RSA:{self.clef_publique[1]}\n p = {self.p}: q = {self.q}\n")
		

	
	#fonction de chiffrement d'un texte
	def chiffrerText(self):
		if not self.clef_publique:
			messagebox.showerror("erreur","Appuyez sur générer clefs, car la clef publique est manquante !")
			return
		
		#ICI je récupère ce dont j'ai besoin pour chiffrer le message
		text = self.entree_text.get().upper()

		self.text = text #pour après

		block = math.floor(math.log(self.clef_publique[1]) / math.log(len(alphabet)))
		taille_alpha = len(alphabet)
		#FIn des paramètres à récupérer
		try:
			debut_chrono = CHRONO.time()
			convert_msg = convert_msg_to_int(text,taille_alpha,block,alphabet)
			chiffre = chiffre_text(convert_msg,self.clef_publique[0],self.clef_publique[1])
			convert_chiffre = convert_int_msg(chiffre,taille_alpha,block,alpha_verlan)
			fin_chrono = CHRONO.time()	





			#partie RSA qui m'arrange
			convert_text = convert_msg_to_int("ENVOYEZ_2500€A",40,2,alphabet)
			chiffre_ttt = chiffre_text(convert_text,179,2047)
			conversion_chiff = convert_int_msg(chiffre_ttt,40,2,alpha_verlan)
			self.deuqu.config(text=f"text: ENVOYEZ_2500€A, \nint: {convert_text}, \nchiffre:{chiffre_ttt},\nfin={conversion_chiff}\n")



			#récupère ces éléments dans la fonction de déchiffrement
			self.fini_conversation = convert_chiffre
			self.taille_b = block
			#fin de récupèration des paramètres

			self.chiffre_t.config(text=f"conversion message en chiffre: \n{convert_msg}\nTexte chiffré ! {chiffre}\n conversion chiffre en message: \n{convert_chiffre}\n  Temps{fin_chrono - debut_chrono:.5f}\n")
		except:
			messagebox.showerror("erreur","Une erreur est survenue lors du chiffrement, merci de recommencer !")
	

	def dechiffrerText(self):
		
		taille_alpha = len(alphabet)

		debut_c = CHRONO.time()
		converse_chiffre = convert_msg_to_int(self.fini_conversation,taille_alpha,self.taille_b+1,alphabet)
		dechi = [dechiffrement_reste_chinois(c,self.clef_prive[0],self.p,self.q) for c in converse_chiffre]
		deconv = convert_int_msg(dechi,len(alphabet),self.taille_b-1,alpha_verlan)
		fin_c = CHRONO.time()
		self.affiche_d.config(text=f"Texte déchiffré {deconv[:len(self.text)].lower()}\n")





if __name__ == "__main__":
	fenetre = tk.Tk()
	prog = progRSA(fenetre)
	fenetre.mainloop()
