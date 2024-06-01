from weapon import Weapon


class Character:
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        self.id = name
        self.hp = hp
        self.ma_hp = hp
        self.dmg = dmg
        self._weapon = None
        print("Charachter")

    def attack(self, target) -> None:
        total_damage = self.dmg
        if self._weapon:
            total_damage += self._weapon.get_damage()
        target.receive_damage(total_damage)

    def receive_damage(self, damage: int) -> None:
        self.hp -= damage
        self.hp = max(self.hp, 0)

    def speak(self, text: str):
        pass

    def get_name(self) -> str:
        return self.id

    def equip(self, weapon: Weapon) -> None:
        self._weapon = weapon
        print(f'{self.get_name()} equipped {weapon.get_name()}')


class Hero(Character):
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        super().__init__(name=name, hp=hp, dmg=dmg)

    def battle_cry(self) -> None:
        print("AAAAAY!")

    def speak(self, text: str):
        print(f"Hello Kronk {text}")


class Enemy(Character):
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        super().__init__(name=name, hp=hp, dmg=dmg)

    def speak(self, text: str):
        print(f"OH Hi there Hero {text}")
