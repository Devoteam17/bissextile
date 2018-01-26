#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

# commentaire : pour le rendre executable : chmod +x ton_script.py
# Pour le lancer : python3 ton_script.py

annee = input("Saisir une année : ")
annee = int(annee)

if annee % 4 != 0 :
	print(annee, " n'est pas une année bissextile")
elif annee % 100 == 0:
	if annee % 400 == 0:
		print(annee, " est une année bissextile")
	else:
		print(annee, " n'est pas une année bissextile")
else:
	print(annee, " est une année bissextile")
        
input ("fin du programme <Taper sur entrée>")


