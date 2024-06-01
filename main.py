from character import Character, Enemy, Hero
from weapon import Weapon

hero = Hero("Polina", 200, 20)
enemy = Enemy("Kronk", 150,10)

sword = Weapon("Sword", 10)
axe = Weapon("Axe", 15)
hero.equip(sword)
enemy.equip(axe)

while True:
    hero.attack(enemy)
    print(f'Health of {hero.get_name()}: {hero.hp}')
    print(f'Health of {enemy.id}: {enemy.hp}')
    input()
    hero.battle_cry()
    enemy.speak("get ready for the attack")
    hero.speak("defend yourself")
    enemy.attack(hero)