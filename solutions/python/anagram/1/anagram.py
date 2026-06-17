def find_anagrams(word, candidates):
    lower_word = word.lower()
    result = []
    for candidate in candidates:
        lower_candidate = candidate.lower()
        if sorted(lower_candidate)==sorted(lower_word) and lower_word!=lower_candidate:
            result.append(candidate)
    return result