import unittest

from src.fish import Fish


class TestFish(unittest.TestCase):
    def setUp(self):
        self.fish1 = Fish("Salmon")
        
    def test_fish_has_name(self):
        self.assertEqual("Salmon", self.fish1.name)