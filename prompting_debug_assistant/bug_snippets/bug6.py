def top_n_words(sentence, n):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq[word] + 1
    sorted_words = sorted(freq, key=freq.get, reverse=True)
    return sorted_words[:n]

def multiply_string_times(text, times):
    return text * times

text = "hello "
times = 3.0
print(multiply_string_times(text, times))

sentence = "the cat sat on the mat the cat"
print(top_n_words(sentence, 2))