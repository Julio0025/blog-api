import re
from pyphonetics import Soundex


def soundex_filter(words, keyword):
    """
    Function that takes in a string of words and a keyword
    and compares keyword soundex result with each word.
    :param words:
    :param keyword:
    :return matched_words (list):
    """
    soundex = Soundex()
    search_argument = soundex.phonetics(keyword)
    matched_words = []
    words = re.split(r"[\s\W0-9]", words)
    for word in words:
        if word:
            result = soundex.phonetics(word)
            if search_argument == result:
                matched_words.append(word)

    return matched_words
