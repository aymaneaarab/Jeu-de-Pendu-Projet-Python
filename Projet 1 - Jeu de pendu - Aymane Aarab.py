print("""--------------Jeu de Pendu-------------
vous devez deviner un mot d'un fruit en devinant les lettres une par une:
  """)
import random
with open("Liste des mots.txt","r") as fichier:
    lignes = fichier.read().splitlines()
    mot_choisi = random.choice(lignes)
    mot_masque = ["_"]* len(mot_choisi)
essai=1
while essai<=10:
    print(*mot_masque)
    lettre=input("entrez une lettre : ")
    trouve = False
    for j in range(len(mot_choisi)):
        if lettre == mot_choisi[j]:
            mot_masque[j]=lettre
            trouve = True
    if trouve==True:
        print(*mot_masque)
        print("bravo, il vous reste",10-essai,"essais")
    else:
        print("faux, il vous reste",10-essai,"essais")
    essai+=1
    if "_" not in mot_masque:
        print(" bravo vous avez trouvé le mot deviné", mot_choisi)
        choix=input("voulez vous rejouer , (Oui ,Non) ")
        if choix=="oui" or choix=="Oui":
            mot_choisi = random.choice(lignes)
            mot_masque = ["_"]* len(mot_choisi)
            essai=1
        else:
            print("au revoir ")
            break
            
    elif essai>10:
        print(" Vous avez terminé votre nombre d'essais sans connaître le mot ",mot_choisi)
        choix=input("voulez vous rejouer , (Oui ,Non) ")
        if choix=="oui" or choix=="Oui":
            mot_choisi = random.choice(lignes)
            mot_masque = ["_"]* len(mot_choisi)
            essai=1
        else:
            print("au revoir ")
            break

    
