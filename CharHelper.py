import random


def getRandomCharacter():
    charsASCII = range(48, 58) + range(65, 91) + range(97, 124)
    return chr(random.choice(charsASCII))
    # chars = "0123456789abcdefghijklmnopqrxtuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ"
    # return chars[random.randrange(0, len(chars))]


def getRandomCharacters(length):
    result = ''
    for i in range(0, length):
        result += getRandomCharacter()

    return result
