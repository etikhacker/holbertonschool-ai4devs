def top_n_words(sentence, n):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    sorted_words = sorted(freq, key=freq.get, reverse=True)
    return sorted_words[:n]

def multiply_string_times(text, times):
    return text * int(times)

def main():
    sentence = "the cat sat on the mat the cat"
    result = top_n_words(sentence, 2)
    assert result == ["the", "cat"], "Test 1 failed"

    assert multiply_string_times("hello ", 3.0) == "hello hello hello ", "Test 2 failed"
    assert multiply_string_times("ab", 2) == "abab", "Test 3 failed"

    print("bug6_fixed.py: All tests passed")

main()
