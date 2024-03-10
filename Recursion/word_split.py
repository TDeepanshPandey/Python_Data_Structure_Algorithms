def word_split(phrase, list_of_words, output = None):
    # Base case: if the phrase is empty, return an empty list
    if output is None:
        output = []

    # Check if the phrase can be split into words
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            # Recursively split the remaining phrase
            return word_split(phrase[len(word):], list_of_words, output)

    return output

print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split('themanran',['clown','ran','man']))