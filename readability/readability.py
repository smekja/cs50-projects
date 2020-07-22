import cs50
# Counting letters in text
def letter_count(text):
    letters = 0
    for char in text:
        x = ord(char)
        if x > 64 and x < 91 or x > 96 and x < 123:
            letters += 1
    return letters
# Counting words in text
def word_count(text):
    words = 1
    for char in text:
        if char == " ":
            words = words + 1
    return words
# Counting sentences in text
def sentence_count(text):
    sentences = 0
    for char in text:
        if char == "." or char == "?" or char == "!":
            sentences += 1
    return sentences
# Counting L for index
def count_L(letters, words):
    if words < 101:
        L = float(letters) * 100 / float(words)
        return L
    if words > 100:
        L = float(letters) * float(words) / 100
        return L
# Counting S for index
def count_S(sentences, words):
    if words < 101:
        S = float(sentences) * 100 / float(words)
        return S
    if words > 100:
        S = float(sentences) * float(words) / 100
        return S

text = cs50.get_string("Text: ")

letters = letter_count(text)
words = word_count(text)
sentences = sentence_count(text)
L = count_L(letters, words)
S = count_S(sentences, words)
index = 0.0588 * L - 0.296 * S - 15.8
index = round(index)

# printing the resulting grade
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print ("Grade 16+")
else:
    print("Grade", index)

