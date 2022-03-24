class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []
        
    def stomach_contents(self):
        return len(self.stomach)

    def add_fish_to_stomach(self, fish):
        self.stomach.append(fish)
    
    def remove_fish_from_river(self, river):
        for fish in self.stomach:
            river.fish_stock.remove(fish)
