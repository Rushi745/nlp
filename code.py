
# =========================================================
# COMPLETE NLP PRACTICAL PROGRAMS
# =========================================================

# Q1. TOKENIZATION TASK

text = "Natural Language Processing is interesting. Python makes NLP easy."

sentences = text.split(".")

print("Sentences:")
for s in sentences:
    if s != "":
        print(s)

words = text.split()

print("\nWords:")
print(words)

print("\nTotal Tokens:", len(words))


# Q2. STOPWORD REMOVAL

sentence = "this is a simple NLP program"

stopwords = ["is", "a"]

words = sentence.split()

clean_words = []

for word in words:
    if word not in stopwords:
        clean_words.append(word)

clean_text = " ".join(clean_words)

print("\nOriginal Sentence:")
print(sentence)

print("\nAfter Stopword Removal:")
print(clean_text)


# Q3. STEMMING VS LEMMATIZATION

words = ["playing", "worked", "studies", "better"]

print("\nOriginal Words:")
print(words)

print("\nStemming Results:")

for word in words:

    if word.endswith("ing"):
        stem = word[:-3]

    elif word.endswith("ed"):
        stem = word[:-2]

    elif word.endswith("ies"):
        stem = word[:-3] + "y"

    else:
        stem = word

    print(word, "->", stem)

print("\nLemmatization Results:")

lemma_dict = {
    "playing": "play",
    "worked": "work",
    "studies": "study",
    "better": "good"
}

for word in words:

    if word in lemma_dict:
        print(word, "->", lemma_dict[word])

    else:
        print(word, "->", word)


# Q4. MORPHOLOGICAL ANALYSIS

words = {
    "unhappiness": ["un", "happy", "ness"],
    "replayed": ["re", "play", "ed"],
    "international": ["inter", "nation", "al"]
}

free_morphemes = ["happy", "play", "nation"]

print("\nMorphological Analysis:\n")

for word, morphemes in words.items():

    print("Word:", word)

    for m in morphemes:

        if m in free_morphemes:
            print(m, "-> Free Morpheme")

        else:
            print(m, "-> Bound Morpheme")

    print()


# Q5. PART OF SPEECH TAGGING

sentence = "Ram is running quickly in the garden"

words = sentence.split()

print("\nPOS Tagging:\n")

for word in words:

    if word.endswith("ly"):
        tag = "Adverb"

    elif word.endswith("ing"):
        tag = "Verb"

    elif word in ["is", "am", "are", "was", "were"]:
        tag = "Helping Verb"

    elif word in ["in", "on", "at"]:
        tag = "Preposition"

    elif word in ["the", "a", "an"]:
        tag = "Article"

    else:
        tag = "Noun"

    print(word, "->", tag)


# Q6. AMBIGUITY DETECTION

sentences = [
    "I saw the man with a telescope",
    "He went to the bank"
]

print("\nAmbiguity Detection:\n")

for sentence in sentences:

    if "with" in sentence:
        ambiguity = "Syntactic Ambiguity"

    elif "bank" in sentence:
        ambiguity = "Semantic Ambiguity"

    else:
        ambiguity = "No Ambiguity"

    print("Sentence:", sentence)
    print("Type:", ambiguity)
    print()

