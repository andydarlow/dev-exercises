import unittest
from  compareStringList import chars_in_strings, same_string_functional, same_string_iterator, any_matching

list_of = lambda i: [z for z in i]
 
class TestStringComparison(unittest.TestCase):

    def test_generator_empty_list(self):
        self.assertEqual(list_of(chars_in_strings([])), [])
     
        
    def test_generator_single_item(self):
         self.assertEqual(list_of(chars_in_strings(["hello"])), ['h', 'e', 'l', 'l', 'o'])
     
          
    def test_generator_multi_items(self):
         self.assertEqual(list_of(chars_in_strings(["hello","l","ii","9uh"])), ['h', 'e', 'l', 'l', 'o', 'l', 'i', 'i', '9', 'u', 'h'])
       
     
    def test_any_matching(self):
         self.assertTrue(any_matching(lambda a: a==1,[3,8,1,2]))
         self.assertFalse(any_matching(lambda a: a==90,[3,8,1,2]))

    def test_same_string_functional(self):
         self.assertTrue(same_string_functional(["abc","d","ef","g"], ["abcdefg"]))
         self.assertTrue(same_string_functional(["abc","d","ef","gh"], ["abc", "defg","h"]))
         self.assertFalse(same_string_functional(["abc","d","ef","g"], []))
         self.assertFalse(same_string_functional(["abc","d","ef","g"], [""]))
  
         self.assertTrue(same_string_functional(["abc","d","ef","g"], ["abc", "defg"]))
         self.assertFalse(same_string_functional(["abc","d","ef","g"], ["abc", "def"]))
         
    def test_same_string_iterator(self):
         self.assertTrue(same_string_iterator(["abc","d","ef","g"], ["abcdefg"]))
         self.assertTrue(same_string_iterator(["abc","d","ef","gh"], ["abc", "defg","h"]))
         self.assertFalse(same_string_iterator(["abc","d","ef","g"], []))
         self.assertFalse(same_string_iterator(["abc","d","ef","g"], [""]))
  
         self.assertTrue(same_string_iterator(["abc","d","ef","g"], ["abc", "defg"]))
         self.assertFalse(same_string_iterator(["abc","d","ef","g"], ["abc", "def"]))
         

if __name__ == '__main__':
    unittest.main()
