import json

class Menu:

    def __init__(self) -> None:
        self.arq = 'menu.json'

    def menu(self) -> dict:
        f = open(self.arq)
        data = json.load(f)
        return data
    
    def get_ingredients(self, input:str) -> list:
        menu = self.menu()
        name, *extras = input.split(',')

        if not name in menu:
            return []

        ingredients = menu.get(name)
        
        for extra in extras:

            if '-' in extra[0] and extra[1:] in ingredients:
                ingredients.remove(extra[1:])

            if '+' in extra[0] and not extra[1:] in ingredients:
                ingredients.append(extra[1:])

        return sorted(ingredients)


if __name__ == '__main__':
    mn = Menu()
    print(mn.get_ingredients('Classic,+chocolate,+morango,-pineapple'))
