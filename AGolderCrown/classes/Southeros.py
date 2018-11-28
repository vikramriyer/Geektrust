from classes.Kingdom import Kingdom
from classes.Message import Message
from classes.Constants import Constants

class Southeros:

    def __init__(self):
        self.kingdoms = self.initialize_kingdoms()
        self.competing_kingdoms = {}

    def initialize_kingdoms(self):
        return {
            'space': Kingdom('space'),
            'land': Kingdom('land'),
            'water': Kingdom('water'),
            'ice': Kingdom('ice'),
            'air': Kingdom('air'),
            'fire': Kingdom('fire')
        }

    def get_all_kingdoms(self):
        return [self.space.get_name(), self.land.get_name(), self.water.get_name(),
        self.ice.get_name(), self.air.get_name(), self.fire.get_name()]

    def get_ruler(self):
        ruler = None
        max_votes = 0
        is_tie = False
        for kingdom in self.competing_kingdoms.keys():
            votes = self.competing_kingdoms[kingdom]
            if votes > max_votes:
                ruler = kingdom
                max_votes = votes
                is_tie = False
            elif votes == max_votes:
                is_tie = True
        if is_tie:
            return None
        else:
            return ruler

    def get_ruler_allies():
        pass

    def set_competing_kingdoms(self, kingdom):
        if kingdom in self.competing_kingdoms:
            self.competing_kingdoms[kingdom] += 1
        else:
            self.competing_kingdoms[kingdom] = 1

    def send_message(self, from_kingdom, to_kingdom, message):
        from_kingdom = self.kingdoms[from_kingdom]
        to_kingdom = self.kingdoms[to_kingdom]
        self.set_competing_kingdoms(from_kingdom)
        message = Message(from_kingdom, to_kingdom, message)
        if message.is_code_present():
            from_kingdom.set_allies(to_kingdom)

    def __str__(self):
        return 'Kingdoms: ' + ' '.join([str(k) for k in self.kingdoms])
