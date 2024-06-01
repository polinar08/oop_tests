class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def get_damage(self) -> int:
        return self.damage

    def get_name(self) -> str:
        return self.name