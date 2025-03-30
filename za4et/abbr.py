def abbreviation(fullPhrase):
    wordsOfPhrase = fullPhrase.split()
    abbreviation = ""
    for currentWord in wordsOfPhrase:
        if currentWord and currentWord[0].isalpha():
            abbreviation += currentWord[0].upper()

    return abbreviation

print(abbreviation("мяу гав"))