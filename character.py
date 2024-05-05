class Character:
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        self.id = name
        self.hp = hp
        self.ma_hp = hp
        self.dmg = dmg
        print("Charachter")

    def attack(self, target) -> None:
        target.hp -= self.dmg
        target.hp = max(target.hp, 0)

    def speak(self, text: str):
        pass

    def get_name(self) -> str:
        return self.id


class Hero(Character):
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        super().__init__(name=name, hp=hp, dmg=dmg)

    def battle_cry(self) -> None:
        print("AAAAAY!")

    def speak(self, text: str):
        print(f"Hello Enemy {text}")


class Enemy(Character):
    def __init__(self, name: str, hp: int, dmg: int) -> None:
        super().__init__(name=name, hp=hp, dmg=dmg)

    def speak(self, text: str):
        print(f"Hello Hero {text}")
