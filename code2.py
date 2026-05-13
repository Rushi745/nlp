# =========================================================
# COMPLETE NLP PRACTICAL PROGRAMS
# =========================================================


# =========================================================
# Q1. TOKENIZATION TASK
# =========================================================

# Input paragraph
text = "Natural Language Processing is interesting. Python makes NLP easy."

# Split into sentences
sentences = text.split(".")

print("Sentences:")
for s in sentences:
    if s != "":
        print(s)

# Split into words
words = text.split()

print("\nWords:")
print(words)

# Count total tokens
print("\nTotal Tokens:", len(words))


# =========================================================
# Q2. STOPWORD REMOVAL
# =========================================================

# Input sentence
sentence = "this is a simple NLP program"

# Stopword list
stopwords = ["is", "a"]

# Split sentence into words
words = sentence.split()

# Empty list for cleaned words
clean_words = []

# Remove stopwords
for word in words:
    if word not in stopwords:
        clean_words.append(word)

# Join words back
clean_text = " ".join(clean_words)

print("\nOriginal Sentence:")
print(sentence)

print("\nCleaned Sentence:")
print(clean_text)


# =========================================================
# Q3. STEMMING VS LEMMATIZATION
# =========================================================

# List of words
words = ["playing", "worked", "studies", "better"]

print("\nOriginal Words:")
print(words)

# ---------------- STEMMING ----------------

print("\nStemming:")

for word in words:

    # Remove 'ing'
    if word.endswith("ing"):
        stem = word[:-3]

    # Remove 'ed'
    elif word.endswith("ed"):
        stem = word[:-2]

    # Convert ies -> y
    elif word.endswith("ies"):
        stem = word[:-3] + "y"

    else:
        stem = word

    print(word, "->", stem)

# ---------------- LEMMATIZATION ----------------

print("\nLemmatization:")

# Manual dictionary
lemma_dict = {
    "playing": "play",
    "worked": "work",
    "studies": "study",
    "better": "good"
}

# Convert into lemma form
for word in words:

    if word in lemma_dict:
        print(word, "->", lemma_dict[word])

    else:
        print(word, "->", word)


# =========================================================
# Q4. MORPHOLOGICAL ANALYSIS
# =========================================================

# Dictionary of words and morphemes
words = {
    "unhappiness": ["un", "happy", "ness"],
    "replayed": ["re", "play", "ed"],
    "international": ["inter", "nation", "al"]
}

# Free morphemes
free_morphemes = ["happy", "play", "nation"]

print("\nMorphological Analysis:\n")

# Access each word
for word, morphemes in words.items():

    print("Word:", word)

    # Check morphemes
    for m in morphemes:

        if m in free_morphemes:
            print(m, "-> Free Morpheme")

        else:
            print(m, "-> Bound Morpheme")

    print()


# =========================================================
# Q5. PART OF SPEECH TAGGING
# =========================================================

# Input sentence
sentence = "Ram is running quickly in the garden"

# Split into words
words = sentence.split()

print("\nPOS Tagging:\n")

# Apply rules
for word in words:

    # Rule for adverb
    if word.endswith("ly"):
        tag = "Adverb"

    # Rule for verb
    elif word.endswith("ing"):
        tag = "Verb"

    # Rule for helping verb
    elif word in ["is", "am", "are", "was", "were"]:
        tag = "Helping Verb"

    # Rule for preposition
    elif word in ["in", "on", "at"]:
        tag = "Preposition"

    # Rule for article
    elif word in ["the", "a", "an"]:
        tag = "Article"

    else:
        tag = "Noun"

    print(word, "->", tag)


# =========================================================
# Q6. AMBIGUITY DETECTION
# =========================================================

# Ambiguous sentences
sentences = [
    "I saw the man with a telescope",
    "He went to the bank"
]

print("\nAmbiguity Detection:\n")

# Check ambiguity type
for sentence in sentences:

    # Syntactic ambiguity
    if "with" in sentence:
        ambiguity = "Syntactic Ambiguity"

    # Semantic ambiguity
    elif "bank" in sentence:
        ambiguity = "Semantic Ambiguity"

    else:
        ambiguity = "No Ambiguity"

    print("Sentence:", sentence)
    print("Type:", ambiguity)
    print()


# =========================================================
# Q7. BAG OF WORDS
# =========================================================

# List of sentences
sentences = [
    "I like NLP",
    "I like Python",
    "Python is easy"
]

# Empty vocabulary list
vocab = []

# Create vocabulary
for sentence in sentences:

    words = sentence.split()

    # Add unique words
    for word in words:

        if word not in vocab:
            vocab.append(word)

print("\nVocabulary:")
print(vocab)

print("\nBag of Words Matrix:\n")

# Create matrix
for sentence in sentences:

    words = sentence.split()

    row = []

    # Count frequency
    for v in vocab:
        row.append(words.count(v))

    print(row)


# =========================================================
# Q8. TF-IDF (MANUAL TF)
# =========================================================

# Input document
document = "NLP is easy and NLP is interesting"

# Split document into words
words = document.split()

# Count total words
total_words = len(words)

print("\nTF Values:\n")

# Find TF of each word
for word in set(words):

    # Count frequency
    frequency = words.count(word)

    # Calculate TF
    tf = frequency / total_words

    print(word, "->", round(tf, 2))


# =========================================================
# Q9. COSINE SIMILARITY
# =========================================================

# Import math module
import math

# Input vectors
A = [1, 2, 3]
B = [2, 1, 3]

# Dot product variable
dot_product = 0

# Calculate dot product
for i in range(len(A)):
    dot_product += A[i] * B[i]

# Magnitude of A
sumA = 0

for x in A:
    sumA += x * x

magnitudeA = math.sqrt(sumA)

# Magnitude of B
sumB = 0

for x in B:
    sumB += x * x

magnitudeB = math.sqrt(sumB)

# Cosine similarity
cosine_similarity = dot_product / (magnitudeA * magnitudeB)

print("\nCosine Similarity =", round(cosine_similarity, 2))


# =========================================================
# Q11. NAIVE BAYES CLASSIFICATION
# =========================================================

# Prior probabilities
P_spam = 0.6
P_ham = 0.4

# Likelihood probabilities
P_offer_spam = 0.5
P_offer_ham = 0.1

# Calculate probabilities
spam_probability = P_spam * P_offer_spam
ham_probability = P_ham * P_offer_ham

print("\nSpam Probability =", spam_probability)
print("Ham Probability =", ham_probability)

# Classification
if spam_probability > ham_probability:
    print("\nResult: Message is SPAM")

else:
    print("\nResult: Message is HAM")


# =========================================================
# Q12. HIDDEN MARKOV MODEL (HMM)
# =========================================================

# Transition probability
transition = 0.7

# Emission probability
emission = 0.6

# Final probability
probability = transition * emission

print("\nHMM Probability =", probability)


# =========================================================
# Q13. N-GRAM TEXT GENERATION
# =========================================================

# Input text
text = "I love NLP and NLP loves Python"

# Split text into words
words = text.split()

print("\nGenerated Bigrams:\n")

# Generate bigrams
for i in range(len(words)-1):
    print(words[i], "->", words[i+1])


# =========================================================
# Q14. BLEU SCORE
# =========================================================

# Reference sentence
reference = ["I", "love", "Python"]

# Candidate sentence
candidate = ["I", "love", "Java"]

# Matching word counter
match = 0

# Count matching words
for word in candidate:

    if word in reference:
        match += 1

# Calculate BLEU score
score = match / len(candidate)

print("\nBLEU Score =", round(score, 2))


# =========================================================
# Q15. REGEX BASED TEXT CLEANING
# =========================================================

# Import regex module
import re

# Input text
text = "Hello123!!! NLP@2025"

# Remove numbers
text = re.sub(r'[0-9]', '', text)

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Convert to lowercase
text = text.lower()

print("\nCleaned Text:")
print(text)


# =========================================================
# Q16. CONTEXT FREE GRAMMAR PARSING
# =========================================================

# Input sentence
sentence = "Ram eats mango"

# Split sentence into words
words = sentence.split()

# Check sentence structure
if len(words) == 3:
    print("\nValid Sentence")

else:
    print("\nInvalid Sentence")


# =========================================================
# Q17. CHUNKING
# =========================================================

# Sentence with POS tags
sentence = [
    ("The", "Det"),
    ("big", "Adj"),
    ("dog", "Noun")
]

# Check noun phrase pattern
if sentence[0][1] == "Det" and sentence[1][1] == "Adj":
    print("\nNoun Phrase Found")

else:
    print("\nNo Noun Phrase")


# =========================================================
# Q18. RNN SENTIMENT ANALYSIS
# =========================================================

# Import required libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Create model
model = Sequential()

# Add RNN layer
model.add(SimpleRNN(10, input_shape=(5,1)))

# Add output layer
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy')

# Display summary
print(model.summary())


# =========================================================
# Q19. NAMED ENTITY RECOGNITION
# =========================================================

# Input sentence
sentence = "Rushi lives in Mumbai"

# Split sentence into words
words = sentence.split()

print("\nNamed Entities:\n")

# Check capitalized words
for word in words:

    # Named entities start with capital letters
    if word[0].isupper():
        print(word, "-> Named Entity")