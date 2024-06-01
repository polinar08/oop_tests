from character import Character, Enemy, Hero


class CharacterController:
    def __init__(self):
        self._heros = []
        self._enemies = []

    def add_character(self, name: str, hp: int, dmg: int) -> None:
        hero = Hero(name, hp, dmg)
        self._heros.append(hero)

    def add_enemy(self, name: str, hp: int, dmg: int) -> None:
        enemy = Enemy(name, hp, dmg)
        self._enemies.append(enemy)

    def remove_hero(self, index: int) -> None:
        self._heros.pop(index)

    def remove_enemy(self, index: int) -> None:
        self._enemies.pop(index)

    def update(self) -> None:
        print(len(self._heros), len(self._enemies))
