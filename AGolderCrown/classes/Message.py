from classes.Constants import Constants

class Message:
    def __init__(self, from_kingdom, to_kingdom, message):
        self.from_kingdom = from_kingdom
        self.to_kingdom = to_kingdom
        self.message = message

    def is_code_present(self):
        from_kingdom = self.from_kingdom
        to_kingdom = self.to_kingdom
        message = self.message.lower()
        desired_message = Constants.KINGDOM_EMBLEM_MAP[str(to_kingdom)]
        for s in desired_message:
            if s in message:
                message = message.replace(s,'',1)
            else:
                return False
        return True
