import unittest
from  rod import max_combination

class TestRodCost(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_combination(0,[]), None)
        self.assertEqual(max_combination(4,[0,0,0,0]), [4,0,0,0])


    def test_same_cost(self):
        self.assertEqual(max_combination(3,[1,1,1]), [3,0,0])
        self.assertEqual(max_combination(3,[4,4,4]), [3,0,0])
        self.assertEqual(max_combination(1,[1]), [1])
     
        
       
    def test_max(self):
     self.assertEqual(max_combination(3,[1,1,4]), [0,0,1])
     self.assertEqual(max_combination(3,[2,5,1]), [1,1,0])
     self.assertEqual(max_combination(3,[3,5,1]), [3,0,0])
     self.assertEqual(max_combination(8,[1,5,8,9,10,17,17,20]), [0,1,0,0,0,1,0,0])
    
  

if __name__ == '__main__':
    unittest.main()
