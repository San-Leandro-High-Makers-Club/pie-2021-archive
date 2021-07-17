# Spring 2021 PiE Coding Challenges
# San Leandro High School Makers Club
# https://www.slmakers.com/

def pending_machine(num):
    if num == 1:
        print("ampharos")
    elif num == 2:
        print("blastoise")
    elif num == 3:
        print("cyndaquil")
    elif num == 4:
        print("dewgong")
    elif num < 1:
        print("grimer")
    else:
        print("Not accepted")


def scramble(word, letter):
    before = []
    after = []
    letter = letter.lower()

    for i in range(len(word)):
        currentChar = word[i].lower()
        if currentChar <= letter:
            before += [word[i]]  # Not currentChar, because we want to preserve case
        else:
            after += [word[i]]

    return before, after


def wacky_numbers(carolNum, oskiNum, numrounds):
    carol_score, oski_score, final = 0, 0, ""
    for i in range(0, numrounds):
        if i % carolNum == 0:
            carol_score += i
            if carol_score > oski_score:
                final = "Carol"
        if i % oskiNum == 0:
            oski_score += i
            if oski_score > carol_score:
                final = "Oski"
        if carol_score == oski_score:
            final = "Tie"
    print(final)


def double_trouble(word):
    count = 0
    checkedChars = []  # Stores all letters whose occurrences have been counted already at any point

    word = word.lower()  # Not sure if this is necessary

    if not word.isalpha():
        newWord = ""
        for i in range(len(word)):
            if word[i].isalpha():
                newWord += word[i]
        word = newWord

    for i in range(len(word)):
        if checkedChars.count(word[i]) <= 0:
            # We have not seen this letter in the word before
            checkedChars += [word[i]]  # Remember that we have seen this letter
            if word.count(word[i]) == 2:
                count += 1

    return count


def rotCipher(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    if not len(word1) == len(word2):
        return False

    for i in range(len(word1)):
        firstPart = word2[i:len(word2)]
        lastPart = word2[0:i]
        if firstPart + lastPart == word1:
            return True

    return False


def robot_triplet(team_weights, target):
    combinations = []

    for first in range(len(team_weights) - 2):
        for second in range(first + 1, len(team_weights) - 1):
            for third in range(first + 2, len(team_weights)):
                if team_weights[first] + team_weights[second] + team_weights[third] == target:
                    weights = [team_weights[first], team_weights[second], team_weights[third]]
                    minimum = min(weights)
                    weights.remove(minimum)
                    middle = min(weights)
                    weights.remove(middle)
                    maximum = weights[0]

                    candidate = (minimum, middle, maximum)
                    if candidate not in combinations and candidate[0] != candidate[1] and candidate[1] != candidate[2]:
                        combinations += [candidate]

    return combinations


def reverse_lower(string):
    parse = [char for char in string]
    item, item_2, item_3 = [], [], []
    word = ""

    for index, letter in enumerate(parse):
        if letter.islower():
            item.append(letter)
            item_2.append(index)
    item_2.reverse()
    for i in range(0, len(item)):
        item_3.append([item[i], item_2[i]])

    for i in range(0, len(item_3)):
        parse.pop(item_3[i][1])
        parse.insert(item_3[i][1], item_3[i][0])

    return word.join(parse)


def travel(stations):
    # stations[0] is the current number of gallons

    if len(stations) == 1:
        return 0  # Arrived

    if stations[0] == 0:
        return -1  # Can't continue, out of gas

    # First try getting gas
    numStopsIfGetting = 1
    nextSituation = stations[1:len(stations)]
    nextSituation[0] += stations[0] - 1  # Add whatever gas is leftover
    result = travel(nextSituation)
    canArriveIfGetting = True
    if result == -1:
        canArriveIfGetting = False
    numStopsIfGetting += result

    # Hold that thought. We will return numStopsIfGetting only if it represents a valid route and it is less than
    # numStopsIfSkipping

    # Try to avoid getting gas
    numStopsIfSkipping = 0
    nextSituation = stations[1:len(stations)]
    nextSituation[0] = stations[0] - 1  # We'll only have whatever is leftover
    result = travel(nextSituation)
    canArriveIfSkipping = True
    if result == -1:
        canArriveIfSkipping = False
    numStopsIfSkipping += result

    if not (canArriveIfGetting == canArriveIfSkipping):
        # We have no choice
        if canArriveIfSkipping:
            return numStopsIfSkipping
        else:
            return numStopsIfGetting
    elif (not canArriveIfGetting) and (not canArriveIfSkipping):
        return -1  # Can't make it
    else:
        assert canArriveIfGetting and canArriveIfSkipping
        return min(numStopsIfGetting, numStopsIfSkipping)
