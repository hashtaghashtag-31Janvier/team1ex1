def main():

	tirage = tirageFunc()
	print('Tirage : ' + tirage)

	solution = []
	nbSolution = 0
	nbLettres = 9
	aucunMotTrouve = True
	chaine = tirage
	dick = open("Dictionnaire.txt", "r")


	while nbLettres > 0 && aucunMotTrouve:
		while 

	for ligne in dick:
    	if chaine in ligne:
        	aucunMotTrouve = False
         	solution[nbSolution]
        	nbSolution = nbSolution +1
        	solution[]
	
	dick.close()



def tirageFunc():

	tirage = []
	import string
	import random
	for x in range(1,9):
		tirage[x] = random.choice(string.letters)
	return tirage