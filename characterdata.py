class Character(object):

    def __init__(self):
        self.char_name = ''
        self.char_class = ''
        self.health = 0
        self.stamina = 0
        self.mana = 0
        self.points = 5
        self.attributes = {
            'spirit': 0,
            'tolerance': 0,
            'intellect': 0,
            'strength': 0,
            'dexterity': 0
        }
        self.weapons = {
            'primary': '',
            'secondary': ''
        }
        self.armor = {
            'head': '',
            'torso': '',
            'hands': '',
            'legs': ''
        }
        self.inventory = {
            'armor': {
                'slot1': '',
                'slot2': '',
                'slot3': '',
                'slot4': ''
            },
            'weapons': {
                'slot1': '',
                'slot2': '',
                'slot3': '',
                'slot4': ''
            },
            'consumables': {
                'slot1': '',
                'slot2': '',
                'slot3': '',
                'slot4': ''
            },
            'reusables': {
                'slot1': '',
                'slot2': '',
                'slot3': '',
                'slot4': ''
            }
        }
