#!/usr/bin/env python3




def limite_checksum(valeur):
        #verifie si la valeur est plus de 65535
        if (valeur > 65535):
                return valeur % 65535
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


def afficher_tableau(res):
	liste = ['checksum1','checksum2']
	for nom in liste:
		print("| ",nom," |")
		for i in res[nom]:
			print(i,"\n")
def main():
	import sys
	if len(sys.argv) != 2:
		print("Inserez un texte en argument")
		return -1
	tableau = somme_fletcher(sys.argv[1])
	afficher_tableau(tableau)


if __name__ == "__main__":
	main()
