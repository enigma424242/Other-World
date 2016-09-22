#!/usr/bin/env python
# utf-8

# Author: Enigma
# Contributor: Cheaterman
# Version: '0.04'
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
        return 'name'

class Name(object):

    def menu(self):
        print("\n------- Into the Shadows -------\n")
        print("\n-------")
        print("Character Name")
        print("-------\n")
        print("Choose your name.")
        print("-------")
        opt = raw_input(">>> ")
        opt = edit(opt)
        if opt.isalnum():
            character.char_name = opt
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
        opt = raw_input(">>> ")
        opt = edit(opt)
        if opt in CREATION_DATA:
            character.char_class = opt
            character.attributes.update(CREATION_DATA[opt]["Attributes"])
            character.armor.update(CREATION_DATA[opt]["Armor"])
            character.weapons.update(CREATION_DATA[opt]["Weapons"])
            character.inventory.update(CREATION_DATA[opt]["Inventory"])
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
            opt = raw_input(">>> ")
            opt = edit(opt)
            if opt in character.attributes:
                self.dedicate(opt)
            elif opt == "Continue":
                if self.creation:
                    character.regen()
                    return "status"
                else:
                    return "_status"
            else:
                print("That is an invalid option.")
                continue

    def dedicate(self, opt):
        while True:
            print("\n-------")
            print("Points: {}".format(character.points))
            print("-------\n")
            print("*Select 'Back' to return to skills.")
            print("-------")
            print("How many points would you like to dedicate towards %s?"
                % opt.lower())
            print("-------")
            i_opt = raw_input(">>> ")
            try:
                i_opt = int(i_opt)
                if i_opt <= character.points and i_opt > 0:
                    character.attributes[opt] += i_opt
                    character.points -= i_opt
                    break
                else:
                    print("That is an improper value.")
                    continue
            except ValueError:
                i_opt = edit(i_opt)
                if i_opt == "Back":
                    return "skills"
                else:
                    print("That is an improper value.")
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
            opt = raw_input(">>> ")
            opt = edit(opt)
            if opt == "Exit":
                exit(0)
            elif opt == "Skills":
                return "skills"
            elif opt == "Reset":
                return "reset"
            else:
                print("That is an invalid option.")
                return "status"
        else:
            print("*Select 'Exit' to return to the main menu.")
            print("-------")
            opt = raw_input(">>> ")
            opt = edit(opt)
            if opt == "Exit":
                return "main"
            elif opt == "Skills":
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
        opt = raw_input(">>> ")
        opt = edit(opt)
        if opt == "Status":
            return "_status"
        elif opt == "Back":
            exit(0)
        elif opt == "Quit":
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
            opt = raw_input(">>> ")
            opt = edit(opt)
            if opt in wears:
                print("\n-------")
                print(opt)
                print("-------\n")
                if opt in MYSTERY_DATA:
                    print(MYSTERY_DATA[opt])
                continue
            elif opt == "Back":
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
