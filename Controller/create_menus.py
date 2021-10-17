class CreateMenus:

    main_menu = [("1", "Menu Tournoi"),
                 ("2", "Quitter")
                 ]

    player_menu = [("1", "Lancer le systeme de creation"),
                   ("2", "Mettre a jours les classement"),
                   ("3", "Menu des rapports"),
                   ("4", "Retour au menu principal")
                   ]

    rapport_menu = [("1", "Afficher les rapports du tournoi"),
                    ("2", "Afficher les rapports des joueurs"),
                    ("3", "Retour au menu principal")
                    ]

    players_report_menu = [("1", "Par ordre alphabétique"),
                           ("2", "Par ordre de classement"),
                           ("3", "Pour revenir au menu principal")
                           ]

    def __call__(self, menu_to_display):
        """Display a menu and ask the user to choose"""
        for line in menu_to_display:
            print(line[0] + " : " + line[1])
        while True:
            entry = input("-->")
            for line in menu_to_display:
                if entry == line[0]:
                    return str(line[0])
            print("Vous devez entrer le chiffre correspondant")
