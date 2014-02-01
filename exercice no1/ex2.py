import string
import random

def main():

    #tirage = tirageFunc()
    tirage = ['a', 'b', 'c']
    print tirage

    solution = []
    nbSolution = 0
    nbLettres = 9
    aucunMotTrouve = True
    dick = open("Dictionnaire2.txt", "r")

    chaine = ''.join(tirage)

    while (aucunMotTrouve):

        for ligne in dick:
            print chaine
            if chaine in ligne:
                print "test2"
                aucunMotTrouve = False
                print "trouve"
                #solution[nbSolution] = ligne
                nbSolution = nbSolution +1
                    #solution[]
        if (len(chaine)> 1):
            chaine = chaine[:-1]
            print chaine

	#dick.close()



def tirageFunc():

	tirage = [None] * 9
	for x in range(0,9):
		tirage[x] = random.choice(string.letters)
	return tirage

main()