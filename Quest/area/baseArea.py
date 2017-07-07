class baseArea():
    def __init__(self, name, event, description):
        self.name = name
        self.event = event
        self.description = description

    def event(self, party, people):
        """place locational events here"""
        print("Default Event Action")
