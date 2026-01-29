def count_vowels(text):
    count = 0
    for c in text:
        if c in "aeiouAEIOU":  # ❌ bug subtil : oublie les lettres accentuées
            count += 1
    return count
