# wanted to see how a recursive solution might work for this problem: https://www.youtube.com/watch?v=2g_b1aYTHeg
# Essentially same solution as video but using an ordered list and recurstioin instead
# I found that the code is more compact but has higher memory useage. THe Sorting is implicit in the link in the list and may have a better order
# Still, interesting exercise.

from collections import Counter
from collections import namedtuple
from itertools import chain


CharOccurance = namedtuple("CharOccurance", ["char", "occurances"])


def sort_occurances(occurances):
    """ensure the char with the most occurances are first in the list
    Args:
        occurances List of CharOccurance objects
    Returns:
        list of CharOccurance ordered by occurance (max first)
    """
    return sorted(occurances, key=lambda i: i.occurances, reverse=True)


def to_frequency_of_characters(text):
    """workout how many occurances of a character appears in the string.
    Args:
       a String of characters
    Returns:
        a list of {char:<character>, ocuurance: <number of times the characters appear in the text>}) objects
        ordered by the most frequebtly occuring charcter first
    """
    return sort_occurances(
        map(lambda i: CharOccurance(i[0], i[1]), Counter(text).items())
    )


def decrease_occurance(character_occurance):
    """reduce the occurance count in the object (char: <char>, occurance: <occurance of the character>) by one
        e.g a parameter of (char: 'a', occurance: 1) returns (char: 'a', occurance: 1)
    Args:
       CharOccurance object you want to decrease the occurance for.
    Returns:
        a copy of the input with it's occurance count reduced by one.
    """
    return CharOccurance(character_occurance.char, character_occurance.occurances - 1)


def __isolate_characters(character_occurances):
    """ensure that two characters in the sequence are aren't adjecent to each other
       will return a value error if it's not possible to return a string that that
       represents

       For example ["a", "j". "j", "a", "b". "b", "c", "f", "f" , "f". "f". "d", "f", "f", "f"]
       becommes: "fafafjfjfbfbfcd"
    Args:
        character_occurances : an array to characters that you to aranage so the same character
        isn't ajecent to itself. note upper case characters are considered different to lowercase
        characters
    Raises:
        ValueError: if there is no way to rearrange the list to meet the constraint
    Returns:
        String that meets the constraint above
    """
    if character_occurances is None or len(character_occurances) == 0:
        return ""
    if len(character_occurances) == 1 and character_occurances[0].occurances > 1:
        raise ValueError()  # can't meet the requirement that chars can be adjent to each other
    if len(character_occurances) == 1:
        return character_occurances[0].char
    [char_occurance1, char_occurance2] = character_occurances[:2]
    next_round = sort_occurances(
        chain(
            filter(
                lambda l: l.occurances,
                [
                    decrease_occurance(char_occurance1),
                    decrease_occurance(char_occurance2),
                ],
            ),
            character_occurances[2:],
        )
    )
    return char_occurance1.char + char_occurance2.char + __isolate_characters(next_round)


def isolate_characters(text):
    """ensure the same characterr isnt found adjecent to itself in the string
        e.g ""ajjabbcffffdfff" would return "fafafjfjfbfbfcd"

        implementation of this: https://www.youtube.com/watch?v=2g_b1aYTHeg

    Args:
        text text  you want to seperate
    Returns:
        a atring with the characters seperated or "" if not possible
    """
    try:
        return __isolate_characters(to_frequency_of_characters(text))
    except ValueError:
        return ""


if __name__ == "__main__":
    print(isolate_characters("ajjabbcffffdfff"))
