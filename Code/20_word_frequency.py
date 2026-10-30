import string

def word_frequency(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    frequency = {}

    for word in sentence.split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

sentence = "Hello, world! Hello Python."
print("Word frequency:", word_frequency(sentence))