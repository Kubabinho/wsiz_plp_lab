import re
from collections import Counter


def zad1(text):
    paragraph = text.strip().split('\n')
    numParagraph = len(paragraph)

    zad = re.split(r'[.!?]+', text)

    numZad = len([s for s in zad if s.strip()])

    words = text.split()
    wordNum = len(words)

    stop_words = {'i', 'o', 'a', 'z', 'w', 'u'}

    filter_words = filter(lambda word: word not in stop_words, words)
    filter_wordsNumb = Counter(filter_words)

    print(numParagraph)
    print(numZad)
    print(wordNum)




text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

zad1(text)