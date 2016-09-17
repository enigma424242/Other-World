class Character(object):

    def __init__(self):
        self.char_name = ""
        self.char_class = ""
        self.health = 0
        self.stamina = 0
        self.mana = 0
        self.points = 0
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
