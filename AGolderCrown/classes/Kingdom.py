from classes.Constants import Constants

class Kingdom:
    allies = []
    def __init__(self, name):
        self.name = name
        self.king = Constants.KINGDOM_EMBLEM_MAP[self.name]

    def get_name(self):
        return self.name

    def get_allies(self):
        return ' ,'.join([str(a) for a in self.allies])

    def set_allies(self, ally):
        Kingdom.allies.append(ally)

    def __str__(self):
        return str(self.name)
