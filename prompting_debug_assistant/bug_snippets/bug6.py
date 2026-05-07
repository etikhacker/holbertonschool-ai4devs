# Bug 6 – bug6.py
# Intended: Count word frequency in a sentence and return top-N words.

def top_n_words(sentence, n):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq[word] + 1  # BUG: KeyError on first occurrence; should use freq.get(word, 0) + 1

    # Sort by frequency descending
    sorted_words = sorted(freq, key=freq.get, reverse=True)

    return sorted_words[:n]


# Second bug: type confusion
def multiply_string_times(text, times):
    return text * times   # Works fine for strings, but caller passes float accidentally

text = "hello "
times = 3.0    # BUG: int expected, float given → TypeError: can't multiply sequence by non-int of type 'float'
print(multiply_string_times(text, times))


# Test for top_n_words
sentence = "the cat sat on the mat the cat"
print(top_n_words(sentence, 2))
# Expected: ['the', 'cat']
# Actual:   KeyError: 'the'