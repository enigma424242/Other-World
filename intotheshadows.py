#!/usr/bin/env python
# utf-8

# Author: Enigma
# Contributor: Cheaterman
# Version: '0.03'
# Requires: Python:2.7

# Into the Shadows, is a text-based Role Playing Game.
# The player creates a character, then begins their epic journey into another world.

from lexicon import *
from gamedata import *
from characterdata import *

class Reset(object):

    def menu(self):
        character.char_name = ""
        character.char_class = ""
        character.stats["Health"] = 0
        character.stats["Stamina"] = 0
        character.stats["Mana"] = 0
        character.attributes.update(RESET_DATA["Attributes"])
        character.points = 5
        character.weapons.update(RESET_DATA["Weapons"])
        character.armor.update(RESET_DATA["Armor"])
        character.inventory.update(RESET_DATA["Inventory"])
        return "name"

class Name(object):

    def menu(self):
        print("\n------- Into the Shadows -------\n")
        print("\n-------")
        print("Character Name")
        print("-------\n")
        print("Choose your name.")
        print("-------")
        option = raw_input(">>> ")
        option = edit(option)
        if option.isalnum():
            character.char_name = option
            return "prof"
        else:
            print("That is an invalid option.")
            print("Names must contain alphabetical and/or numerical characters.*")
            return "name"

class Prof(object):

    def menu(self):
        print("\n-------")
        print("Character Class")
        print("-------\n")
        for classes in CREATION_DATA:
            print("{}\n{}\n".format(classes, CLASS_DESCRIPTIONS[classes]))
        print("-------\n")
        print("Choose your class.")
        print("-------")
        option = raw_input(">>> ")
        option = edit(option)
        if option in CREATION_DATA:
            character.char_class = option
            character.attributes.update(CREATION_DATA[option]["Attributes"])
            character.armor.update(CREATION_DATA[option]["Armor"])
            character.weapons.update(CREATION_DATA[option]["Weapons"])
            character.inventory.update(CREATION_DATA[option]["Inventory"])
            return "skills"
        else:
            print("That is an invalid option.")
            return "prof"

class Skills(object):

    # Can pop back to this menu outside the Character Creation.

    def __init__(self, creation=True):
        self.creation = creation

    def menu(self):
        while True:
            character.stats["Health"] = character.attributes["Spirit"] * 3 / 2
            character.stats["Stamina"] = character.attributes["Tolerance"] * 3 / 2
            character.stats["Mana"] = character.attributes["Intellect"] * 3 / 2
            print("\n-------")
            print("Character Skills")
            print("-------\n")
            if self.creation:
                print("Tutorial:")
                print("This menu can be accessed later,")
                print("from the character status menu.")
                print("Use this menu to dedicate points")
                print("towards your attributes.")
                print("-------")
                print("Be sure to spend your points wisely!")
                print("-------\n")
            print("Skills")
            print("--------")
            for stats, values in character.attributes.items():
                print("{}: {}".format(stats, values))
            print("\n-------")
            print("Points: {}".format(character.points))
            print("-------\n")
            print("-------")
            print("*Select 'Continue' for character status.")
            print("Which skill would you like to increase?")
            print("-------")
            option = raw_input(">>> ")
            option = edit(option)
            if option in character.attributes:
                while True:
                    print("\n")
                    print("Points: {}".format(character.points))
                    print("-------\n")
                    print("*Select 'Back' to return to skills.")
                    print("-------")
                    print("How many points would you like to dedicate towards %s?"
                        % option.lower())
                    print("-------")
                    i_option = raw_input(">>> ")
                    try:
                        i_option = int(i_option)
                        if i_option <= character.points and i_option > 0:
                            character.attributes[option] += i_option
                            character.points -= i_option
                            break
                        else:
                            print("That is an improper value.")
                            break
                    except ValueError:
                        i_option = edit(i_option)
                        if i_option == "Back":
                            break
                        else:
                            print("That is an improper value.")
                            continue
            elif option == "Continue":
                if self.creation:
                    return "status"
                else:
                    return "_status"
            else:
                print("That is an invalid option.")
                continue

class Status(object):

    # Last menu inside the Character Creation.
    # Can pop back to this menu outside the Character Creation

    def __init__(self, creation=True):
        self.creation = creation

    def menu(self):
        print("\n-------")
        print("Character Status")
        print("-------\n")
        print("Name: {}".format(character.char_name))
        print("Class: {}".format(character.char_class))
        print("-------")
        print("Health: {}".format(character.stats["Health"]))
        print("Stamina: {}".format(character.stats["Stamina"]))
        print("Mana: {}".format(character.stats["Mana"]))
        print("-------")
        primary = character.weapons["Primary"]
        secondary = character.weapons["Secondary"]
        print("Primary Weapon: +{} {}".format(WEAPON_DATA[primary], primary))
        print("Secondary Weapon: +{} {}".format(WEAPON_DATA[secondary], secondary))
        print("-------")
        for attributes, values in character.attributes.items():
            print("{}: {}".format(attributes, values))
        print("-------")
        print("Points: {}".format(character.points))
        print("-------")
        for sections, items in character.armor.items():
            print("{}: +{} {}".format(sections, ARMOR_DATA[items], items))
        print("-------")
        print("Select 'Skills' for character attributes.")
        if self.creation:
            print("Select 'Exit' to begin your adventure.")
            print("Select 'Reset' to restart the character creation.")
            print("-------")
            option = raw_input(">>> ")
            option = edit(option)
            if option == "Exit":
                exit(0)
            elif option == "Skills":
                return "skills"
            elif option == "Reset":
                return "reset"
            else:
                print("That is an invalid option.")
                return "status"
        else:
            print("*Select 'Exit' to return to the main menu.")
            print("-------")
            option = raw_input(">>> ")
            option = edit(option)
            if option == "Exit":
                return "main"
            elif option == "Skills":
                return "_skills"
            else:
                print("That is an invalid option.")
                return "_status"

class Main(object):

    def menu(self):
        print("\n-------")
        print("Main Menu")
        print("-------\n")
        print("-------")
        print("Status")
        print("Back")
        print("Save")
        print("Quit")
        print("-------")
        print("*The 'Save' option is not configured yet.")
        option = raw_input(">>> ")
        option = edit(option)
        if option == "Status":
            return "_status"
        elif option == "Back":
            exit(0)
        elif option == "Quit":
            exit(0)
        else:
            print("That is an invalid option.")
            return "main"

class Inventory(object):

    def menu(self):
        print("\n-------")
        print("Inventory")
        print("-------\n")
        wears = []
        for catagories in character.inventory:
            print("{}".format(catagories))
            for slots, items in character.inventory[catagories].items():
                print("{}: {}".format(slots, items))
                wears.append(items)
        while True:
            print("-------")
            print("Back")
            print("-------")
            option = raw_input(">>> ")
            option = edit(option)
            if option in wears:
                print("\n-------")
                print(option)
                print("-------\n")
                if option in MYSTERY_DATA:
                    print(MYSTERY_DATA[option])
                continue
            elif option == "Back":
                exit(0)
            else:
                print("That is an invalid option.")
                return "inventory"

class Engine(object):

    """A small finite state machine.
    
    Whatever is returned from the current menu is set to following_phase.
    following_phase is then called from self.phase, and repeated.
    """

    phase = {
        "reset": Reset(),
        "name": Name(),
        "prof": Prof(),
        "skills": Skills(creation=True),
        "status": Status(creation=True),
        "_skills": Skills(creation=False),
        "_status": Status(creation=False)
    }

    def __init__(self, start_phase):
        self.start_phase = start_phase

    def play(self):
        current_phase = self.current()
        while True:
            following_phase = current_phase.menu()
            current_phase = self.following(following_phase)

    def current(self):
        return self.following(self.start_phase)

    def following(self, next_phase):
        return self.phase[next_phase]

character = Character()
engine = Engine("reset")
engine.play()
