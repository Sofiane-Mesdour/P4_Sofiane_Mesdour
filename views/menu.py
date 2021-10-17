from os import system, name
from Controller import debut


class MainDisplay:
    """Display the main title"""

    def display_title(self):
        """Display the title of the application"""
        print("------------------------------------------------\n"
              "---------------Gestion de tournoi---------------\n"
              "------------------------------------------------\n"
              "------------------------------------------------\n"
              "-----------------Menu principal-----------------\n"
              "------------------------------------------------\n"
              " Entrez le numéro correspondant au menu choisi :\n"
              "------------------------------------------------\n"
              )


class ClearScreen:
    """Clear the terminal"""

    def __call__(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


class DisplayPlayersReport:

    def __call__(self):
        print("------------------------------------------------\n"
              "-------------Affichages des rapports des joueurs-------------\n"
              "------------------------------------------------\n"
              " Afficher les rapports :\n"
              "1 - Par ordre alphabétique des joueurs\n"
              "2 - Par ordre de classement des joueurs\n"
              "3 - Pour revenir au menu principal\n"
              )

    def display_alphabetical(self, players_list):
        for player in players_list:
            print(f"{player.name} - {player.age} - {player.genre} - Classement : {player.rang}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()

    def display_ranking(self, players_list):
        for player in players_list:
            print(f"Classement :{player.rang} - {player.name} - {player.age} - {player.genre}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()


class DisplayTournoiReport:

    def __call__(self):
        print("------------------------------------------------\n"
              "-------------Affichages des Tournois------------\n"
              "------------------------------------------------\n"
              "1 - Afficher la liste de tous les Tournois déjà joué :\n"
              "2 - Afficher la liste des tournois avec les matchs:\n"
              "3 - Pour revenir au menu principal\n"

              )

    tournoi_list = debut.Debut.save_tournoi

    def display_tournoi(self, tournoi_list):
        for tournois in tournoi_list:
            print("Le Nom du Tournoi : "f"{tournois.get('Le Nom du Tournoi')}\n"
                  "Le lieu du tournoi' : "f"{tournois.get('Le lieu du tournoi')}\n"
                  "Date du tounoi : "f"{tournois.get('Date du tounoi')}\n"
                  "Nombre de tours : "f"{tournois.get('Nombre de tours')}\n"
                  "Contrôle du temps : "f"{tournois.get('Contrôle du temps')}\n"
                  "Les rounds : "f"{[r.get('name') for r in tournois.get('rounds')]}\n"
                  "Les joueurs : "f"{[p.get('name') for p in tournois.get('players')]}\n"
                  )
            input()

    def display_round(self, tournoi_list):
        for tournois in tournoi_list:
            print("Le Nom du Tournoi : "f"{tournois.get('Le Nom du Tournoi')}")
            for round in tournois.get("rounds"):
                print(f"nom: {round.get('name')}")
                if round.get("matchs"):
                    for i, match in enumerate(round.get("matchs")):
                        print(f"match {i} : {match[0][0].get('name')} - {match[1][0].get('name')}")
                else:
                    print("no match found")
            input()
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()
