class River:
    def __init__(self, name):
        self.name = name
        self.fish_stock = []
        
    def add_fish_to_river(self, fish):
        self.fish_stock.append(fish)

    def remove_fish_from_river(self, fish):
        self.fish_stock.remove(fish)

    def fish_count(self):
        return len(self.fish_stock)