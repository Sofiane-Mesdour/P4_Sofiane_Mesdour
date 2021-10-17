from tinydb import TinyDB

db = TinyDB('dbPlayer.json')
players_table = db.table


class Player:

    def __init__(self, name, prenom, age, genre, rang):
        self.name = name
        self.prenom = prenom
        self.age = age
        self.genre = genre
        self.rang = rang

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def from_input(cls):
        print("------------------------------\n"
              "------------------------------\n"
              "        Création Joueur :     \n"
              "------------------------------\n"
              "------------------------------\n"
              )

        return cls(
            input('Name: '),
            input('Prénom: '),
            int(input('age : ')),
            str(input('genre : ')),
            int(input('rang : ')),
        )

    def serialize(self):
        return {
            'name': self.name,
            'prenom': self.prenom,
            'age': self.age,
            'gender': self.genre,
            'rang': self.rang,
        }
