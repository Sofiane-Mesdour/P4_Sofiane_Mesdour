from tinydb import TinyDB
from Controller import tournoi_controller
import sys

from models import Serialized
from views import menu
from Controller.create_menus import CreateMenus
from Controller.debut import Debut
from Controller import player_controller

db = TinyDB('dbPlayer.json')
players_table = db.table
dbs = TinyDB('dbTournoi.json')
tournoi_table = dbs.table


class HomeMenuController:
    """Display the title and leads to the main menu"""

    def __init__(self):
        self.view = menu.MainDisplay()
        self.clear = menu.ClearScreen()
        self.create_menu = CreateMenus()
        self.choosen_controller = None

    def __call__(self):
        self.clear()
        self.view.display_title()
        entry = self.create_menu(self.create_menu.main_menu)

        if entry == "1":
            self.choosen_controller = PlayerMenuController()
            self.go_to_player_menu_controller()

        if entry == "2":
            self.choosen_controller = QuitAppController()
            self.go_to_quit_app_controller()

    def go_to_player_menu_controller(self):
        return self.choosen_controller()

    def go_to_tournament_menu_controller(self):
        return self.choosen_controller()

    def go_to_quit_app_controller(self):
        return self.choosen_controller()


class PlayerMenuController(HomeMenuController):

    def __init__(self):
        super().__init__()

        self.create_tournoi = Debut.lancement
        self.home_menu_controller = HomeMenuController()
        self.rapport = RapportMenu()
        self.update = Serialized.Seria.update_ranking

    def __call__(self):
        self.clear()
        entry = self.create_menu(self.create_menu.player_menu)
        if entry == "1":
            self.tournoi = self.create_tournoi()
            self.choosen_controller = self.home_menu_controller()
        if entry == "2":
            self.choosen_controller = self.update()
            self.choosen_controller = self.home_menu_controller()
        if entry == "3":
            self.rapport()
            self.choosen_controller = self.home_menu_controller()
        if entry == "4":
            self.choosen_controller = self.home_menu_controller()


class RapportMenu(HomeMenuController):

    def __init__(self):
        super().__init__()
        self.rapport_player = player_controller.PlayerReport()
        self.rapport_tournoi = tournoi_controller.TournoiReport()
        self.home_menu_controller = HomeMenuController()

    def __call__(self):
        self.clear()
        entry = self.create_menu(self.create_menu.rapport_menu)
        if entry == "1":
            self.choosen_controller = self.rapport_tournoi()
        if entry == "2":
            self.choosen_controller = self.rapport_player()
        if entry == "3":
            self.choosen_controller = self.home_menu_controller()


class QuitAppController:

    def __call__(self):
        sys.exit()
