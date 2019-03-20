import re


def soundex(string):
    """
    soundex algorithm from https://en.wikipedia.org/wiki/Soundex
    """
    s = string
    first_letter = s[0].upper()
    s = s[1:]
    s = re.sub(r'[aeiouyhw]', '', s)
    s = re.sub(r'[bfpv]', '1', s)
    s = re.sub(r'[cgjkqsxz]', '2', s)
    s = re.sub(r'[dt]', '3', s)
    s = re.sub(r'[l]', '4', s)
    s = re.sub(r'[mn]', '5', s)
    s = re.sub(r'[r]', '6', s)

    s = first_letter + s
    if len(s) > 3:
        s = s[:4]
    elif len(s) <= 3:
        while len(s) <= 3:
            s += '0'
    return s


def soundex_filter(words, keyword):
    """
    Function that takes in a string of words and a keyword
    and compares keyword soundex result with each word.
    """

    search_argument = soundex(keyword)
    matched_words = []
    words = re.split(r'[^A-Za-z]+', words)
    for word in words:
        if word:
            result = soundex(word)
            if search_argument == result:
                matched_words.append(word)

    return matched_words
