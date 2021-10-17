from views import menu
from Controller import main_controller
from tinydb import TinyDB


class TournoiReport:
    """Display the player's report"""

    def __init__(self):
        self.display_tournoi = menu.DisplayTournoiReport()
        self.home_menu_controller = main_controller.HomeMenuController()

    def __call__(self):
        tournoi_serialized = []
        dbs = TinyDB('dbTournoi.json')

        for t in dbs.table('Tournoi'):
            tournoi_serialized.append(t)

        self.display_tournoi()

        choice = input("--> ")

        if choice == "1":
            self.display_tournoi.display_tournoi(tournoi_serialized)
            TournoiReport.__call__(self)

        if choice == "2":
            self.display_tournoi.display_round(tournoi_serialized)
            TournoiReport.__call__(self)

        if choice == "3":
            self.home_menu_controller()
