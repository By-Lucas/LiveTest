from main import Menu
import json

menu = Menu()

class TestMenu:

    def test_menu(self):
        f = open('menu.json')
        data = json.load(f)
        assert menu.menu() == data
    
    def test_ingredients(self):
        assert len(menu.get_ingredients('Classic,+chocolate,+morango,-pineapple')) == 9