__authors__ = "Mohamed Ben Halima"
__date__ = "04/01/2020"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from plateau import Plateau
from joueur import Joueur

class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouer avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """
        print("Bienvenue au jeu Tic Tac Toe.")
        print("---------------Menu---------------")
        print("1- Jouer avec l'ordinateur.")
        print("2- Jouer avec une autre personne.")
        print("0- Quitter.")
        print("-----------------------------------")
        
        valeur=self.saisir_nombre(0,2)  
        # print(valeur)
        if valeur==0:
            print(end=' ')
        elif(valeur==1):
            nom=input("Entrez s.v.p votre Nom:?")
            pion=self.demander_forme_pion()
            self.joueurs.append(Joueur(nom,'Personne',pion))
            if pion=='O':
                self.joueurs.append(Joueur('Colosse','Ordinateur','X'))
            else:
                self.joueurs.append(Joueur('Colosse','Ordinateur','O'))
        elif(valeur==2):
            nom=input("Entrez s.v.p votre Nom:? ")
            pion=self.demander_forme_pion()
            self.joueurs.append(Joueur(nom,'Personne',pion))
            nom2=input("Entrez s.v.p le Nom de l'autre Joueur:? ")
            if pion=='O':
                self.joueurs.append(Joueur(nom2,'Personne','X'))
            else:
                self.joueurs.append(Joueur(nom2,'Personne','O'))
        recommencer='O'
        while(recommencer=='O' and valeur!=0):
            while(self.plateau.non_plein()==True and self.plateau.est_gagnant('O')==False and self.plateau.est_gagnant('X')==False):
                self.joueur_courant=self.joueurs[0]
                self.tour(valeur)
                if self.plateau.non_plein()==True and self.plateau.est_gagnant(self.joueurs[0].pion)==False :
                    self.joueur_courant=self.joueurs[1]
                    self.tour(valeur)
            print(self.plateau)
            if self.plateau.non_plein()==False:
                self.nb_parties_nulles+=1
                print("Partie Terminée! Aucun joueur n'a gagné!!")
            elif self.plateau.est_gagnant(self.joueurs[0].pion)==True:
                self.joueurs[0].nb_parties_gagnees+=1
                print("Partie Terminée! le joueur gagnant est:",self.joueurs[0].nom)
            elif self.plateau.est_gagnant(self.joueurs[1].pion)==True:
                self.joueurs[1].nb_parties_gagnees+=1
                print("Partie Terminée! le joueur gagnant est:",self.joueurs[1].nom)
            print("Partie gagnée par",self.joueurs[1].nom,":",self.joueurs[1].nb_parties_gagnees)
            print("Partie gagnée par",self.joueurs[0].nom,":",self.joueurs[0].nb_parties_gagnees)
            print("Parties nulles",self.nb_parties_nulles)
            recommencer=input("Voulez-vous recommencer (O,N)")
            while(recommencer != 'O' and recommencer != 'N'):
                recommencer=input("Tapez O si Voulez-vous recommencer, Sinon Tapez N: ")
            if(recommencer=='O'):
                self.plateau.initialiser()
        print("***merci et au revoir!*** ")   

    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."
        x=input("Entrez s.v.p un nombre entre 0 et 2:? ")
        while(x.isnumeric()==False or int(x)<0 or int(x)>2  ):
           print("***valeur incorrecte!*** ")
           x=input("Entrez s.v.p un nombre entre 0 et 2:? ")
        return(int(x))

        #pass

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        forme=input("Sélectionner s.v.p la forme de votre pion (X,O):?")
        while(forme!='X' and forme!='O'):
            forme=input("Sélectionner s.v.p la forme de votre pion (X,O):?")
        return(forme)
        # pass

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."
        print(self.plateau)
        if choix==1:
            if self.joueur_courant.type=="Personne":
                pos=self.demander_postion()
                self.plateau.selectionner_case(pos[0],pos[1],self.joueurs[0].pion)
                #print(self.plateau)
            elif self.joueur_courant.type=="Ordinateur":
                print("C'est le Tour maintenant de l'ordinateur Colosse!")
                prochaine=self.plateau.choisir_prochaine_case(self.joueurs[1].pion)
                self.plateau.selectionner_case(prochaine[0],prochaine[1],self.joueurs[1].pion)
                #print(self.plateau)
        else:
            pos=self.demander_postion()
            self.plateau.selectionner_case(pos[0],pos[1],self.joueur_courant.pion)

            

        #pass

    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        
        print(self.joueur_courant.nom,": Entrez s.v.p. les coordonnées de la case à utiliser:")
        print("Numéro de la ligne:",end=' ')
        i=self.saisir_nombre(0,2)
        print("Numéro de la Colonne:",end=' ')
        j=self.saisir_nombre(0,2)
        while(self.plateau.position_valide(i,j)==False):
            print(self.joueur_courant.nom,":cette position est occuper Entrez s.v.p. d'autre coordonnées:")
            print("Numéro de la ligne:",end=' ')
            i=self.saisir_nombre(0,2)
            print("Numéro de la Colonne:",end=' ')
            j=self.saisir_nombre(0,2)   
        l=[i,j]
        return(l) 
        #pass
   
    

if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()
    

