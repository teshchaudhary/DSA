"""

You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k

"""

def count_valid_substrings(word, allowed_consonants):
    vowel_freq = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  
    left = 0  # Left boundary of the sliding window
    start = 0  # Start of valid substring count
    unique_vowel_count = 0  # Number of distinct vowels in the window
    valid_substring_count = 0  # Stores count of valid substrings

    for char in word:
        if char in vowel_freq:
            vowel_freq[char] += 1
            if vowel_freq[char] == 1:
                unique_vowel_count += 1
        else:
            allowed_consonants -= 1  # Reduce remaining allowed consonants

        while allowed_consonants < 0 or (unique_vowel_count == 5 and vowel_freq.get(word[left], 0) > 1):
            left_char = word[left]
            left += 1

            if left_char in vowel_freq:
                vowel_freq[left_char] -= 1
                if vowel_freq[left_char] == 0:
                    unique_vowel_count -= 1
            else:
                allowed_consonants += 1  
                start = left  # Move start of valid substring count
                   
        if unique_vowel_count == 5 and allowed_consonants == 0:
            valid_substring_count += left - start + 1

    return valid_substring_count
