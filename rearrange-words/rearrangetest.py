import unittest
from rearrange import isolate_characters

class TestStringSeperation(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(isolate_characters(""), '')


    def test_one_letter(self):
        self.assertEqual(isolate_characters("a"), 'a')
        
    
    def test_already_seperated(self):
        self.assertEqual(isolate_characters("abcd"), 'abcd')
    
       
    def test_seperating(self):
        self.assertEqual(isolate_characters("aab"), 'aba')
        self.assertEqual(isolate_characters("baa"), 'aba')
        self.assertEqual(isolate_characters("fffffaabbbuuu"), 'fbfufufbafabu')
        self.assertEqual(isolate_characters("ffffaabbbuuu"), 'fbfufubabafu')
    
  
         
    def test_cant_seperate(self):
        self.assertEqual(isolate_characters("aaab"), '') 
        self.assertEqual(isolate_characters("fffffffffffffff"), '')  
        self.assertEqual(isolate_characters("ff"), '')               

if __name__ == '__main__':
    unittest.main()
