import random

from Character_controller import CharacterController
from weapon import Weapon
import time
import tkinter as tk

names = ["Morva", "Draven", "Thalia", "Vesper", "Zorin", "Kyra", "Ragnar", "Seraphine", "Malek", "Lilith"]
min_hp = 10
max_hp = 150
min_dmg = 1
max_dmg = 100
CC = CharacterController()

CC.add_character("Polina", 200, 20)
CC.add_enemy("Kronk", 150, 10)

sword = Weapon("Sword", 10)
axe = Weapon("Axe", 15)
# hero.equip(sword)
# enemy.equip(axe)

root = tk.Tk()
root.title("Character Controller")
root.geometry("300x200")

input_label = tk.Label(root, text="User input: ")
input_label.pack(pady=10)


def handle_input(event):
    user_input = event.char
    input_label.config(text=f"User input: {user_input}")

    if user_input == "a":
        CC.add_character(names[random.randint(0, len(names)-1)], random.randint(min_hp, max_hp), random.randint(min_dmg, max_dmg))

    CC.update()


root.bind('<Key>', handle_input)

root.mainloop()
