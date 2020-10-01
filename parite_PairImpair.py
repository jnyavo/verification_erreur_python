#!/usr/bin/env python3

#fonction Counter() pour compter les élements dans un string ou array
from collections import Counter


def bitParite_pair( b_array):
	#b_array doit être un bytearray
	#fonction qui retourne un bytearray avec le bit de parité pair

	res = bytearray()

	for i in range(len(b_array)):
		#convertir l'element en binaire
		octet = bin(b_array[i])[2:]


		if (Counter(octet)['1'] % 2 == 0):
			#le nombre de 1 est pair
			res.append(int('0' + octet,2))
		else:
			#le nombre de 1 est impair
			res.append(int('1' + octet,2))
	return res



def bitParite_impair(b_array):
	#b_array doit être un bytearray
	#fonction qui retourne un bytearray avec le bit de parité impair
	res = bytearray()
	for i in range(len(b_array)):

                #convertir l'element en binaire
                octet = bin(b_array[i])[2:]


                if (Counter(octet)['1'] % 2 == 0):
                        #le nombre de 1 est pair
                        res.append(int('1' + octet,2))
                else:
                        #le nombre de 1 est impair
                        res.append(int('0' + octet,2))

	return res


