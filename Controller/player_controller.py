from operator import attrgetter
from views import menu
from models import Serialized
from Controller import main_controller


class PlayerReport:
    """Display the player's report"""

    def __init__(self):
        self.display_player = menu.DisplayPlayersReport()
        self.players_database = Serialized.players_table
        self.player = Serialized.Seria()
        self.home_menu_controller = main_controller.HomeMenuController()

    def __call__(self):
        player_serialized = []
        # self.players_database = pd.read_json("models/players.json")

        for player in self.players_database:
            player_serialized.append(self.player.unserialized(player))

        self.display_player()
        choice = input("--> ")
        if choice == "1":
            player_serialized.sort(key=attrgetter("name"))
            self.display_player.display_alphabetical(player_serialized)
            PlayerReport.__call__(self)
        if choice == "2":
            player_serialized.sort(key=attrgetter("rang"))
            self.display_player.display_ranking(player_serialized)
            PlayerReport.__call__(self)
        if choice == "3":
            self.home_menu_controller()
