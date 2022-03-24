import unittest

from src.river import River
from src.fish import Fish


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
        
    

        
        