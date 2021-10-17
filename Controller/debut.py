from tinydb import TinyDB
from models import Serialized, tournoi

dbs = TinyDB('dbTournoi.json')
tournoi_table = dbs.table('Tournoi')


# tournoi_table.truncate()


class Debut:

    def save_tournoi(tournois):
        serialized_tournois = {'Le Nom du Tournoi': tournois.name,
                               'Le lieu du tournoi': tournois.place,
                               'Date du tounoi': tournois.date,
                               'Nombre de tours': tournois.number_of_tours,
                               'Contrôle du temps': tournois.type,
                               'rounds': [r.serialize()for r in tournois.rounds],
                               'players': [j.serialize() for j in tournois.players]
                               }

        tournoi_table.insert(serialized_tournois)
        return print('sauvegarde réussie')

    def lancement():
        tournois = tournoi.Tournoi.from_input()
        print('Vos données sur le tournoi vont etre sauvegarder')

        print("------------------------------------------------\n"
              "------------------------------------------------\n"
              "---------Etape de création des joueurs----------\n"
              "------------------------------------------------\n"
              "------------------------------------------------\n"
              )

        donnee = int(input("Combien de joueur avez vous a introduire pour ce tournois :  "))
        for i in range(donnee):
            player = Serialized.Seria.organisation()
            tournois.add_player(player)
        print(tournois)
        print(tournois.players)

        print("------------------------------------------------\n"
              "------------------------------------------------\n"
              "-Lancement du Tournois : ", tournois.name, "\n"
              "------------------------------------------------\n"
              "------------------------------------------------\n"
              )

        tournois.generate_first_round()
        for match in tournois.rounds[-1].matchs:
            print(match)
            print("Es que le match s'est achevé sur un match nul : ")
            resultat = str(input("Répondez par oui ou non : "))

            if resultat == 'oui':
                match[0][1] = 1 / 2
                match[1][1] = 1 / 2
            else:
                resultat = int(input(" Qui des deux joueurs a remporté le match/n"
                                     " Répondez par 1 ou 2 :  "))
                if resultat == 1:
                    match[0][1] += 1
                else:
                    match[1][1] += 1
            print("------------------------------------------------\n"
                  "------------------------------------------------\n"
                  "---Le resultat du 1er Round est comme suit : ---\n"
                  "------------", tournois.rounds[0].matchs, "------------\n"
                  "------------------------------------------------\n"
                  )

        while len(tournois.rounds) < tournois.number_of_tours:
            tournois.generate_other_round()  # effet : alimenter tournoi.rounds avec un nouveau round
            for match in tournois.rounds[-1].matchs:
                print(match)
                print("Es que le match s'est achevé sur un match nul : ")
                resultat = str(input("Répmondez par oui ou non : "))

                if resultat == 'oui':
                    match[0][1] = 1 / 2
                    match[1][1] = 1 / 2
                else:
                    resultat = int(input(" Qui des deux joueurs a remporté le match\n Répondez par 1 ou 2 :  "))
                    if resultat == 1:
                        match[0][1] += 1
                    else:
                        match[1][1] += 1
            print("----------------------------------------------------------------\n"
                  "le resultat du ", len(tournois.rounds), " Round est comme suit :\n"
                                                           "------", tournois.rounds[0].matchs,
                  "---------------------------\n"
                  "----------------------------------------------------------------\n"
                  )
        print("--------------------------------------------------\n"
              "--------------------------------------------------\n"
              "----Le tournoi ", tournois.name, " est terminé----\n"
                                                "--------------------------------------------------\n"
                                                "--------------------------------------------------\n"
              )
        Debut.save_tournoi(tournois)
        print("Appuyiez sur une touche pour revenir au menu")
        input()
        return tournois
