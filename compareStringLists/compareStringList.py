#--------------------------------------------------------------------
# variation of this string comprision exercise using lazy iterators and 
# generators rather that index manipulation. 
# 
#   https://www.youtube.com/watch?v=ejBwc2oE7ck&t=325s
# 
# This gives a couple of advantages
#
# 1. seperate of functionality/concerns: mapping a list of strings to a list of characters
#    is seperate from the algorithm making the seperate parts testable and hides the complexity
#    mapping characters from strings from the comparision algorithm, makin code easier to follow
#  2. can use lazy iterator functions to solve the problem - less code to write (see same_string_functional) 
# 
#--------------------------------------------------------------------



from itertools import zip_longest


def chars_in_strings(string_array):
    """creates an iterable that lazily generates all the characters from all the strings in the list
       e.g ["abc","l"."jk"] would lazily generate the character list ["a", "b", "c","l","j","k"]
    Args:
        string_array  a list of strings that you want to iterate over, char by char
    Yields:
        a  character from the list.
    """
    for word in string_array:
      for letter in list(word):
        yield letter


#--------------------------------------------------------------------
# solution using lazy iterators
#--------------------------------------------------------------------

def any_matching(match_function, iterable):
    """Returns true if any of the value in the iterator return true to the match function"""
    return any(filter(match_function, iterable))


def same_string_functional(string_list1, string_list2):
    """ do the two list of string produce the same string when contacted together?
        (using lazy iteration functions to minimise iterations and memory)
    Args:
        string_list1: list of strings to compare
        string_list2 list of strings to compare
    Returns:
      true if the two lists produce the same string when concatinated, false if not
    """
    return not any_matching(
        lambda letter_pair: letter_pair[0] != letter_pair[1],
        zip_longest(chars_in_strings(string_list1), chars_in_strings(string_list2)),
    )

#--------------------------------------------------------------------
# alternarive usimg iteration
#--------------------------------------------------------------------


def same_string_iterator(string_list1, string_list2):
    """ do the two list of string produce the same string when contacted together?
        (do this using lazy iteration to save memory via a while loop)
    Args:
        string_list1: list of strings to compare
        string_list2 list of strings to compare
    Returns:
      true if the two lists produce the same string when concatinated, false if not
    """
    i1 = chars_in_strings(string_list1)
    i2 = chars_in_strings(string_list2)
    c1 = next(i1, None)
    c2 = next(i2, None)
    while c1 is not None and c2 is not None and c1 == c2:
        c1 = next(i1, None)
        c2 = next(i2, None)
    return c1 is None and c2 is None
