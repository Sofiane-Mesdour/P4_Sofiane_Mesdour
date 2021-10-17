import pandas as pd
from models import Player_Models
from tinydb import TinyDB

db = TinyDB('dbPlayer.json')
players_table = db.table('players')


class Seria:

    def organisation():
        player = Player_Models.Player.from_input()
        serialized_player = {'name': player.name,
                             'prenom': player.prenom,
                             'age': player.age,
                             'genre': player.genre,
                             'Classement': player.rang
                             }
        players_table.insert(serialized_player)
        return player

    def serialized(self):
        player_infos = {'Nom': Player_Models.Player.name,
                        'Prénom': Player_Models.Player.prenom,
                        'Age': Player_Models.Player.age,
                        'genre': Player_Models.Player.genre,
                        'Classement': Player_Models.Player.rang
                        }
        return player_infos

    def unserialized(self, serialized_player):
        name = serialized_player["name"]
        prenom = serialized_player["prenom"]
        age = serialized_player["age"]
        genre = serialized_player["genre"]
        rang = int(serialized_player["Classement"])
        return Player_Models.Player(name, prenom, age, genre, rang)

    def update_ranking():
        player_id = 0
        players_data = pd.read_json("dbPlayer.json")
        players_data = pd.concat([players_data.drop("players", axis=1),
                                  players_data["players"].apply(pd.Series)], axis=1)
        print(players_data)
        print()
        ansewer = input("Voulez vous actualiser des mise a jour de classements : ")

        while ansewer == "oui":

            valid_id = False
            while not valid_id:
                player_id = input("Entrer le numéro du joueur : ")
                if player_id.isdigit() and 1 <= int(player_id) <= len(players_table):
                    valid_id = True
                else:
                    print("Vous devez entrer le numéro correspondant au joueur")

            valid_ranking = False

            while not valid_ranking:

                new_ranking = input("Entrez le nouveau classement : ")

                if new_ranking.isdigit() and int(new_ranking) >= 0:
                    valid_ranking = True
                    players_table.update(fields={"Classement": new_ranking}, doc_ids=[int(player_id)])
                else:
                    print("Vous devez entrer un nombre entier positif")

            ansewer = input("Voulez vous continuez les actualisations : ")

        print("mise a jour du classement effectué avec succès")

    def home_menu_controller(self):
        pass
