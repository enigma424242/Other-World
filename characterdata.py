class Character(object):

    def __init__(self):
        self.char_name = ""
        self.char_class = ""
        self.stats = {
            "Health": 0,
            "Stamina": 0,
            "Mana": 0
        }
        self.attributes = {
            "Spirit": 0,
            "Tolerance": 0,
            "Intellect": 0,
            "Strength": 0,
            "Dexterity": 0
        }
        self.weapons = {
            "Primary": "",
            "Secondary": ""
        }
        self.armor = {
            "Head": "",
            "Torso": "",
            "Hands": "",
            "Legs": ""
        }
        self.inventory = {
            "Armor": {
                "Slot1": "",
                "Slot2": "",
                "Slot3": "",
                "Slot4": ""
            },
            'Weapons': {
                "Slot1": "",
                "Slot2": "",
                "Slot3": "",
                "Slot4": ""
            },
            'Consumables': {
                "Slot1": "",
                "Slot2": "",
                "Slot3": "",
                "Slot4": ""
            },
            'Reusables': {
                "Slot1": "",
                "Slot2": "",
                "Slot3": "",
                "Slot4": ""
            }
        }

    def regen(self):
        self.stats["Health"] = self.attributes['Spirit'] * 3 / 2
        self.stats["Stamina"] = self.attributes['Tolerance'] * 3 / 2
        self.stats["Mana"] = self.attributes['Intellect'] * 3 / 2
