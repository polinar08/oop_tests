from character import Character, Enemy, Hero

hero = Hero("Polina", 100, 20)
enemy = Enemy("Kronk", 50,10)


while True:
    hero.attack(enemy)
    print(f'Health of {hero.get_name()}: {hero.hp}')
    print(f'Health of {enemy.id}: {enemy.hp}')
    input()
    hero.battle_cry()
    enemy.speak("get ready for the attack")
    hero.speak("defend yourself")
