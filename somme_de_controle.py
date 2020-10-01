#!/usr/bin/env python3




def limite_checksum(valeur):
        #verifie si la valeur est plus de 65535
        if (valeur > 65535):
                return 65535 % 255
        return valeur


def somme_fletcher(texte):
	checksum1 = []
	checksum2 = []
	somme = 0
	#faire le tableau checksum1 
	for i in texte:
		#ord() retourne la valeur acsii
		valeur = ord(i)
		somme += valeur
		checksum1.append(limite_checksum(somme))

	#faire le tableau checksum2
	counter = 0
	somme = 0
	for i in texte:
		somme += checksum1[counter]
		checksum2.append(limite_checksum(somme))
		counter += 1
	#retourner un dictionnaire des deux checksums
	return {'checksum1':checksum1,'checksum2':checksum2}



