#!/usr/bin/env python
# utf-8

## Text Based Role Playing Game ##

# Author: Enigma
# Contributor: Cheaterman
# Version: '0.03'
# Requires: Python:2.7

from gamedata import *
from characterdata import *

class Reset(object):

    def meth(self):
        character.char_name = ''
        character.char_class = ''
        character.health = 0
        character.stamina = 0
        character.mana = 0
        character.points = 5
        character.attributes.update(RESET_DATA['attributes'])
        character.weapons.update(RESET_DATA['weapons'])
        character.armor.update(RESET_DATA['armor'])
        character.inventory.update(RESET_DATA['inventory'])
        return 'name'

class Name(object):

    def meth(self):
        print("\n------- Into the Shadows -------\n")
        print("Character Creation")
        print("\n-------")
        print("Character Name")
        print("-------\n")
        print("What is your name?")
        option = raw_input(">>> ")
        if option.isalnum():
            character.char_name = option
            return 'prof'
        else:
            print("That is an invalid option.")
            print("Names must contain alphabetical and/or numerical characters.*")
            return 'name'

class Prof(object):

    def meth(self):
        print("\n-------")
        print("Character Class")
        print("-------\n")
        print("Classes")
        for classes in CREATION_DATA:
            print("\n{}\n{}".format(classes, CLASS_DESCRIPTIONS[classes]))
        print("-------\n")
        print("What is your class?")
        option = raw_input(">>> ")
        if option in CREATION_DATA:
            character.char_class = option
            character.attributes.update(CREATION_DATA[option]['attributes'])
            character.armor.update(CREATION_DATA[option]['armor'])
            character.weapons.update(CREATION_DATA[option]['weapons'])
            character.inventory.update(CREATION_DATA[option]['inventory'])
            return 'skills'
        else:
            print("That is an invalid option.")
            return 'prof'

class Skills(object):

    def __init__(self, creation=True):
        self.creation = creation

    def meth(self):
        while True:
            character.health = character.attributes['spirit'] * 3 / 2
            character.stamina = character.attributes['tolerance'] * 3 / 2
            character.mana = character.attributes['intellect'] * 3 / 2
            print("\n-------")
            print("Character Skills")
            print("-------\n")
            if self.creation:
                print("Tutorial:")
                print("This menu can be accessed later,")
                print("from the character status menu.")
                print("Use this menu to dedicate points")
                print("towards your attributes.")
                print("Be sure to spend your points wisely!")
                print("-------\n")
            print("Skills")
            for stats, values in character.attributes.items():
                print("{}: {}".format(stats, values))
            print("-------")
            print("Points: {}".format(character.points))
            print("-------\n")
            print("*Select 'exit' for character status.*")
            print("-------")
            print("Which skill would you like to increase?")
            option = raw_input(">>> ")
            if option in character.attributes:
                print("\n")
                print("Points: {}".format(character.points))
                print("-------\n")
                print("How many points would you like to dedicate towards %s?" % option)
                try:
                    i_option = int(raw_input(">>> "))
                    if int(i_option) > character.points or i_option <= 0:
                        print("That is an improper value.")
                        continue
                    else:
                        character.attributes[option] += i_option
                        character.points -= i_option
                        continue
                except ValueError:
                    print("That is an improper value.")
                    continue
            elif option == 'exit':
                if self.creation:
                    return 'status'
                else:
                    return '_status'
            else:
                print("That is an invalid option.")
                continue

class Status(object):

    def __init__(self, creation=True):
        self.creation = creation

    def meth(self):
        print("\n")
        print("Character Status")
        print("-------\n")
        print("Name: {}".format(character.char_name))
        print("Class: {}".format(character.char_class))
        print("-------")
        print("Health: {}".format(character.health))
        print("Stamina: {}".format(character.stamina))
        print("Mana: {}".format(character.mana))
        print("-------")
        print("Primary Weapon: {}".format(character.weapons['primary']))
        print("Secondary Weapon: {}".format(character.weapons['secondary']))
        print("-------")
        for stats, values in character.attributes.items():
            print("{}: {}".format(stats, values))
        print("-------")
        print("Points: {}".format(character.points))
        print("-------")
        for gear, values in character.armor.items():
            print("{}: {}".format(gear, values))
        print("-------")
        print("Select 'skills' for character attributes.")
        if self.creation:
            print("Select 'exit' to quit the character creation and begin your adventure.")
            print("Select 'reset' to discard and restart the character creation.")
            option = raw_input(">>> ").lower()
            if option == 'exit':
                return 'hangmans_forest'
            elif option == 'skills':
                return 'skills'
            elif option == 'reset':
                return 'reset'
            else:
                print("That is an invalid option.")
                return 'status'
        else:
            print("*Select 'back' to return to the main menu.*")
            option = raw_input(">>> ").lower()
            if option == 'back':
                return 'main menu'
            elif option == 'skills':
                return '_skills'
            else:
                print("That is an invalid option.")
                return '_status'

class HangmansForest(object):

    def meth(self):
        print("\n-------")
        print("Hangmans Forest")
        print("-------\n")
        print("{}".format(MAP_DATA['hangmans forest']))
        print("-------")
        print("main menu")
        print("inventory")
        print("-------")
        option = raw_input(">>> ").lower()
        if option == 'main menu':
            return 'main menu'
        elif option == 'inventory':
            return 'inventory'
        else:
            print("That is an invalid option.")
            return 'hangmans_forest'

class MainMenu(object):

    def meth(self):
        print("\n-------")
        print("Main Menu")
        print("-------\n")
        print("status")
        print("back")
        print("quit")
        print("-------")
        option = raw_input(">>> ").lower()
        if option == 'status':
            return '_status'
        elif option == 'back':
            return 'hangmans_forest'
        elif option == 'quit':
            exit(0)
        else:
            print("That is an invalid option.")
            return 'main menu'

class Inventory(object):

    def meth(self):
        print("\n-------")
        print("Inventory")
        print("-------\n")
        for catagories in character.inventory:
            print("{}".format(catagories))
            for slots, items in character.inventory[catagories].items():
                print("{}: {}".format(slots, items))
        while True:
            print("-------\n")
            print("back")
            option = raw_input(">>> ")
            if option in MYSTERY_DATA:
                for catagories in character.inventory:
                    for slots, items in character.inventory[catagories].items():
                        if option in items:
                            print(MYSTERY_DATA[option])
                            continue
            elif option == 'back':
                return 'hangmans_forest'
            else:
                print("That is an invalid option.")
                return 'inventory'

class Engine(object):

    """A small finite state machine."""

    phase = {
        'reset': Reset(),
        'name': Name(),
        'prof': Prof(),
        'skills': Skills(creation=True),
        'status': Status(creation=True),
        '_skills': Skills(creation=False),
        '_status': Status(creation=False),
        'main menu': MainMenu(),
        'inventory': Inventory(),
        'hangmans_forest': HangmansForest()
    }

    def __init__(self, start_phase):
        self.start_phase = start_phase

    def play(self):
        current_phase = self.current()
        while True:
            following_phase = current_phase.meth()
            current_phase = self.following(following_phase)

    def current(self):
        return self.following(self.start_phase)

    def following(self, next_phase):
        return self.phase[next_phase]

character = Character()

engine = Engine('reset')
engine.play()
