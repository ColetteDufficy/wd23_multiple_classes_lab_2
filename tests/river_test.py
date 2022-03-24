import unittest

from src.river import River
from src.fish import Fish
from src.bear import Bear


class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River("Amazon")
        self.fish1 = Fish("Salmon")

        
    def test_river_has_name(self):
        self.assertEqual("Amazon", self.river.name)
        
    def test_add_fish_to_river(self):
        fish2 = Fish("Cod")
        fish3 = Fish("Pollock")
        self.river.add_fish_to_river(self.fish1)
        self.river.add_fish_to_river(fish2)
        self.river.add_fish_to_river(fish3)
        self.assertEqual(3, len(self.river.fish_stock))
        
        
    def test_river_loses_a_fish_when_taken_by_bear(self):
        self.river.add_fish_to_river(self.fish1)
        self.river.remove_fish_from_river(self.fish1)
        self.assertEqual(0, len(self.river.fish_stock))
        
        
    def test_river_fish_count(self):
        self.assertEqual(0, self.river.fish_count())
        
    

        
        