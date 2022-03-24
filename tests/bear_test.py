import unittest

from src.bear import Bear
from src.river import River
from src.fish import Fish


class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear1 = Bear("Yogi", "grizzly") #creating an object called bear_1, using the class Bear with its two arguments
        self.fish1 = Fish("Salmon")

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear1.name)
    
    def test_type_of_bear(self):
        self.assertEqual("grizzly", self.bear1.type)
        
    def test_vol_of_stomach_contents(self):
        self.assertEqual(0, self.bear1.stomach_contents())
        
    def test_add_fish_to_stomach(self):
        self.bear1.add_fish_to_stomach(self.fish1)
        self.assertEqual(1, len(self.bear1.stomach))

        
    def test_bear_take_fish_from_river(self):
        # # the following 6 lines werent needed!!!! not sure if i hard coded it?????? The result is just the block above
                # fish2 = Fish("Cod")
                # fish3 = Fish("Pollock") 
                # river = River("Amazon")
                
                # river.add_fish_to_river(fish2)
                # river.add_fish_to_river(fish3)
                
                # river.remove_fish_from_river(fish2)
        self.bear1.add_fish_to_stomach(self.fish1)
        self.assertEqual(1, len(self.bear1.stomach))
        
        
    def test_bear_can_roar(self):
        self.bear1.bear_roar()
        self.assertEqual("rooooar", self.bear1.bear_roar())
        

            
        
    
        
    


    