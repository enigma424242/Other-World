#!/usr/bin/env python
# utf-8

## Text Based Role Playing Game ##

# Author: Enigma
# Contributor: Cheaterman
# Version: '0.03'
# Requires: Python:2.7

from gamedata import *
from characterdata import *
from lexicon import *

class Reset(object):

    def meth(self):
        character.char_name = ''
        character.char_class = ''
        character.health = 0
        character.stamina = 0
        character.mana = 0
        character.points = 5
        character.attributes.update(RESET_DATA['Attributes'])
        character.weapons.update(RESET_DATA['Weapons'])
        character.armor.update(RESET_DATA['Armor'])
        character.inventory.update(RESET_DATA['Inventory'])
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
        option = edit(option)
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
        option = edit(option)
        if option in CREATION_DATA:
            character.char_class = option
            character.attributes.update(CREATION_DATA[option]['Attributes'])
            character.armor.update(CREATION_DATA[option]['Armor'])
            character.weapons.update(CREATION_DATA[option]['Weapons'])
            character.inventory.update(CREATION_DATA[option]['Inventory'])
            return 'skills'
        else:
            print("That is an invalid option.")
            return 'prof'

class Skills(object):

    def __init__(self, creation=True):
        self.creation = creation

    def meth(self):
        while True:
            character.health = character.attributes['Spirit'] * 3 / 2
            character.stamina = character.attributes['Tolerance'] * 3 / 2
            character.mana = character.attributes['Intellect'] * 3 / 2
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
            print("*Select 'Exit' for character status.*")
            print("-------")
            print("Which skill would you like to increase?")
            option = raw_input(">>> ")
            option = edit(option)
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
            elif option == 'Exit':
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
        health = character.health
        stamina = character.stamina
        mana = character.mana
        char_name = character.char_name
        char_class = character.char_class
        attributes = character.attributes
        points = character.points
        armor = character.armor
        primary = character.weapons['Primary']
        secondary = character.weapons['Secondary']
        print("\n-------")
        print("Character Status")
        print("-------\n")
        print("Name: {}".format(char_name))
        print("Class: {}".format(char_class))
        print("-------")
        print("Health: {}".format(health))
        print("Stamina: {}".format(stamina))
        print("Mana: {}".format(mana))
        print("-------")
        print("Primary Weapon: +{} {}".format(WEAPON_DATA[primary], primary))
        print("Secondary Weapon: +{} {}".format(WEAPON_DATA[secondary], secondary))
        print("-------")
        for stats, values in attributes.items():
            print("{}: {}".format(stats, values))
        print("-------")
        print("Points: {}".format(points))
        print("-------")
        for gear, items in armor.items():
            print("{}: +{} {}".format(gear, ARMOR_DATA[items], items))
        print("-------")
        print("Select 'Skills' for character attributes.")
        if self.creation:
            print("Select 'Exit' to quit the character creation and begin your adventure.")
            print("Select 'Reset' to discard and restart the character creation.")
            option = raw_input(">>> ")
            option = edit(option)
            if option == 'Exit':
                return 'hangmans_forest'
            elif option == 'Skills':
                return 'skills'
            elif option == 'Reset':
                return 'reset'
            else:
                print("That is an invalid option.")
                return 'status'
        else:
            print("*Select 'Back' to return to the main menu.*")
            option = raw_input(">>> ")
            option = edit(option)
            if option == 'Back':
                return 'main menu'
            elif option == 'Skills':
                return '_skills'
            else:
                print("That is an invalid option.")
                return '_status'

class HangmansForest(object):

    def meth(self):
        print("\n-------")
        print("Hangmans Forest")
        print("-------\n")
        print("{}".format(MAP_DATA['Hangmans Forest']))
        print("-------")
        print("Main menu")
        print("Inventory")
        print("-------")
        option = raw_input(">>> ")
        option = edit(option)
        if option == 'Main menu':
            return 'main menu'
        elif option == 'Inventory':
            return 'inventory'
        else:
            print("That is an invalid option.")
            return 'hangmans_forest'

class MainMenu(object):

    def meth(self):
        print("\n-------")
        print("Main Menu")
        print("-------\n")
        print("Status")
        print("Back")
        print("Quit")
        print("-------")
        option = raw_input(">>> ")
        option = edit(option)
        if option == 'Status':
            return '_status'
        elif option == 'Back':
            return 'hangmans_forest'
        elif option == 'Quit':
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
            print("Back")
            option = raw_input(">>> ")
            option = edit(option)
            if option in MYSTERY_DATA:
                for catagories in character.inventory:
                    for slots, items in character.inventory[catagories].items():
                        if option in items:
                            print(MYSTERY_DATA[option])
                            continue
            elif option == 'Back':
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
