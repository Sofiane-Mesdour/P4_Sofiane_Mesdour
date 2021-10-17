from models.Round import Rounds


class Tournoi:
    def __init__(self, name, place,
                 date, number_of_tours,
                 type, rounds=None
                 ):
        if rounds is None:
            rounds = []
        self.name = name
        self.place = place
        self.date = date
        self.number_of_tours = number_of_tours
        self.type = type
        self.players = []
        self.rounds = rounds

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def from_input(cls):
        print("-------------------------------------")
        print("Création Tournoi :")
        return cls(
            input('Le Nom du Tournoi: '),
            str(input('Le lieu du tournoi : ')),
            str(input('Date du tounoi : ')),
            int(int(input('Nombre de tours : '))),
            str(input('Contrôle du temps : '
                      'Bullet, '
                      'Blitz,'
                      'Coup rapide  :'
                      )),
        )

    def add_player(self, player):
        self.players.append(player)

    def sort_by_rang(self):
        return sorted(self.players, key=lambda x: getattr(x, 'rang'), reverse=True)

    def sort_by_name(self):
        return sorted(self.players, key=lambda x: getattr(x, 'name'))

    def get_round_number(self):
        return len(self.rounds) + 1

    def generate_first_round(self):
        sorted_players = self.sort_by_rang()
        # créer la liste des matchs
        nb_players = len(sorted_players)
        high_point = sorted_players[:int(nb_players / 2)]
        inferior_point = sorted_players[int(nb_players / 2):]
        # Round avec la liste des matchs

        list_matchs = []

        for p1, p2 in zip(high_point, inferior_point):
            match = ([p1, 0], [p2, 0])
            list_matchs.append(match)
        round = Rounds("Round " + str(self.get_round_number()), list_matchs)
        self.rounds.append(round)

    # def generate_round(self):
    #     last_round

    def sort_by_point(self):
        list_players_with_score = []
        for match in self.rounds[-1].matchs:
            list_players_with_score.append({
                "player": match[0][0],
                "score": match[0][1],
                "rang": match[0][0].rang
            })
            list_players_with_score.append({
                "player": match[1][0],
                "score": match[1][1],
                "rang": match[1][0].rang
            })
        sorted_players = sorted(list_players_with_score,
                                key=lambda x: getattr(x, "score", "Classement"), reverse=True
                                )
        response = [x for x in sorted_players]
        return response

    def has_played(self, player1, player2):
        for round in self.rounds:
            for match in round.matchs:
                if match[0][0] == player1 and match[1][0] == player2:
                    return True
                if match[0][0] == player2 and match[1][0] == player1:
                    return True
        return False

    def find_opponent_index(self, player, list_players):
        for index, opponent in enumerate(list_players):
            if not self.has_played(player.get("player"), opponent.get("player")):
                return index
        return 0

    def generate_other_round(self):
        list_players = self.sort_by_point()
        list_matchs = []

        while len(list_players) > 1:
            first_player = list_players.pop(0)
            second_player_index = self.find_opponent_index(first_player, list_players)
            second_player = list_players.pop(second_player_index)
            list_matchs.append((
                [first_player.get("player"), first_player.get("score")],
                [second_player.get("player"), second_player.get("score")]
            ))

        round_number = len(self.rounds) + 1
        round = Rounds("Round " + str(round_number), list_matchs)
        self.rounds.append(round)
