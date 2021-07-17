from doctest import testmod
import challenges as ch
import re
import os

"""
STUDENTS MAY SEE THIS FILE

STUDENTS SHOULD NOT MODIFY THIS FILE

STUDENTS SHOULD COPY THEIR CODE INTO THE FUNCTIONS IN THE CHALLENGES.PY FILE
"""


def pending_machine(num):
    """
    >>> pending_machine(1)
    ampharos
    >>> pending_machine(2)
    blastoise
    >>> pending_machine(3)
    cyndaquil
    >>> pending_machine(-1)
    grimer
    >>> pending_machine(25)
    Not accepted
    """
    return ch.pending_machine(num)


def scramble(randomWord, letter):
    """
    >>> scramble("Andrew", "n")
    (['A', 'n', 'd', 'e'], ['r', 'w'])
    >>> scramble("Oski", "k")
    (['k', 'i'], ['O', 's'])
    >>> scramble("Aidan", "A")
    (['A', 'a'], ['i', 'd', 'n'])
    >>> scramble("Jennifer", "r")
    (['J', 'e', 'n', 'n', 'i', 'f', 'e', 'r'], [])
    >>> scramble("Elizabeth", "e")
    (['E', 'a', 'b', 'e'], ['l', 'i', 'z', 't', 'h'])
    """
    return ch.scramble(randomWord, letter)


def wacky_numbers(carolNum, oskiNum, numrounds):
    """
    >>> wacky_numbers(2, 3, 5) # carol=2+4=6,oski=3. oski is less than carol so Carol wins
    Carol
    >>> wacky_numbers(3, 3, 4)
    Tie
    >>> wacky_numbers(4, 5, 25)
    Carol
    >>> wacky_numbers(4, 3, 12)
    Oski
    >>> wacky_numbers(5, 3, 2)
    Tie
    """
    return ch.wacky_numbers(carolNum, oskiNum, numrounds)


def double_trouble(randomWord):
    """
    >>> double_trouble("What Will Happen?")
    5
    >>> double_trouble("Apple")
    1
    >>> double_trouble("Alabama")
    0
    >>> double_trouble("Vitruvius")
    3
    >>> double_trouble("Succession")
    1
    """
    return ch.double_trouble(randomWord)


def rotCipher(word1, word2):
    """
    >>> rotCipher("Elephant", "Phantele")
    True
    >>> rotCipher("NonNon", "NonNon")
    True
    >>> rotCipher("Stanfurd", "Furdnsatn")
    False
    >>> rotCipher("Oski", "Kios")
    True
    >>> rotCipher("Berkeley", "Yelekreb")
    False
    """
    return ch.rotCipher(word1, word2)


def robot_triplet(team_weights, target):
    """
    >>> robot_triplet([1, 2, 3, 4, 5, 6], 15)
    [(4, 5, 6)]
    >>> robot_triplet([1, 2, 3, 4, 5], 13)
    []
    >>> robot_triplet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 14)
    [(1, 2, 11), (1, 3, 10), (1, 4, 9), (1, 5, 8), (1, 6, 7), (2, 3, 9), (2, 4, 8), (2, 5, 7), (3, 4, 7), (3, 5, 6)]
    >>> robot_triplet([], 10)
    []
    >>> robot_triplet([1,2,3,4,5], 0)
    []
    """
    return ch.robot_triplet(team_weights, target)


def reverse_lower(string):
    """
    >>> reverse_lower('OskI')
    'OksI'
    >>> reverse_lower('PoWeFuL')
    'PuWeFoL'
    >>> reverse_lower("WAHWaSa")
    'WAHWaSa'
    >>> reverse_lower("He!lo.")
    'Ho!le.'
    >>> reverse_lower("NumB3r5")
    'NrmB3u5'
    """
    return ch.reverse_lower(string)


def travel(stations):
    """
    >>> travel([2, 3, 1, 1, 4])
    1
    >>> travel([1, 1])
    0
    >>> travel([0, 3, 2])
    -1
    >>> travel([1, 1, 1, 1])
    2
    >>> travel([1, 2, 2, 1, 0, 1])
    2
    """
    return ch.travel(stations)


if __name__ == '__main__':
    os.system('clear')
    bars = ""
    for _ in range(70):
        bars = bars + "-"

    illegal_character_sequences = "(\.sort\()|(\Aimport )|(\nimport )"
    illegal_character_messages = {
        1: "found illegal method sort on line",
        2: "found illegal import on line",
        3: "found illegal import on line"
    }
    challenges_file = open("challenges.py", "r")
    illegal_characters = re.search(illegal_character_sequences, challenges_file.read())
    print(bars.replace("-", "#"))
    print("Starting disallowed character sequences test:")
    print("---")
    num_illegal_characters = 0
    line_processed_up_to = 0
    while illegal_characters != None:
        line_processed_up_to += illegal_characters.span()[1]
        num_illegal_characters += 1
        challenges_file.seek(0)
        num_newlines = challenges_file.read().count("\n", 0, line_processed_up_to)
        for i in illegal_character_messages.keys():
            if illegal_characters.group(i) != None:
                print(illegal_character_messages[i], num_newlines + 1, "of challenges.py")
                break
        challenges_file.seek(line_processed_up_to)
        illegal_characters = None
        illegal_characters = re.search(illegal_character_sequences, challenges_file.read())
    print("---")
    if num_illegal_characters:
        print("[FAILED] found", num_illegal_characters, "disallowed character sequences in challenges.py.")
    else:
        print("[PASSED] disallowed character sequences test.")
    print(bars.replace("-", "#"))
    print()
    challenges_file.close()

    testmod(name='tests', verbose=False)

    print(bars)
    if num_illegal_characters:
        print("[FAILED] found", num_illegal_characters, "disallowed character sequences in challenges.py.")
    else:
        print("[PASSED] disallowed character sequences test.")
    print(bars)
