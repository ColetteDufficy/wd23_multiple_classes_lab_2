class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []
        
    def stomach_contents(self):
        return len(self.stomach)

    def add_fish_to_stomach(self, fish):
        self.stomach.append(fish)
    
    # # this block wasnt needed. See bear_test.py for further note
    # def remove_fish_from_river(self, river):
    #     for fish in self.stomach:
    #         river.fish_stock.remove(fish)

    def bear_roar(self):
        return "rooooar"